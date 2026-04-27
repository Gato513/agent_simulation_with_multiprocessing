import networkx as nx
import random
import time
from threading import Lock, Event
from queue import Queue


class Vehiculo:
    def __init__(
            self,
            id_vehiculo : int,
            mapa        : nx.DiGraph,
            origen      : str,
            destino     : str,
            velocidad   : int,
            lock_mapa   : Lock,
            report_queue: Queue,
            stop_event  : Event
        ):

        self.id_vehiculo    = id_vehiculo
        self.report_queue   = report_queue
        self.lock_mapa      = lock_mapa
        self.mapa           = mapa
        self.nodo_actual    = origen
        self.indice_ruta    = 0
        self.destino        = destino
        self.ruta           = self._calcular_ruta()
        self.velocidad      = velocidad
        self.estado         = "en_ruta"
        self.stop_event     = stop_event


        while not self.mapa.nodes[self.nodo_actual]["semaforo"].acquire(blocking=False):
            self.nodo_actual = random.choice(list(self.mapa.nodes))
            self.ruta        = self._calcular_ruta()

        self.mapa.nodes[self.nodo_actual]["vp"] += 1

    def _calcular_ruta(self):
        return nx.shortest_path(self.mapa, self.nodo_actual, self.destino, weight="weight")

    def send_state(self):
        self.report_queue.put({
            "id"         : self.id_vehiculo,
            "nodo_actual": self.nodo_actual,
            "destino"    : self.destino,
            "estado"     : self.estado,
            "velocidad"  : self.velocidad,
        })

    def llego(self):
        return self.indice_ruta >= len(self.ruta) - 1

    def avanzar(self):
        if self.llego():
            return

        siguiente     = self.ruta[self.indice_ruta + 1]
        sem_siguiente = self.mapa.nodes[siguiente]["semaforo"]
        sem_actual    = self.mapa.nodes[self.nodo_actual]["semaforo"]


        while not sem_siguiente.acquire(blocking=False):
            if self.stop_event.is_set():
                return
            self.estado = "esperando"
            self.send_state()
            time.sleep(0.5)


        self.estado      = "en_ruta"
        self.indice_ruta += 1
        nodo_anterior     = self.nodo_actual
        self.nodo_actual  = siguiente

        with self.lock_mapa:
            self.mapa.nodes[siguiente]["vp"]    += 1
            self.mapa.nodes[nodo_anterior]["vp"] -= 1
        sem_actual.release()

        if self.llego():
            self.estado = "llegado"

    def elegir_nuevo_destino(self):
        nodos = list(self.mapa.nodes)
        nodos.remove(self.nodo_actual)
        self.destino     = random.choice(nodos)
        self.ruta        = self._calcular_ruta()
        self.indice_ruta = 0
        self.estado      = "en_ruta"

    def run(self):
        while not self.stop_event.is_set():
            if self.llego():
                self.elegir_nuevo_destino()
            else:
                self.avanzar()
            self.send_state()

            time.sleep(30 / self.velocidad)
