"""
vehiculos.py
============
Define la clase Vehiculo — el agente central de la simulación.

Cada vehículo es un agente independiente que:
    - Calcula su ruta óptima sobre el grafo del Circuito Comercial.
    - Se mueve nodo a nodo respetando los semáforos de cada intersección.
    - Reporta su estado en tiempo real a través de una cola multiproceso.
    - Corre en su propio hilo dentro de un proceso asignado a un núcleo de CPU.
"""

import random
import time
from threading import Lock, Event
from queue import Queue

import networkx as nx


class Vehiculo:
    """
    Agente de tráfico que representa un vehículo circulando por el
    Circuito Comercial de Encarnación.

    Cada instancia corre en un hilo independiente dentro de un proceso
    asignado a un núcleo de CPU. El vehículo calcula rutas óptimas usando
    el algoritmo de Dijkstra (shortest_path con peso 'weight'), avanza nodo
    a nodo y elige un nuevo destino al llegar al actual.

    Atributos
    ---------
    id_vehiculo : int
        Identificador único del vehículo en toda la simulación.
    proceso_id : int
        Identificador del proceso (núcleo de CPU) al que pertenece este vehículo.
    nodo_actual : str
        Nombre de la intersección donde se encuentra el vehículo en este momento.
    destino : str
        Nombre de la intersección objetivo del viaje actual.
    ruta : list[str]
        Secuencia de nodos desde nodo_actual hasta destino.
    indice_ruta : int
        Posición actual dentro de la lista ruta.
    velocidad : int
        Velocidad del vehículo en km/h. Determina el tiempo entre nodos:
        tiempo_nodo = 30 / velocidad (segundos).
    estado : str
        Estado actual del vehículo: 'en_ruta', 'esperando' o 'llegado'.
    """

    def __init__(
        self,
        id_vehiculo: int,
        mapa: nx.DiGraph,
        origen: str,
        destino: str,
        velocidad: int,
        lock_mapa: Lock,
        report_queue: Queue,
        stop_event: Event,
        proceso_id: int,
    ):
        """
        Inicializa el vehículo, calcula su ruta inicial y ocupa el nodo de origen.

        Si el nodo de origen está al límite de capacidad (semáforo agotado),
        busca automáticamente otro nodo disponible para no bloquear la creación
        del proceso principal.

        Parámetros
        ----------
        id_vehiculo : int
            Identificador único del vehículo.
        mapa : nx.DiGraph
            Grafo dirigido del Circuito Comercial. Cada proceso tiene
            su propia copia — los procesos no comparten memoria.
        origen : str
            Nodo de partida del vehículo.
        destino : str
            Nodo objetivo del primer viaje.
        velocidad : int
            Velocidad en km/h (rango recomendado: 20-60).
        lock_mapa : Lock
            Candado de threading para proteger la escritura del contador
            de vehículos presentes (vp) en cada nodo.
        report_queue : Queue | MPQueue
            Cola donde el vehículo deposita su estado en cada tick.
            Es compartida entre todos los vehículos del mismo proceso
            y leída por el proceso principal (visualizador pygame).
        stop_event : Event | MPEvent
            Bandera compartida entre procesos. Cuando se activa, todos los vehículos terminan su loop de forma ordenada.
        proceso_id : int
            Número del proceso al que pertenece este vehículo (1, 2, ...).
            Se usa en el visualizador para asignar color por núcleo.
        """
        self.id_vehiculo = id_vehiculo
        self.proceso_id = proceso_id
        self.mapa = mapa
        self.lock_mapa = lock_mapa
        self.report_queue = report_queue
        self.stop_event = stop_event

        self.nodo_actual = origen
        self.destino = destino
        self.indice_ruta = 0
        self.velocidad = velocidad
        self.estado = "en_ruta"

        # Calcular la ruta óptima desde origen hasta destino
        self.ruta = self._calcular_ruta()

        while not self.mapa.nodes[self.nodo_actual]["semaforo"].acquire(blocking=False):
            self.nodo_actual = random.choice(list(self.mapa.nodes))
            self.ruta = self._calcular_ruta()

        # Registrar presencia del vehículo en el nodo inicial
        self.mapa.nodes[self.nodo_actual]["vp"] += 1

    # * Métodos de navegación
    def _calcular_ruta(self) -> list:
        """
        Calcula la ruta óptima desde nodo_actual hasta destino usando
        el algoritmo de Dijkstra con el campo 'weight' como costo.

        El campo 'weight' de cada arista representa la distancia en metros
        entre dos intersecciones.

        Retorna
        -------
        list[str]
            Lista ordenada de nombres de nodos desde origen hasta destino.
        """
        return nx.shortest_path(
            self.mapa, self.nodo_actual, self.destino, weight="weight"
        )

    def llego(self) -> bool:
        """
        Indica si el vehículo alcanzó su destino actual.
        Retorna: True si el índice de ruta apunta al último nodo de la ruta.
        """
        return self.indice_ruta >= len(self.ruta) - 1

    def avanzar(self):
        """
        Mueve el vehículo al siguiente nodo de su ruta.

        El movimiento respeta los semáforos de cada intersección:
        - Adquiere el semáforo del nodo siguiente antes de moverse.
        - Libera el semáforo del nodo actual al salir.
        - Actualiza el contador de vehículos presentes (vp) en ambos nodos bajo el lock_mapa para evitar race conditions.
        """
        if self.llego():
            return

        siguiente = self.ruta[self.indice_ruta + 1]
        sem_siguiente = self.mapa.nodes[siguiente]["semaforo"]
        sem_actual = self.mapa.nodes[self.nodo_actual]["semaforo"]

        # TODO: Reactivar cuando las capacidades del grafo OSM estén configuradas.
        # Este bloque implementa la espera activa: si el nodo siguiente está lleno,
        # el vehículo espera hasta que se libere un lugar.
        #
        # while not sem_siguiente.acquire(blocking=False):
        #     if self.stop_event.is_set():
        #         return
        #     self.estado = "esperando"
        #     self.send_state()
        #     time.sleep(0.5)

        sem_siguiente.acquire(blocking=False)

        # Mover al siguiente nodo y actualizar contadores bajo el mismo lock
        self.estado = "en_ruta"
        self.indice_ruta += 1
        nodo_anterior = self.nodo_actual
        self.nodo_actual = siguiente

        with self.lock_mapa:
            self.mapa.nodes[siguiente]["vp"] += 1
            self.mapa.nodes[nodo_anterior]["vp"] -= 1

        sem_actual.release()

        if self.llego():
            self.estado = "llegado"

    def elegir_nuevo_destino(self):
        """
        Selecciona un nuevo destino aleatorio al llegar al actual y
        recalcula la ruta.
        """
        # Obtener solo los nodos que tienen camino entre sí
        componente_principal = max(nx.strongly_connected_components(self.mapa), key=len)
        nodos_validos = list(componente_principal)
        nodos_validos.remove(self.nodo_actual)

        self.destino = random.choice(nodos_validos)
        self.ruta = self._calcular_ruta()
        self.indice_ruta = 0
        self.estado = "en_ruta"

    # * Comunicación y ciclo de vida
    def send_state(self):
        """
        Deposita el estado actual del vehículo en la cola de reporte.

        El proceso principal (visualizador pygame) lee esta cola cada frame
        para actualizar la posición de los vehículos en pantalla.
        El nombre completo del nodo se envía sin truncar para que el
        visualizador pueda encontrarlo en node_data.
        """
        self.report_queue.put(
            {
                "id": self.id_vehiculo,
                "nodo_actual": self.nodo_actual,
                "destino": self.destino,
                "estado": self.estado,
                "velocidad": self.velocidad,
                "proceso_id": self.proceso_id,
            }
        )

    def run(self):
        """
        Ciclo principal del vehículo — se ejecuta en un hilo independiente.

        En cada iteración el vehículo:
            1. Verifica si llegó a destino → elige uno nuevo.
            2. Si no llegó → avanza al siguiente nodo.
            3. Reporta su estado a la cola.
            4. Duerme según su velocidad, cediendo la CPU a otros hilos.

        El loop termina cuando stop_event es activado por el proceso principal.
        """
        while not self.stop_event.is_set():
            if self.llego():
                self.elegir_nuevo_destino()
            else:
                self.avanzar()

            self.send_state()

            # Tiempo de recorrido entre nodos según velocidad: velocidad 20 km/h → 1.5s por nodo
            time.sleep(30 / self.velocidad)
