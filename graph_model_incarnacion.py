from graph_config import connections, nodes
from threading import Semaphore
import networkx as nx


def connect_nodes(mapa, connections):
    for origen, destino, atributos in connections:
        mapa.add_edge(origen, destino, **atributos)
        mapa.add_edge(destino, origen, **atributos)


def generate_graph():
    mapa = nx.DiGraph()
    mapa.add_nodes_from(nodes)
    connect_nodes(mapa, connections)

    for _, datos in mapa.nodes(data=True):
        datos["semaforo"] = Semaphore(datos["capacidad"])

    return mapa


def show_data(mapa):
    print("\n" + " TODOS LOS NODOS ".center(80, "="))
    print(f"{'Nodo':<40} {'Semáforo':<10} {'Zona':<15} {'Vehículos':<10}")
    print("-" * 80)

    for n, data in mapa.nodes(data=True):
        print(
            f"{n:<40} "
            f"{str(data.get('tiene_semaforo')):<10} "
            f"{data.get('zona', ''):<15} "
            f"{data.get('vehi_presentes', 0):<10}"
        )

    print("\n" + " ARISTAS ".center(100, "="))
    print(f"{'Origen':<35} {'Destino':<35} {'Vel Max':<10} {'Carriles':<10} {'Vehículos':<10}")
    print("-" * 100)

    for u, v, data in mapa.edges(data=True):
        print(
            f"{u:<35} "
            f"{v:<35} "
            f"{data.get('vel_max', 0):<10} "
            f"{data.get('carriles', 0):<10} "
            f"{data.get('vehi_calle', 0):<10}"
        )
