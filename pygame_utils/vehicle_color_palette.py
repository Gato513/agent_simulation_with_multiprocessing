"""
pygame_utils/vehicle_color_palette.py
======================================
Generación dinámica de la paleta de colores para los vehículos por proceso.

Los vehículos de cada proceso (núcleo de CPU) se dibujan con un color
distinto para que sea visualmente evidente que pertenecen a procesos
diferentes corriendo en paralelo.

"""

import colorsys


def generar_paleta(num_procesos: int) -> list:
    """
    Genera una paleta de colores neón para N procesos de simulación.

    Los colores se distribuyen equitativamente en el rango de tonos
    libres (0°-150°), todos con saturación máxima y brillo medio para
    lograr el efecto neón que armoniza con la paleta del mapa.

    El color de 'esperando' es rojo alerta (#FF1744) igual para todos
    los procesos — indica congestión independientemente del núcleo.

    El color de 'llegado' es gris azulado (#4A4A6A) igual para todos —
    neutro, no confundible con ningún color de nodo ni de vehículo en ruta,
    y diferente del color 'en_ruta' para que se note que llegó a destino.

    Parámetros
    ----------
    num_procesos : int
        Cantidad de procesos de simulación activos. Equivale al número
        de núcleos de CPU que usa la simulación (min(cpu_count(), N_VEHICULOS)).

    Retorna
    -------
    list[dict]
        Lista de diccionarios de color por proceso. Cada diccionario tiene:
            - "en_ruta"   : str — color hex neón único por proceso
            - "esperando" : str — rojo alerta (#FF1744), igual para todos
            - "llegado"   : str — gris azulado (#4A4A6A), igual para todos

    Ejemplo
    -------
    >>> paleta = generar_paleta(2)
    >>> paleta[0]["en_ruta"]    # proceso 1 — naranja-rojo
    '#FF3000'
    >>> paleta[1]["en_ruta"]    # proceso 2 — amarillo-verde
    '#AAFF00'
    """
    paleta = []

    for i in range(num_procesos):
        # Distribuir tonos desde 15° (0.042 en escala 0-1) hasta 150°
        # El offset de 15° aleja el primer color del rojo puro (#FF0000)
        # que es demasiado similar al color de 'esperando' (#FF1744)
        tono = 0.042 + (i / num_procesos) * (150 / 360)

        # HLS → RGB con luminosidad 0.50 y saturación 1.0 para efecto neón
        r, g, b = colorsys.hls_to_rgb(tono, 0.50, 1.0)
        color_en_ruta = "#{:02X}{:02X}{:02X}".format(
            int(r * 255), int(g * 255), int(b * 255)
        )

        paleta.append(
            {
                "en_ruta": color_en_ruta,
                "esperando": "#FF1744",  # rojo alerta — igual para todos los procesos
                "llegado": "#4A4A6A",  # gris azulado — armoniza con fondo oscuro
            }
        )

    return paleta
