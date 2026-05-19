"""
main.py
=======
Punto de entrada principal del Simulador de Tráfico — Encarnación.

Arquitectura del sistema
------------------------
El simulador usa una arquitectura híbrida de multiprocesamiento y multihilo:

Proceso Principal (este archivo)
├── Construye el mapa para pygame (initialize_map_nodes)
├── Lanza N procesos de simulación (start_parallel_simulation)
│     Proceso 1 → núcleo 0 → hilos de vehículos 0, 2, 4, ...
│     Proceso 2 → núcleo 1 → hilos de vehículos 1, 3, 5, ...
│     ...
└── Corre el game loop de pygame (visualización en tiempo real)
    Lee MPQueue → actualiza estado_vehiculos → dibuja en pantalla

Comunicación entre procesos
---------------------------
Los procesos de simulación envían el estado de cada vehículo a través
de una MPQueue (multiprocessing.Queue). El proceso principal lee esa
cola cada frame y actualiza el diccionario estado_vehiculos que el
visualizador usa para dibujar los puntos en pantalla.

Sincronización
--------------
Un MPEvent (multiprocessing.Event) actúa como señal de parada global.
Cuando el usuario cierra la ventana o presiona Escape, el proceso
principal activa el evento y todos los procesos de simulación terminan
de forma ordenada al completar su iteración actual.
"""

from threading import Thread, Lock
from multiprocessing import Process, Event as MPEvent, Queue as MPQueue, cpu_count
from queue import Empty

import networkx as nx
import random
import pygame

from graph_model import generate_graph
from vehiculos import Vehiculo
from pygame_utils.node import Node
from pygame_utils.coordinate_transform import normalized_to_screen
from pygame_utils.vehicle_color_palette import generar_paleta
from pygame_utils.constants import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    WINDOW_NAME,
    ZONA_COLORS,
    ZONA_EDGE_COLORS,
    ZONA_NODE_RADIUS,
)

N_VEHICULOS = 2


def renderizar_vehiculos(
    window: pygame.Surface, estado_vehiculos: dict, node_data: dict, paleta: list
):
    """
    Dibuja todos los vehículos activos sobre el mapa en la ventana pygame.

    Cada vehículo se representa como un círculo de 5px de radio. El color
    del círculo indica el proceso al que pertenece el vehículo y su estado:
        - en_ruta   → color del proceso (neón único por núcleo de CPU)
        - esperando → rojo alerta (#FF1744)
        - llegado   → gris azulado (#4A4A6A)

    Parámetros
    ----------
    window : pygame.Surface
        Superficie principal de pygame donde se dibuja.
    estado_vehiculos : dict
        Diccionario {id_vehiculo: estado} con el último estado conocido
        de cada vehículo, leído de la MPQueue.
    node_data : dict
        Diccionario {nombre_nodo: {"node_pos": (px, py), ...}} con las
        posiciones de pantalla precalculadas de cada intersección.
    paleta : list
        Lista de diccionarios de colores por proceso, generada por
        generar_paleta(). Índice 0 = proceso 1, índice 1 = proceso 2, etc.
    """
    for estado in estado_vehiculos.values():
        nombre_nodo = estado["nodo_actual"]

        if nombre_nodo not in node_data:
            continue

        proceso_id = estado.get("proceso_id", 1)
        color_vehiculo = paleta[(proceso_id - 1) % len(paleta)][estado["estado"]]
        posicion = node_data[nombre_nodo]["node_pos"]

        pygame.draw.circle(window, color_vehiculo, posicion, 5)


def initialize_map_nodes() -> tuple[list, dict]:
    """
    Construye los objetos Node de pygame y el diccionario de posiciones
    en pantalla a partir del grafo del Circuito Comercial.

    Esta función se llama solo en el proceso principal — el mapa pygame
    no se comparte con los procesos de simulación.

    El grafo se construye una vez aquí para obtener posiciones y vecinos.
    Cada proceso de simulación construye su propia copia del grafo
    internamente (en simular_grupo) porque los Semaphores de threading
    no son serializables entre procesos.

    Retorna
    -------
    nodes : list[Node]
        Lista de objetos Node listos para dibujar con draw_node().
    node_data : dict
        Diccionario {nombre_nodo: {"node_pos": (px, py), "neighbors": [...]}}
        con las posiciones de pantalla de cada intersección y sus vecinos.
    """
    mapa = generate_graph()

    # Precalcular posiciones de pantalla para cada nodo del grafo
    node_data = {}
    for nombre_nodo, atributos in mapa.nodes(data=True):
        posicion_pantalla = normalized_to_screen(
            atributos["pos"], WINDOW_WIDTH, WINDOW_HEIGHT
        )
        node_data[nombre_nodo] = {
            "node_pos": posicion_pantalla,
            "neighbors": [
                {
                    "id": vecino,
                    "pos": normalized_to_screen(
                        mapa.nodes[vecino]["pos"], WINDOW_WIDTH, WINDOW_HEIGHT
                    ),
                }
                for vecino in mapa.neighbors(nombre_nodo)
            ],
        }

    # Construir objetos Node con colores por zona para el renderizado
    atributos_nodos = dict(mapa.nodes(data=True))
    nodes = []
    for nombre_nodo, datos_pantalla in node_data.items():
        zona = atributos_nodos[nombre_nodo]["zona"]
        nodes.append(
            Node(
                nombre=nombre_nodo,
                zona=zona,
                center=datos_pantalla["node_pos"],
                neighbors=datos_pantalla["neighbors"],
                color=ZONA_COLORS[zona],
                edge_color=ZONA_EDGE_COLORS[zona],
                radius=ZONA_NODE_RADIUS[zona],
            )
        )

    return nodes, node_data


def simular_grupo(ids_vehiculos: list, cola, stop_event, proceso_id: int):
    """
    Crea un subconjunto de vehículos, los corre en hilos independientes
    y espera hasta que stop_event sea activado por el proceso principal.

    Parámetros
    ----------
    ids_vehiculos : list[int]
        Lista de IDs asignados a este proceso.
    cola : MPQueue
        Cola compartida entre todos los procesos. Los vehículos depositan
        su estado aquí y el proceso principal lo lee para visualizar.
    stop_event : MPEvent
        Bandera de parada compartida entre todos los procesos.
        Cuando se activa, todos los hilos terminan su loop ordenadamente.
    proceso_id : int
        Número de este proceso (1, 2, ...). Se incluye en cada estado
        enviado a la cola para que el visualizador asigne el color correcto.
    """
    # Cada proceso construye su propia copia del grafo
    mapa = generate_graph()
    lock_mapa = Lock()

    # Usar solo nodos del componente fuertemente conectado principal
    componente_principal = max(nx.strongly_connected_components(mapa), key=len)
    nodos_validos = list(componente_principal)

    # Crear los vehículos asignados a este proceso
    vehiculos = []
    for id_vehiculo in ids_vehiculos:
        origen = random.choice(nodos_validos)
        destino = random.choice([n for n in nodos_validos if n != origen])

        vehiculo = Vehiculo(
            id_vehiculo=id_vehiculo,
            mapa=mapa,
            origen=origen,
            destino=destino,
            velocidad=random.randint(20, 60),
            lock_mapa=lock_mapa,
            report_queue=cola,
            stop_event=stop_event,
            proceso_id=proceso_id,
        )
        vehiculos.append(vehiculo)

    # Arrancar un hilo por vehículo
    hilos = [Thread(target=v.run, daemon=True) for v in vehiculos]
    for hilo in hilos:
        hilo.start()

    # Mantener el proceso vivo hasta recibir la señal de parada
    stop_event.wait()

    # Esperar que todos los hilos terminen su iteración actual
    for hilo in hilos:
        hilo.join(timeout=2)


def start_parallel_simulation(n_vehiculos: int, cola, stop_event, num_cores: int):
    """
    Divide la carga de vehículos entre los núcleos disponibles y lanza
    un proceso por núcleo.

    La distribución es intercalada para balancear la carga uniformemente:
    con 5 vehículos y 2 núcleos:
        Proceso 1 → IDs [0, 2, 4]  (3 vehículos)
        Proceso 2 → IDs [1, 3]     (2 vehículos)

    Nunca se crean más procesos que vehículos — si hay más núcleos que
    vehículos, num_cores se limita a n_vehiculos en el llamador.

    Parámetros
    ----------
    n_vehiculos : int
        Cantidad total de vehículos a simular.
    cola : MPQueue
        Cola compartida para el reporte de estados.
    stop_event : MPEvent
        Bandera de parada compartida entre todos los procesos.
    num_cores : int
        Cantidad de procesos a lanzar (núcleos a usar).

    Retorna: Lista de procesos lanzados, necesaria para hacer join al cierre.
    """
    todos_los_ids = list(range(n_vehiculos))

    grupos = [todos_los_ids[i::num_cores] for i in range(num_cores)]

    procesos = []
    for proceso_id, grupo in enumerate(grupos, start=1):
        proceso = Process(
            target=simular_grupo,
            args=(grupo, cola, stop_event, proceso_id),
            daemon=True,
        )
        proceso.start()
        procesos.append(proceso)

    return procesos


def setup_pygame_window() -> tuple:
    """
    Inicializa pygame y crea la ventana principal de la simulación.

    Retorna
    -------
    window : pygame.Surface
        Superficie principal donde se dibuja el mapa y los vehículos.
    reloj : pygame.time.Clock
        Reloj para controlar los FPS del game loop.
    fuente : pygame.font.Font
        Fuente monoespaciada para el panel de información en pantalla.
    """
    pygame.init()
    pygame.font.init()

    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption(WINDOW_NAME)

    reloj = pygame.time.Clock()
    fuente = pygame.font.SysFont("monospace", 11, bold=True)

    return window, reloj, fuente


if __name__ == "__main__":
    num_cores = min(cpu_count(), N_VEHICULOS)
    PALETA = generar_paleta(num_cores)

    cola_reporte = MPQueue()  # canal de comunicación simulación
    stop_event = MPEvent()  # señal de parada global para todos los procesos

    nodes, node_data = initialize_map_nodes()

    procesos = start_parallel_simulation(
        N_VEHICULOS, cola_reporte, stop_event, num_cores
    )

    window, reloj, fuente = setup_pygame_window()

    estado_vehiculos = {}
    corriendo = True

    while corriendo:
        # Procesar eventos del sistema (cerrar ventana, teclas)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                corriendo = False

        # Leer hasta 50 estados de la cola por frame
        mensajes_procesados = 0
        while mensajes_procesados < 50:
            try:
                estado = cola_reporte.get_nowait()
                estado_vehiculos[estado["id"]] = estado
                mensajes_procesados += 1
            except Empty:
                break

        # Renderizar el frame
        window.fill((8, 11, 18))  # limpiar con fondo oscuro

        for nodo in nodes:
            nodo.draw_node(window)  # dibujar mapa

        renderizar_vehiculos(  # dibujar vehículos
            window, estado_vehiculos, node_data, PALETA
        )

        pygame.display.flip()  # mostrar frame
        reloj.tick(30)  # limitar a 30 FPS

    # Cierre ordenado
    stop_event.set()  # señal de parada a todos los procesos

    for proceso in procesos:
        proceso.join(timeout=3)

    pygame.quit()
