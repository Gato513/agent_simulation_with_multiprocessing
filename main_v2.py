from graph_model import generate_graph, show_data
from vehiculos import Vehiculo
from threading import Thread, Lock, Event
from queue import Queue, Empty
import random
import time

DURACION_SIMULACION = 30

# N_VEHICULOS no debe superar la capacidad total del grafo, para ver congestión: usar un número cercano al límite.
N_VEHICULOS = 6


def render(estado):
    """
    Renderiza el estado de un vehículo.
    Semana 3: reemplazar el contenido de esta función por llamadas a pygame.
    La firma (recibe un dict con id, nodo_actual, destino, estado, velocidad)
    no cambia — solo cambia lo que hace adentro.
    """
    VERDE = "\033[32m"
    ROJO  = "\033[31m"
    RESET = "\033[0m"
    color = VERDE if estado["estado"] == "en_ruta" else ROJO
    print(
        f"{estado['id']:<5} "
        f"{estado['velocidad']:<12} "
        f"{color}{estado['estado']:<12}{RESET}"
        f"{estado['nodo_actual']:<65} "
        f"{estado['destino']:<35} "
    )


if __name__ == "__main__":
    mapa         = generate_graph()
    lock_mapa    = Lock()
    report_queue = Queue()
    stop_event   = Event()

    nodos    = list(mapa.nodes)
    vehiculos = []
    for i in range(N_VEHICULOS):
        origen  = random.choice(nodos)
        destino = random.choice([n for n in nodos if n != origen])
        v = Vehiculo(
            id_vehiculo  = i,
            mapa         = mapa,
            origen       = origen,
            destino      = destino,
            velocidad    = random.randint(20, 60),
            lock_mapa    = lock_mapa,
            report_queue = report_queue,
            stop_event   = stop_event,
        )
        vehiculos.append(v)

    threads = []
    for v in vehiculos:
        t = Thread(target=v.run, daemon=True)
        t.start()
        threads.append(t)

    print("\n" + " SIMULADOR DE TRÁFICO — ENCARNACIÓN ".center(110, "="))
    print(f"{'ID':<5} {'Velocidad':<12} {'Estado':<12} {'Nodo Actual':<35} {'Nodo Destino':<35} ")
    print("-" * 110)

    fin = time.time() + DURACION_SIMULACION
    while time.time() < fin:
        procesados = 0
        while not report_queue.empty() and procesados < 50:
            try:
                estado = report_queue.get_nowait()
                render(estado)
                procesados += 1
            except Empty:
                break
        time.sleep(0.05)

    stop_event.set()
    for t in threads:
        t.join(timeout=2)

    show_data(mapa)
