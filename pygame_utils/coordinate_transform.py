"""
pygame_utils/coordinate_transform.py
=====================================
Transformaciones de coordenadas entre el espacio del grafo y la pantalla.

El grafo OSM almacena las posiciones de los nodos normalizadas en el
rango [-1, 1] para ambos ejes. Para dibujar en pygame necesitamos
convertirlas a píxeles dentro del área visible de la ventana.
"""


def normalized_to_screen(
    pos: tuple, width: int, height: int, padding: int = 50
) -> tuple[int, int]:
    """
    Convierte una posición normalizada [-1, 1] a coordenadas de pantalla
    en píxeles, respetando el padding y la inversión del eje Y.

    Parámetros
    ----------
    pos     : Posición normalizada (x, y) en el rango [-1.0, 1.0], proviene del campo 'pos' de cada nodo.
    width   : Ancho de la ventana pygame en píxeles (WINDOW_WIDTH).
    height  : Alto de la ventana pygame en píxeles (WINDOW_HEIGHT).
    padding : Margen en píxeles alrededor del área de dibujo. Por defecto: 50px.

    Retorna: Coordenadas (px, py) en píxeles listas para usar en pygame.draw.
    """
    x, y = pos

    x_normalizado = (x + 1) / 2
    y_normalizado = (y + 1) / 2

    area_ancho = width - 2 * padding
    area_alto = height - 2 * padding

    px = padding + x_normalizado * area_ancho

    py = padding + (1 - y_normalizado) * area_alto

    return int(px), int(py)
