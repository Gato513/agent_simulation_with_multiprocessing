"""
pygame_utils/
=============
Paquete de utilidades de visualización para el simulador.

Módulos
-------
constants.py
    Constantes globales de configuración visual: dimensiones de ventana,
    colores por zona y radios de nodos.

coordinate_transform.py
    Transformación de coordenadas normalizadas [-1, 1] del grafo OSM
    a coordenadas de pantalla en píxeles para pygame.

node.py
    Clase Node — representación visual de una intersección del mapa.
    Encapsula el dibujo del nodo y sus aristas hacia los vecinos.

vehicle_color_palette.py
    Generación dinámica de la paleta de colores neón para los vehículos,
    diferenciada por proceso de simulación (núcleo de CPU).
"""
