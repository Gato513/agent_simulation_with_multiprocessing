import colorsys


def generar_paleta(num_procesos: int) -> list:
    """
    Genera colores neón en el rango de tonos libre (0°-150°)
    """
    paleta = []
    for i in range(num_procesos):
        hue = 0.042 + (i / num_procesos) * (150 / 360)
        r, g, b = colorsys.hls_to_rgb(hue, 0.50, 1.0)
        color = "#{:02X}{:02X}{:02X}".format(int(r * 255), int(g * 255), int(b * 255))
        paleta.append(
            {
                "en_ruta": color,
                "esperando": "#FF1744",
                "llegado": "#4A4A6A",
            }
        )
    return paleta
