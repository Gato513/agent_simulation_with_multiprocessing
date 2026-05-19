"""
pygame_utils/constants.py
=========================
Constantes globales de configuración visual del simulador.

Centraliza todos los valores de diseño en un único lugar para facilitar
ajustes sin modificar el código de renderizado. Incluye dimensiones de
ventana, colores por zona del mapa y radios de nodos.

Paleta de diseño
----------------
El simulador usa una estética cyberpunk urbano:
    - Fondo muy oscuro (#080B12) para maximizar el contraste.
    - Nodos con colores neón de alta saturación por zona.
    - Aristas en tonos oscuros del mismo color que el nodo (sutiles).
    - Vehículos en tonos neón del espectro opuesto al mapa (sin conflicto).
"""


# ──────────────────────────────────────────────────────────────────────────────
# Configuración de ventana
# ──────────────────────────────────────────────────────────────────────────────

WINDOW_WIDTH  = 1200   # ancho de la ventana en píxeles
WINDOW_HEIGHT = 720    # alto de la ventana en píxeles
WINDOW_NAME   = "Simulador de Tráfico — Encarnación"


# ──────────────────────────────────────────────────────────────────────────────
# Colores globales de la interfaz
# ──────────────────────────────────────────────────────────────────────────────

DARK_BG  = "#080B12"   # fondo principal de la ventana
TEXT_CLR = "#E8EAF0"   # color de texto general
ACCENT   = "#00d4ff"   # color de acento para elementos destacados
MUTED    = "#4a5068"   # color para elementos secundarios o inactivos


# ──────────────────────────────────────────────────────────────────────────────
# Colores de nodos por zona
# ──────────────────────────────────────────────────────────────────────────────
# Cada zona del Circuito Comercial tiene un color neón distinto.
# Los colores ocupan el espectro 172°-330° (cyan → azul → violeta → rosa)
# dejando el rango 0°-150° libre para los colores de los vehículos.

ZONA_COLORS = {
    "comercial"  : "#FF3CAC",   # rosa neón   — nodos de alta densidad comercial
    "secundaria" : "#784BA0",   # violeta      — calles secundarias
    "peatonal"   : "#2B86C5",   # azul         — zonas peatonales (cuellos de botella)
    "residencial": "#00F5D4",   # cyan turquesa — zona residencial (mayoría del mapa)
}


# ──────────────────────────────────────────────────────────────────────────────
# Colores de aristas por zona
# ──────────────────────────────────────────────────────────────────────────────
# Versiones oscurecidas de los colores de nodo para que las calles sean
# visibles pero no compitan visualmente con los nodos y vehículos.

ZONA_EDGE_COLORS = {
    "comercial"  : "#9B2D6A",   # rosa oscuro
    "secundaria" : "#5D3490",   # violeta oscuro
    "peatonal"   : "#1E3A5F",   # azul oscuro
    "residencial": "#006B66",   # cyan oscuro
}


# ──────────────────────────────────────────────────────────────────────────────
# Radios de nodos por zona
# ──────────────────────────────────────────────────────────────────────────────
# Los nodos comerciales son más grandes para jerarquizar visualmente
# las intersecciones de mayor importancia en el Circuito Comercial.
# Los residenciales son más pequeños porque dominan en cantidad (91 nodos).

ZONA_NODE_RADIUS = {
    "comercial"  : 8,
    "secundaria" : 6,
    "peatonal"   : 5,
    "residencial": 4,
}