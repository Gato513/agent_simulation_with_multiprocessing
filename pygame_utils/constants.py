# Configuracion de Ventana
# En main_v3.py — ventana más grande
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 720
WINDOW_NAME = "Simulacion"

# Configuracion de Nodos:
NODE_RADIUS = 5

# ══════════════════════════════════════════════════════════════════════════
#  PALETA
# ══════════════════════════════════════════════════════════════════════════


DARK_BG = "#080B12"
TEXT_CLR = "#E8EAF0"
ACCENT = "#00d4ff"
MUTED = "#4a5068"


ZONA_COLORS = {
    "comercial": "#FF3CAC",
    "secundaria": "#784BA0",
    "peatonal": "#2B86C5",
    "residencial": "#00F5D4",
}
# constants.py — aristas más visibles y radios más diferenciados
ZONA_EDGE_COLORS = {
    "comercial": "#9B2D6A",  # más claro que antes
    "secundaria": "#5D3490",  # más claro
    "peatonal": "#1E3A5F",  # más claro
    "residencial": "#006B66",  # más claro
}

ZONA_NODE_RADIUS = {
    "comercial": 8,  # más grande — son los nodos principales
    "secundaria": 6,
    "peatonal": 5,
    "residencial": 4,  # más pequeño — hay 91, dominan el mapa
}
