from threading import Thread
from threading import Lock

from multiprocessing import Process
from multiprocessing import Queue as MPQueue
from multiprocessing import Event as MPEvent
from multiprocessing import cpu_count

from queue import Empty

import networkx as nx
import random
import pygame
from pygame_utils.coordinate_transform import normalized_to_screen
from graph_model import generate_graph
from pygame_utils.vehicle_color_palette import generar_paleta
from vehiculos import Vehiculo
from pygame_utils.node import Node

from pygame_utils.constants import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    WINDOW_NAME,
    ZONA_COLORS,
    ZONA_EDGE_COLORS,
    ZONA_NODE_RADIUS,
)

N_VEHICULOS = 5


def head_state_vehiculo():
    print("\n" + " SIMULADOR DE TRÁFICO — ENCARNACIÓN ".center(110, "="))
    print(f"{'ID':<5} {'Velocidad':<12} {'Estado':<11} {'Nodo Actual':<35}")
    print("-" * 110)


def show_state_vehiculo(estado):
    VERDE = "\033[32m"
    ROJO = "\033[31m"
    RESET = "\033[0m"
    color = VERDE if estado["estado"] == "en_ruta" else ROJO
    print(
        f"{estado['id']:<5} "
        f"{estado['velocidad']:<12} "
        f"{color}{estado['estado']:<12}{RESET}"
        f"{estado['nodo_actual']:<35} "
    )


def vehicle_rendering(window, estado_vehiculos, node_data):
    num_cores = min(cpu_count(), N_VEHICULOS)
    PALETA = generar_paleta(num_cores)

    for _, estado in estado_vehiculos.items():
        nodo_actual = estado["nodo_actual"]
        if nodo_actual in node_data:
            pid = estado.get("proceso_id", 1)
            color = PALETA[(pid - 1) % len(PALETA)][estado["estado"]]
            pos = node_data[nodo_actual]["node_pos"]
            pygame.draw.circle(window, color, pos, 5)


def initialize_pygame_nodes():
    mapa = generate_graph()

    # Creacion de los nodos del Mapa en Pygame:
    node_data = {}
    for n, data in mapa.nodes(data=True):
        node_pos = normalized_to_screen(
            pos=data["pos"], width=WINDOW_WIDTH, height=WINDOW_HEIGHT
        )

        node_data[n] = {
            "node_pos": node_pos,
            "neighbors": [
                {
                    "id": neighbor,
                    "pos": normalized_to_screen(
                        pos=mapa.nodes[neighbor]["pos"],
                        width=WINDOW_WIDTH,
                        height=WINDOW_HEIGHT,
                    ),
                }
                for neighbor in mapa.neighbors(n)
            ],
        }

    node_attrs = dict(mapa.nodes(data=True))
    nodes = []
    for n, data in node_data.items():
        NODE_POS = data["node_pos"]
        NEIGHBORS = data["neighbors"]
        ZONA = node_attrs[n]["zona"]

        NODE_COLOR = ZONA_COLORS[ZONA]
        EDGE_COLORS = ZONA_EDGE_COLORS[ZONA]
        NODE_RADIUS = ZONA_NODE_RADIUS[ZONA]

        n = Node(
            nombre=n,
            zona=ZONA,
            center=NODE_POS,
            neighbors=NEIGHBORS,
            color=NODE_COLOR,
            edge_color=EDGE_COLORS,
            radius=NODE_RADIUS,
        )

        nodes.append(n)

    return nodes, node_data


def simular_grupo(ids_vehiculos, cola, stop_event, proceso_id):
    mapa = generate_graph()
    lock_mapa = Lock()

    scc = max(nx.strongly_connected_components(mapa), key=len)
    nodos = list(scc)

    vehiculos = []
    for i in ids_vehiculos:
        origen = random.choice(nodos)
        destino = random.choice([n for n in nodos if n != origen])
        v = Vehiculo(
            id_vehiculo=i,
            mapa=mapa,
            origen=origen,
            destino=destino,
            velocidad=random.randint(20, 60),
            lock_mapa=lock_mapa,
            report_queue=cola,
            stop_event=stop_event,
            proceso_id=proceso_id,
        )
        vehiculos.append(v)

    threads = []
    for v in vehiculos:
        t = Thread(target=v.run, daemon=True)
        t.start()
        threads.append(t)

    stop_event.wait()
    for t in threads:
        t.join(timeout=2)


def start_parallel_simulation(n_vehiculos, queue, stop_event):
    """
    Divide la carga de vehículos proporcionalmente entre los núcleos
    disponibles. Nunca crea más procesos que vehículos.
    """
    num_cores = min(cpu_count(), n_vehiculos)
    ids = list(range(n_vehiculos))  # [0, 1, 2, 3, 4]

    # Dividir la lista de IDs en num_cores grupos proporcionales donde con CPU: 2 y Vhs: 5 los grupos son [[0, 2, 4], [1, 3]]
    grupos = [ids[i::num_cores] for i in range(num_cores)]

    procesos = []
    # P1 = (1, [0, 2, 4]) y P2 = (2, [1, 3])
    for proceso_id, grupo in enumerate(grupos, start=1):
        p = Process(
            target=simular_grupo,
            args=(grupo, queue, stop_event, proceso_id),
            daemon=True,
        )
        p.start()
        procesos.append(p)

    return procesos


def setup_pygame_window():
    # Inicializacion y configuracion de Pygame:
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption(WINDOW_NAME)
    reloj = pygame.time.Clock()
    pygame.font.init()
    fuente = pygame.font.SysFont(name="monospace", size=11, bold=True)

    return window, reloj, fuente


if __name__ == "__main__":
    report_queue = MPQueue()
    stop_event = MPEvent()
    nodes, node_data = initialize_pygame_nodes()
    procesos = start_parallel_simulation(N_VEHICULOS, report_queue, stop_event)
    window, reloj, fuente = setup_pygame_window()

    estado_vehiculos = {}
    run = True
    while run:
        # Control de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                run = False

        # Recoleccion de los estados de los Vehiculos:
        procesados = 0
        while procesados < 50:
            try:
                e = report_queue.get_nowait()
                estado_vehiculos[e["id"]] = e
                procesados += 1
            except Empty:
                break

        # Renderizado de la fondo de pygame:
        window.fill((8, 11, 18))

        for nodo in nodes:
            nodo.draw_node(window)

        # Renderizado posicion de veiculos
        vehicle_rendering(
            estado_vehiculos=estado_vehiculos, node_data=node_data, window=window
        )

        pygame.display.flip()
        reloj.tick(30)

    stop_event.set()
    for p in procesos:
        p.join(timeout=3)
    pygame.quit()
