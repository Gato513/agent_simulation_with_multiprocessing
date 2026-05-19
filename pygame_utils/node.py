"""
pygame_utils/node.py
====================
Clase Node — representación visual de una intersección del mapa.

Cada instancia de Node corresponde a un nodo del grafo del Circuito
Comercial y encapsula su posición en pantalla, sus vecinos y su
configuración visual (color y radio según zona).
"""

import pygame


class Node:
    """
    Representación visual de una intersección del Circuito Comercial.

    Atributos
    ---------
    nombre    : Nombre completo de la intersección (ej: "Av. Moisés Bertoni").
    zona      : Tipo de zona: 'comercial', 'secundaria', 'peatonal' o 'residencial'.
    center    : Posición del nodo en píxeles en la ventana pygame.
    radius    : Radio del círculo que representa al nodo en pantalla.
    color     : Color del nodo en formato hex (#RRGGBB), determinado por zona.
    edge_color: Color de las aristas hacia los vecinos, en tono más oscuro que color.
    neighbors : Lista de vecinos con formato [{"id": nombre, "pos": (px, py)}, ...].
    """

    def __init__(
        self,
        nombre: str,
        zona: str,
        center: tuple,
        neighbors: list,
        color: str,
        edge_color: str,
        radius: int = 5,
    ):
        """
        nombre      : Nombre de la intersección tal como aparece en graph_config_osm.py.
        zona        : Zona del mapa a la que pertenece: 'comercial', 'secundaria', 'peatonal' o 'residencial'.
        center      : Posición en píxeles calculada por normalized_to_screen().
        neighbors   : Lista de nodos vecinos con sus posiciones de pantalla.
        color       : Color del círculo del nodo (hex). Viene de ZONA_COLORS.
        edge_color  : Color de las líneas hacia los vecinos (hex). Viene de ZONA_EDGE_COLORS.
        radius      : Radio del círculo en píxeles. Viene de ZONA_NODE_RADIUS. Por defecto: 5.
        """
        self.nombre = nombre
        self.zona = zona
        self.center = center
        self.radius = radius
        self.color = color
        self.edge_color = edge_color
        self.neighbors = neighbors

    def draw_node(self, window: pygame.Surface):
        """
        Dibuja el nodo y sus aristas hacia los vecinos en la ventana pygame.

        Parámetros
        ----------
        window: Superficie de pygame donde se dibuja.
        """
        # Dibujar aristas primero para que queden debajo del nodo
        for vecino in self.neighbors:
            pygame.draw.line(
                window,
                self.edge_color,
                self.center,
                vecino["pos"],
                2,  # grosor de 2px para mayor visibilidad
            )

        # Dibujar el círculo del nodo encima de las aristas
        pygame.draw.circle(
            surface=window,
            color=self.color,
            center=self.center,
            radius=self.radius,
        )

    def contiene_punto(self, x: int, y: int) -> bool:
        """
        Determina si un punto (x, y) está dentro del área del nodo.

        Parámetros
        ----------
        x : Coordenada X del punto a verificar.
        y : Coordenada Y del punto a verificar.

        Retorna: True si el punto está dentro o sobre el borde del nodo.
        """
        distancia_cuadrada = (x - self.center[0]) ** 2 + (y - self.center[1]) ** 2
        return distancia_cuadrada <= self.radius**2
