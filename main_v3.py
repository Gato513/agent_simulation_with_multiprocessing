from threading import Thread, Lock, Event
from queue import Queue, Empty
import random
import pygame
from pygame_utils.coordinate_transform import normalized_to_screen
from graph_model import generate_graph, show_data
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

N_VEHICULOS = 30

def head_state_vehiculo():
    print("\n" + " SIMULADOR DE TRÁFICO — ENCARNACIÓN ".center(110, "="))
    print(f"{'ID':<5} {'Velocidad':<12} {'Estado':<12} {'Nodo Actual':<65} {'Nodo Destino':<35} ")
    print("-" * 110)

def show_state_vehiculo(estado):
    VERDE = "\033[32m"
    ROJO  = "\033[31m"
    RESET = "\033[0m"
    color = VERDE if estado["estado"] == "en_ruta" else ROJO
    print(
        f"{estado['id']:<5} "
        f"{estado['velocidad']:<12} "
        f"{color}{estado['estado']:<12}{RESET}"
        f"{estado['nodo_actual']:<65} "
        f"{estado['destino']} "
    )

def render(window, estado_vehiculos, node_data):
    COLOR = {
        "llegado"   : "#FF0000",
        "esperando" : "#FFFF00",
        "en_ruta"   : "#0F9400",
    }
    
    for _, estado in estado_vehiculos.items():
        nodo_actual = estado["nodo_actual"]

        if nodo_actual in node_data:
            vehiculo_position = node_data[estado['nodo_actual']]["node_pos"]

            pygame.draw.circle(
                surface=window, 
                color= COLOR[estado["estado"]],
                center=vehiculo_position, 
                radius=5
            )

if __name__ == "__main__":

    mapa = generate_graph()
    lock_mapa    = Lock()
    report_queue = Queue()
    stop_event   = Event()
    nodos    = list(mapa.nodes)

    # Creacion de los nodos del Mapa en Pygame:
    node_data = {}
    for n, data in mapa.nodes(data=True):

        node_pos = normalized_to_screen(
            pos=data["pos"],
            width=WINDOW_WIDTH,
            height=WINDOW_HEIGHT
        )

        node_data[n] = {
            "node_pos": node_pos,
            "neighbors": [
                {
                    "id": neighbor,
                    "pos": normalized_to_screen(
                        pos=mapa.nodes[neighbor]["pos"],
                        width=WINDOW_WIDTH,
                        height=WINDOW_HEIGHT
                    )
                }
                for neighbor in mapa.neighbors(n)
            ]
        }

    node_attrs = dict(mapa.nodes(data=True))
    nodes = []
    for n, data in node_data.items():
        NODE_POS  = data["node_pos"]
        NEIGHBORS = data["neighbors"]
        ZONA = node_attrs[n]["zona"]

        NODE_COLOR  = ZONA_COLORS[ZONA]
        EDGE_COLORS = ZONA_EDGE_COLORS[ZONA]
        NODE_RADIUS = ZONA_NODE_RADIUS[ZONA]
    
        n = Node(
            nombre     = n,
            zona       = ZONA,
            center     = NODE_POS,
            neighbors  = NEIGHBORS,
            color      = NODE_COLOR,
            edge_color = EDGE_COLORS,
            radius     = NODE_RADIUS,
        )
    
        nodes.append(n)

    # Creacion de los vehiculos:
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

    # Inicializacion de los hilos:
    threads = []
    for v in vehiculos:
        t = Thread(target=v.run, daemon=True)
        t.start()
        threads.append(t)

    # Inicializacion y configuracion de Pygame:
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption(WINDOW_NAME)
    reloj = pygame.time.Clock()
    pygame.font.init()
    fuente = pygame.font.SysFont(name="monospace", size=11, bold=True)


    head_state_vehiculo()
    estado_vehiculos = {}
    run = True
    while run:
        # Control de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                run = False

        # Receccion de datos de los hilos
        procesados = 0
        while not report_queue.empty() and procesados < 50:
            try:
                e = report_queue.get_nowait()
                estado_vehiculos[e["id"]] = e
                show_state_vehiculo(e)
                procesados += 1
            except Empty:
                break

        # Renderizado de la simulacion:
        window.fill((10, 10, 20))

        for nodo in nodes:
            nodo.draw_node(window)

        # Mostrar Frame
        # Renderizado posicion de veiculos
        render(
            estado_vehiculos = estado_vehiculos, 
            node_data        = node_data,
            window           = window
        )

        pygame.display.flip()

        # 5. Control de FPS:
        reloj.tick(30)

    pygame.quit()

    stop_event.set()
    for t in threads:
        t.join(timeout=2)
        
    # show_data(mapa) # Mucha informacion inecesaria.

