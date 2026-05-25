"""
graph_model.py
==============
Construcción del grafo del Circuito Comercial de Encarnación.

Responsable de:
    - Construir el grafo dirigido (DiGraph) a partir de los datos del mapa OSM.
    - Inicializar los semáforos de capacidad en cada intersección.

Cada proceso de simulación llama a generate_graph() de forma independiente
para obtener su propia copia del grafo — los procesos no comparten memoria.
"""

from threading import Semaphore
import networkx as nx
from graph_config_osm import connections, nodes


def agregar_conexiones(mapa: nx.DiGraph, conexiones: list):
    """
    Agrega las aristas al grafo respetando la direccionalidad real de OSM.

    Para cada conexión:
        - Siempre agrega la arista en la dirección definida (A→B).
        - Solo agrega la dirección inversa (B→A) si oneway=False.

    Parámetros
    ----------
    mapa : nx.DiGraph
        Grafo dirigido al que se agregan las aristas.
    conexiones : list
        Lista de conexiones con formato [origen, destino, atributos].
        Los atributos incluyen: weight (metros), vel_max, carriles,
        vehi_calle y oneway (bool).
    """
    for origen, destino, atributos in conexiones:
        mapa.add_edge(origen, destino, **atributos)

        # Solo agregar la dirección inversa si la calle es de doble sentido
        if not atributos.get("oneway", False):
            mapa.add_edge(destino, origen, **atributos)


def generate_graph() -> nx.DiGraph:
    """
    Construye y retorna el grafo completo del Circuito Comercial.

    El grafo se construye en tres pasos:
        1. Se agregan todos los nodos con sus atributos (pos, zona, vp, capacidad).
        2. Se agregan las aristas respetando la direccionalidad real de OSM:
            oneway=True  → una sola arista A→B
            oneway=False → dos aristas A→B y B→A
        3. Se inicializa un Semaphore(capacidad) en cada nodo para controlar
            la cantidad máxima de vehículos simultáneos en cada intersección.

    Los Semaphores son objetos de threading — no son serializables entre procesos.
    Por eso cada proceso llama a generate_graph() por separado en lugar de
    recibir el grafo como parámetro.

    Retorna
    -------
    nx.DiGraph
        Grafo dirigido listo para ser usado por la simulación.
        Cada nodo tiene los atributos: pos, zona, vp, capacidad, semaforo.
        Cada arista tiene los atributos: weight, vel_max, carriles,
        vehi_calle, oneway.
    """
    mapa = nx.DiGraph()

    # Agregar intersecciones con sus atributos geográficos y de configuración
    mapa.add_nodes_from(nodes)

    # Agregar calles respetando la direccionalidad real de OSM
    agregar_conexiones(mapa, connections)

    # Inicializar semáforo de capacidad en cada intersección
    for _, atributos_nodo in mapa.nodes(data=True):
        atributos_nodo["semaforo"] = Semaphore(atributos_nodo["capacidad"])

    return mapa