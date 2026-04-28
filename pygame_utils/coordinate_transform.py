def normalized_to_screen(pos: tuple, width: int, height: int, padding: int = 50):
    x, y = pos

    # Normalizar de [-1,1] → [0,1]
    x_norm = (x + 1) / 2
    y_norm = (y + 1) / 2

    # Escalar a ventana con padding
    px = padding + x_norm * (width - 2 * padding)

    # IMPORTANTE: invertir eje Y
    py = padding + (1 - y_norm) * (height - 2 * padding)

    return int(px), int(py)