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
    Agrega todas las aristas al grafo.

    Parámetros
    ----------
    mapa : nx.DiGraph
        Grafo dirigido al que se agregan las aristas.
    conexiones : list
        Lista de conexiones con formato [origen, destino, atributos].
        Los atributos incluyen: weight (metros), vel_max, carriles, vehi_calle.
    """
    for origen, destino, atributos in conexiones:
        mapa.add_edge(origen, destino, **atributos)
        mapa.add_edge(destino, origen, **atributos)


def generate_graph() -> nx.DiGraph:
    """
    Construye y retorna el grafo completo del Circuito Comercial.

    El grafo se construye en tres pasos:
        1.  Se agregan todos los nodos con sus atributos (pos, zona, vp, capacidad).
        2.  Se agregan todas las aristas con sus atributos (weight, vel_max, carriles).
        3.  Se inicializa un Semaphore(capacidad) en cada nodo para controlar
            la cantidad máxima de vehículos simultáneos en cada intersección.

    Los Semaphores son objetos de threading — no son serializables entre procesos.
    Por eso cada proceso llama a generate_graph() por separado en lugar de
    recibir el grafo como parámetro.

    Retorna
    -------
    nx.DiGraph
        Grafo dirigido listo para ser usado por la simulación.
        Cada nodo tiene los atributos: pos, zona, vp, capacidad, semaforo.
        Cada arista tiene los atributos: weight, vel_max, carriles, vehi_calle.
    """
    mapa = nx.DiGraph()

    # Agregar intersecciones con sus atributos geográficos y de configuración
    mapa.add_nodes_from(nodes)

    # Agregar calles como aristas con sus atributos
    agregar_conexiones(mapa, connections)

    # Inicializar semáforo de capacidad en cada intersección.
    for _, atributos_nodo in mapa.nodes(data=True):
        atributos_nodo["semaforo"] = Semaphore(atributos_nodo["capacidad"])

    return mapa
