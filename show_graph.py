import matplotlib.pyplot as plt
import networkx as nx
from graph_model_incarnacion import generate_graph
from graph_config import  node_position

def display_attributes(map_graph, node_position):
    top_labels  = {"Av. Costanera", "Mcal. Estigarribia y Pereira", "Mcal. Estigarribia y Caballero"}
    offset_up   = 0.45
    offset_down = 0.45

    pos_node_attributes = {
        n: (x, y + offset_up) if n in top_labels else (x, y - offset_down)
        for n, (x, y) in node_position.items()
    }

    node_labels = {n:(f"VP: {d['vehi_presentes']} | TSF: {d['tiene_semaforo']}") for n, d in map_graph.nodes(data=True)}
    edge_labels = {(u, v) : d["vehi_calle"] for u, v, d in map_graph.edges(data=True)}

    nx.draw_networkx_labels(
        map_graph,
        pos         = pos_node_attributes,
        labels      = node_labels,
        font_color  = "black",
        font_size   = 9,
        font_family = "DejaVu Sans",
        font_weight = "bold",
    )

    nx.draw_networkx_edge_labels(
        map_graph,
        pos = node_position,
        edge_labels = edge_labels,
        label_pos = 0.5,
        
    )

def graph_visualization(map_graph, node_position):
    nx.draw(
        map_graph,
        pos         = node_position,
        node_color  = "blue",
        node_size   = 2500,
        with_labels = True,
        font_color  = "white",
        font_size   = 6,
        arrows      = True,
        font_weight = "bold"
    )

    display_attributes(map_graph, node_position)

    plt.margins(0.2)
    plt.show()

map_graph = generate_graph()

graph_visualization(map_graph = map_graph, node_position = node_position)