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
        f"{estado['nodo_actual']:<35}"
    )


def render_vehiculos(window, estado_vehiculos, node_data, paleta):
    for estado in estado_vehiculos.values():
        nodo = estado["nodo_actual"]
        if nodo in node_data:
            pid = estado.get("proceso_id", 1)
            color = paleta[(pid - 1) % len(paleta)][estado["estado"]]
            pos = node_data[nodo]["node_pos"]
            pygame.draw.circle(window, color, pos, 5)


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

    threads = [Thread(target=v.run, daemon=True) for v in vehiculos]
    for t in threads:
        t.start()

    stop_event.wait()
    for t in threads:
        t.join(timeout=2)


def start_parallel_simulation(n_vehiculos, queue, stop_event, num_cores):
    """
    Divide los vehículos en num_cores grupos y lanza un proceso por grupo.
    Ejemplo con 5 vehículos y 2 núcleos:
        Proceso 1 → IDs [0, 2, 4]
        Proceso 2 → IDs [1, 3]
    """
    ids = list(range(n_vehiculos))
    grupos = [ids[i::num_cores] for i in range(num_cores)]

    procesos = []
    for proceso_id, grupo in enumerate(grupos, start=1):
        p = Process(
            target=simular_grupo,
            args=(grupo, queue, stop_event, proceso_id),
            daemon=True,
        )
        p.start()
        procesos.append(p)

    return procesos


def initialize_map_nodes():
    mapa = generate_graph()

    node_data = {}
    for n, data in mapa.nodes(data=True):
        node_pos = normalized_to_screen(data["pos"], WINDOW_WIDTH, WINDOW_HEIGHT)
        node_data[n] = {
            "node_pos": node_pos,
            "neighbors": [
                {
                    "id": neighbor,
                    "pos": normalized_to_screen(
                        mapa.nodes[neighbor]["pos"], WINDOW_WIDTH, WINDOW_HEIGHT
                    ),
                }
                for neighbor in mapa.neighbors(n)
            ],
        }

    node_attrs = dict(mapa.nodes(data=True))
    nodes = []
    for n, data in node_data.items():
        zona = node_attrs[n]["zona"]
        nodes.append(
            Node(
                nombre=n,
                zona=zona,
                center=data["node_pos"],
                neighbors=data["neighbors"],
                color=ZONA_COLORS[zona],
                edge_color=ZONA_EDGE_COLORS[zona],
                radius=ZONA_NODE_RADIUS[zona],
            )
        )

    return nodes, node_data


def setup_pygame_window():
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

    report_queue = MPQueue()
    stop_event = MPEvent()

    nodes, node_data = initialize_map_nodes()
    procesos = start_parallel_simulation(
        N_VEHICULOS, report_queue, stop_event, num_cores
    )
    window, reloj, fuente = setup_pygame_window()

    estado_vehiculos = {}
    run = True

    while run:
        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                run = False

        # Leer estados de los vehículos desde la queue
        procesados = 0
        while procesados < 50:
            try:
                e = report_queue.get_nowait()
                estado_vehiculos[e["id"]] = e
                procesados += 1
            except Empty:
                break

        # Dibujar
        window.fill((8, 11, 18))
        for nodo in nodes:
            nodo.draw_node(window)
        render_vehiculos(window, estado_vehiculos, node_data, PALETA)
        pygame.display.flip()
        reloj.tick(30)

    # Cierre ordenado
    stop_event.set()
    for p in procesos:
        p.join(timeout=3)
    pygame.quit()
