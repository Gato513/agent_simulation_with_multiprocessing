import pygame

class Node:
    def __init__(
        self,
        nombre: str,
        center: tuple[int, int],
        neighbors: list[dict],
        color: str,
        edge_color: str,
        zona: str,
        radius: int = 10,
    ):
        self.nombre = nombre
        self.zona = zona
        self.center = center
        self.radius = radius
        self.color = color
        self.edge_color = edge_color
        self.neighbors = neighbors

    def draw_node(self, window: pygame.Surface):
        pygame.draw.circle(
            surface=window, color=self.color, center=self.center, radius=self.radius
        )

        for neighbor in self.neighbors:
            pygame.draw.line(
                surface=window,
                color=self.edge_color,
                start_pos=self.center,
                end_pos=neighbor["pos"],
                width=2,
            )

    def contiene_punto(self, x: int, y: int) -> bool:
        dx = x - self.center[0]
        dy = y - self.center[1]
        return (dx**2 + dy**2) <= self.radius**2
