"""
show_graph.py — Visualizador del Circuito Comercial de Encarnación
==================================================================
Modos de uso:
  python show_graph.py              → panel doble: grafo + superposición
  python show_graph.py --solo       → solo el grafo (sin imagen)
  python show_graph.py --overlay    → solo superposición sobre imagen
  python show_graph.py --info       → estadísticas en consola

Interactividad:
  Click izquierdo sobre un nodo  → muestra nombre y atributos
  Click derecho                  → cierra el tooltip

Requiere en el mismo directorio:
  graph_config.py
  nueva_represetacion_morfologia_urbana.png
"""

# ══════════════════════════════════════════════════════════════════════════
#  PASO 1 — fijar backend ANTES de importar pyplot
#
#  ORDEN DE PRIORIDAD (probados en secuencia, se usa el primero disponible):
#    1. TkAgg   — tkinter, disponible en la mayoría de sistemas
#    2. QtAgg   — PyQt6 / PySide6
#    3. Qt5Agg  — PyQt5 / PySide2
#
#  matplotlib.use() DEBE llamarse antes de cualquier "import matplotlib.pyplot"
# ══════════════════════════════════════════════════════════════════════════
import sys, os, math
import matplotlib

_CANDIDATES = ["TkAgg", "QtAgg", "Qt5Agg", "GTK4Agg", "GTK3Agg", "WxAgg"]
_chosen = None

for _b in _CANDIDATES:
    try:
        matplotlib.use(_b, force=True)
        # Importar pyplot UNA SOLA VEZ aquí para verificar que el backend carga
        import matplotlib.pyplot as plt
        # Crear figura mínima para confirmar que el canvas responde
        _fig = plt.figure()
        assert hasattr(_fig.canvas, "mpl_connect")
        plt.close(_fig)
        _chosen = _b
        break
    except Exception as _e:
        # Limpiar completamente matplotlib para el siguiente intento
        _mods = [k for k in sys.modules
                 if k == "matplotlib" or k.startswith("matplotlib.")]
        for _k in _mods:
            del sys.modules[_k]
        import matplotlib  # reimportar el núcleo limpio

if _chosen is None:
    print("[show_graph] ADVERTENCIA: ningún backend interactivo disponible.")
    print("  El click no funcionará. Para habilitarlo:")
    print("    uv add pyqt6        o   uv add pyqt5")
    print("    sudo pacman -S tk   (backend Tk)")
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
else:
    print(f"[show_graph] Backend: {_chosen}")

# ══════════════════════════════════════════════════════════════════════════
#  PASO 2 — importar el resto de matplotlib y librerías
#  (pyplot ya fue importado en el paso 1 durante la selección de backend)
# ══════════════════════════════════════════════════════════════════════════
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
import networkx as nx
import numpy as np

try:
    from PIL import Image
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False

try:
    from graph_config_osm import nodes, node_position, connections
except ImportError:
    print("ERROR: No se encontró graph_config.py")
    sys.exit(1)

try:
    from graph_model import generate_graph
    GRAPH_MODEL = True
except ImportError:
    GRAPH_MODEL = False


# ══════════════════════════════════════════════════════════════════════════
#  PALETA
# ══════════════════════════════════════════════════════════════════════════

DARK_BG  = "#0d0f14"
TEXT_CLR = "#e8eaf0"
ACCENT   = "#00d4ff"
MUTED    = "#4a5068"

ZONA_COLORS = {
    "comercial":   "#ff6b35",
    "secundaria":  "#ffd166",
    "peatonal":    "#06d6a0",
    "residencial": "#74b9ff",
}
ZONA_EDGE_COLORS = {
    "comercial":   "#ff9560",
    "secundaria":  "#ffe599",
    "peatonal":    "#4fffcc",
    "residencial": "#aad4ff",
}
ZONA_NODE_SIZE = {
    "comercial":   120,
    "secundaria":  90,
    "peatonal":    60,
    "residencial": 45,
}

def edge_color_by_vel(vel):
    if vel >= 80: return "#ff4444"
    if vel >= 60: return "#ff8c42"
    if vel >= 50: return "#ffd166"
    if vel >= 30: return "#74b9ff"
    if vel >= 20: return "#a8a8b3"
    return "#06d6a0"


# ══════════════════════════════════════════════════════════════════════════
#  GRAFO
# ══════════════════════════════════════════════════════════════════════════

def build_graph():
    if GRAPH_MODEL:
        return generate_graph()
    G = nx.DiGraph()
    G.add_nodes_from(nodes)
    for origen, destino, attrs in connections:
        G.add_edge(origen, destino, **attrs)
        G.add_edge(destino, origen, **attrs)
    return G


# ══════════════════════════════════════════════════════════════════════════
#  COORDENADAS  norm[-1,1] → píxeles de imagen
# ══════════════════════════════════════════════════════════════════════════

def norm_to_img_px(nx_, ny_, img_w, img_h):
    return (nx_ + 1) / 2.0 * img_w, (1.0 - (ny_ + 1) / 2.0) * img_h

def build_img_pos(np_, img_w, img_h):
    return {l: norm_to_img_px(x, y, img_w, img_h) for l, (x, y) in np_.items()}


# ══════════════════════════════════════════════════════════════════════════
#  NODE PICKER — interactividad por click
# ══════════════════════════════════════════════════════════════════════════

class NodePicker:
    """
    Escucha button_press_event en `ax`.
    Click izquierdo → tooltip con nombre y atributos del nodo más cercano.
    Click derecho   → cierra el tooltip.
    Si se pasa `pair=(ax2, pos2)`, también resalta el nodo en ese panel.
    """

    _BOX = dict(
        boxstyle="round,pad=0.55",
        facecolor="#111827",
        edgecolor=ACCENT,
        alpha=0.96,
        linewidth=1.4,
    )

    def __init__(self, ax, G, pos, radius=0.07, pair=None):
        self.ax     = ax
        self.G      = G
        self.pos    = pos
        self.radius = radius   # fracción del span del axes
        self.pair   = pair     # (ax2, pos2) panel sincronizado

        self._labels = list(pos.keys())
        self._xy     = np.array([pos[l] for l in self._labels], dtype=float)
        self._active = []      # artists en pantalla que hay que borrar

        # Conectar al canvas de la figura
        self._cid = ax.figure.canvas.mpl_connect(
            "button_press_event", self._on_click
        )

    # ── Buscar nodo más cercano ────────────────────────────────────────

    def _nearest(self, xc, yc):
        """Devuelve (label, distancia_normalizada) del nodo más cercano."""
        xl = self.ax.get_xlim()
        yl = self.ax.get_ylim()
        sx = abs(xl[1] - xl[0]) or 1.0
        sy = abs(yl[1] - yl[0]) or 1.0
        diff = self._xy - np.array([xc, yc])
        dist = np.hypot(diff[:, 0] / sx, diff[:, 1] / sy)
        idx  = int(np.argmin(dist))
        return self._labels[idx], dist[idx]

    # ── Formatear tooltip ──────────────────────────────────────────────

    def _make_text(self, label):
        d    = self.G.nodes.get(label, {})
        zona = d.get("zona", "—")
        sf   = "Sí" if d.get("tiene_semaforo") else "No"
        cap  = d.get("capacidad", "—")
        vp   = d.get("vehi_presentes", 0)
        din  = self.G.in_degree(label)  if self.G.is_directed() else self.G.degree(label)
        dout = self.G.out_degree(label) if self.G.is_directed() else "—"
        name = label if len(label) <= 46 else label[:43] + "…"

        return (
            f"{name}\n"
            f"{'─'*36}\n"
            f"Zona {zona}\n"
            f"Semáforo {sf}\n"
            f"Capacidad {cap}\n"
            f"Veh. pres.{vp}\n"
            f"Grado ent.{din}   sal. {dout}"
        )

    # ── Borrar feedback anterior ───────────────────────────────────────

    def _clear(self):
        for a in self._active:
            try:
                a.remove()
            except Exception:
                pass
        self._active.clear()

    # ── Añadir anillo de highlight ─────────────────────────────────────

    def _add_ring(self, ax, pos_dict, label):
        x, y   = pos_dict[label]
        xl, yl = ax.get_xlim(), ax.get_ylim()
        span   = max(abs(xl[1]-xl[0]), abs(yl[1]-yl[0]))
        r      = span * 0.018

        ring = plt.Circle(
            (x, y), r,
            fill=False, edgecolor=ACCENT,
            linewidth=2.5, zorder=15, alpha=0.95,
        )
        ax.add_patch(ring)
        self._active.append(ring)

        dot = ax.scatter([x], [y], s=60, c=ACCENT,
                        zorder=16, linewidths=0)
        self._active.append(dot)

    # ── Añadir tooltip ─────────────────────────────────────────────────

    def _add_tooltip(self, ax, pos_dict, label):
        x, y   = pos_dict[label]
        xl, yl = ax.get_xlim(), ax.get_ylim()
        span_y = yl[1] - yl[0]
        span   = max(abs(xl[1]-xl[0]), abs(span_y))
        r      = span * 0.018

        # Poner encima si hay espacio, abajo si no
        frac   = (y - min(yl)) / (abs(span_y) or 1)
        if frac > 0.85:          # cerca del borde superior
            va, dy = "top",    -r * 1.6
        else:
            va, dy = "bottom",  r * 1.6

        txt = ax.text(
            x, y + dy,
            self._make_text(label),
            fontsize    = 8,
            fontfamily  = "monospace",
            color       = TEXT_CLR,
            va          = va,
            ha          = "center",
            zorder      = 25,
            bbox        = self._BOX,
            clip_on     = False,
            path_effects= [pe.withStroke(linewidth=1, foreground=DARK_BG)],
        )
        self._active.append(txt)

    # ── Evento ────────────────────────────────────────────────────────

    def _on_click(self, event):
        # Siempre imprimir para poder diagnosticar
        _ex = f"{event.xdata:.3f}" if event.xdata is not None else "None"
        _ey = f"{event.ydata:.3f}" if event.ydata is not None else "None"
        print(f"[EVENT] button={event.button} inaxes={event.inaxes is not None} x={_ex} y={_ey}")

        if event.inaxes is not self.ax:
            return
        if event.xdata is None or event.ydata is None:
            return

        # Click derecho → limpiar y salir
        if event.button == 3:
            self._clear()
            event.canvas.draw_idle()
            return

        label, dist = self._nearest(event.xdata, event.ydata)

        self._clear()

        if dist > self.radius:
            # Click en el vacío
            event.canvas.draw_idle()
            return

        # Feedback en el axes principal
        self._add_ring(self.ax, self.pos, label)
        self._add_tooltip(self.ax, self.pos, label)

        # Highlight sincronizado en el segundo panel
        if self.pair is not None:
            ax2, pos2 = self.pair
            if label in pos2:
                self._add_ring(ax2, pos2, label)

        # Imprimir también en consola (útil para copiar el nombre)
        print(f"[NODO] {label}")

        event.canvas.draw_idle()


# ══════════════════════════════════════════════════════════════════════════
#  HELPERS DE DIBUJO
# ══════════════════════════════════════════════════════════════════════════

def get_node_attrs(G):
    nc, ns, nec = [], [], []
    for n in G.nodes():
        z = G.nodes[n].get("zona", "residencial")
        nc.append(ZONA_COLORS.get(z, "#74b9ff"))
        ns.append(ZONA_NODE_SIZE.get(z, 45))
        nec.append(ZONA_EDGE_COLORS.get(z, "#aad4ff"))
    return nc, ns, nec

def get_edge_attrs(G):
    ec, ew = [], []
    for _, _, d in G.edges(data=True):
        vel = d.get("vel_max", 30)
        ec.append(edge_color_by_vel(vel))
        ew.append(0.5 if vel <= 20 else (0.9 if vel <= 30 else 1.3))
    return ec, ew

def draw_graph_on_ax(ax, G, pos, bg=DARK_BG, alpha=0.88):
    ax.set_facecolor(bg)
    nc, ns, nec = get_node_attrs(G)
    ec, ew = get_edge_attrs(G)
    nx.draw_networkx_edges(
        G, pos, ax=ax,
        edge_color=ec, width=ew, alpha=alpha,
        arrows=False
    )
    nx.draw_networkx_nodes(
        G, pos, ax=ax,
        node_color=nc, node_size=ns,
        linewidths=0.8, edgecolors=nec, alpha=0.95,
    )

def draw_legend(ax, compact=False):
    fs = 6 if compact else 7
    p1 = [
        mpatches.Patch(facecolor=ZONA_COLORS[z], edgecolor=ZONA_EDGE_COLORS[z], linewidth=0.8, label=z.capitalize())
        for z in ["comercial", "secundaria", "residencial", "peatonal"]
    ]
    p2 = [
        mpatches.Patch(facecolor=edge_color_by_vel(v), label=lb)
        for v, lb in [(80,"Trunk 80"), (60,"Primary 60"), (50,"Secondary 50"), (30,"Residential 30"), (20,"Service 20"), (10,"Peatonal 10")]
    ]
    l1 = ax.legend(
        handles=p1, 
        title="Zona", 
        title_fontsize=fs+1,
        loc="lower left", fontsize=fs,
        facecolor="#1a1e2e", edgecolor=MUTED,
        labelcolor=TEXT_CLR, framealpha=0.92)
    l1.get_title().set_color(ACCENT)
    ax.add_artist(l1)
    l2 = ax.legend(handles=p2, title="Vel (km/h)", title_fontsize=fs+1,
                loc="lower right", fontsize=fs,
                facecolor="#1a1e2e", edgecolor=MUTED,
                labelcolor=TEXT_CLR, framealpha=0.92)
    l2.get_title().set_color(ACCENT)

def draw_stats(ax, G, compact=False):
    from collections import Counter
    zonas = Counter(d.get("zona","?") for _,d in G.nodes(data=True))
    lines = (
        [f"  Nodos:   {G.number_of_nodes()}",
         f"  Aristas: {G.number_of_edges()}",
         "  ──────────────"] +
        [f"  {z}: {c}" for z,c in sorted(zonas.items())]
    )
    ax.text(0.01, 0.99, "\n".join(lines),
            transform=ax.transAxes, va="top", ha="left",
            fontsize=6 if compact else 7, family="monospace", color=TEXT_CLR,
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#1a1e2e",
                      edgecolor=MUTED, alpha=0.92))

def draw_hint(target, compact=False, use_fig=False):
    fs  = 6 if compact else 7
    msg = "● Click izquierdo = nombre del nodo   |   Click derecho = cerrar"
    kw  = dict(fontsize=fs, fontfamily="monospace", color=ACCENT, alpha=0.80)
    if use_fig:
        target.text(0.5, 0.003, msg, ha="center", va="bottom",
                    transform=target.transFigure, **kw)
    else:
        target.text(0.5, 0.005, msg, ha="center", va="bottom",
                    transform=target.transAxes, **kw)


# ══════════════════════════════════════════════════════════════════════════
#  IMAGEN
# ══════════════════════════════════════════════════════════════════════════

REF_IMAGE = "nueva_represetacion_morfologia_urbana.png"

def load_ref_image():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), REF_IMAGE)
    if not PIL_AVAILABLE:
        print("AVISO: instalá Pillow → pip install Pillow")
        return None
    if not os.path.exists(path):
        print(f"AVISO: no se encontró {path}")
        return None
    return np.array(Image.open(path))


# ══════════════════════════════════════════════════════════════════════════
#  MODOS
# ══════════════════════════════════════════════════════════════════════════

def mode_solo(G, pos):
    fig, ax = plt.subplots(figsize=(14, 14))
    fig.patch.set_facecolor(DARK_BG)
    draw_graph_on_ax(ax, G, pos, bg=DARK_BG)
    draw_legend(ax)
    draw_stats(ax, G)
    draw_hint(ax)
    ax.set_title("CIRCUITO COMERCIAL — ENCARNACIÓN",
                 color=ACCENT, fontsize=14, fontweight="bold",
                 fontfamily="monospace", pad=14,
                 path_effects=[pe.withStroke(linewidth=3, foreground=DARK_BG)])
    ax.axis("off")
    plt.tight_layout(pad=1.5)
    fig._picker = NodePicker(ax, G, pos, radius=0.07)
    plt.show()


def mode_overlay(G, pos):
    img = load_ref_image()
    if img is None:
        mode_solo(G, pos); return
    h, w = img.shape[:2]
    ipos = build_img_pos(pos, w, h)

    fig, ax = plt.subplots(figsize=(14, 14))
    fig.patch.set_facecolor(DARK_BG)
    ax.imshow(img, extent=[0, w, h, 0], aspect="equal", alpha=0.50)
    draw_graph_on_ax(ax, G, ipos, bg="none", alpha=0.92)
    draw_legend(ax, compact=True)
    draw_stats(ax, G, compact=True)
    draw_hint(ax, compact=True)
    ax.set_xlim(0, w); ax.set_ylim(h, 0)
    ax.set_facecolor(DARK_BG)
    ax.set_title("CIRCUITO COMERCIAL — SUPERPOSICIÓN",
                 color=ACCENT, fontsize=12, fontweight="bold",
                 fontfamily="monospace", pad=12)
    ax.axis("off")
    plt.tight_layout(pad=1.0)
    fig._picker = NodePicker(ax, G, ipos, radius=0.05)
    plt.show()


def mode_dual(G, pos):
    img = load_ref_image()
    if img is None:
        mode_solo(G, pos); return
    h, w = img.shape[:2]
    ipos = build_img_pos(pos, w, h)

    fig = plt.figure(figsize=(26, 14), facecolor=DARK_BG)

    # Panel izquierdo — grafo
    ax_l = fig.add_subplot(1, 2, 1)
    ax_l.set_facecolor(DARK_BG)
    draw_graph_on_ax(ax_l, G, pos, bg=DARK_BG)
    draw_legend(ax_l, compact=True)
    draw_stats(ax_l, G, compact=True)
    ax_l.set_title("GRAFO  ·  COORDENADAS NORMALIZADAS",
                   color=ACCENT, fontsize=10, fontweight="bold",
                   fontfamily="monospace", pad=10,
                   path_effects=[pe.withStroke(linewidth=2, foreground=DARK_BG)])
    ax_l.axis("off")

    # Panel derecho — superposición
    ax_r = fig.add_subplot(1, 2, 2)
    ax_r.set_facecolor(DARK_BG)
    ax_r.imshow(img, extent=[0, w, h, 0], aspect="equal", alpha=0.50)
    draw_graph_on_ax(ax_r, G, ipos, bg="none", alpha=0.92)
    ax_r.set_xlim(0, w); ax_r.set_ylim(h, 0)
    ax_r.set_title("SUPERPOSICIÓN  ·  IMAGEN DE REFERENCIA",
                   color=ACCENT, fontsize=10, fontweight="bold",
                   fontfamily="monospace", pad=10)
    ax_r.axis("off")

    fig.add_artist(plt.Line2D(
        [0.5, 0.5], [0.04, 0.96], transform=fig.transFigure,
        color=MUTED, linewidth=0.8, linestyle="--",
    ))
    fig.suptitle(
        "CIRCUITO COMERCIAL DE ENCARNACIÓN  —  Verificación Morfológica",
        color=TEXT_CLR, fontsize=14, fontweight="bold",
        fontfamily="monospace", y=0.985,
        path_effects=[pe.withStroke(linewidth=3, foreground=DARK_BG)],
    )
    draw_hint(fig, compact=True, use_fig=True)
    plt.tight_layout(pad=1.2, rect=[0, 0.015, 1, 0.97])

    # Pickers sincronizados: click izq → tooltip izq + anillo der
    #                        click der → tooltip der + anillo izq
    # IMPORTANTE: guardar en variable para evitar garbage collection
    _picker_l = NodePicker(ax_l, G, pos,  radius=0.07, pair=(ax_r, ipos))
    _picker_r = NodePicker(ax_r, G, ipos, radius=0.04, pair=(ax_l, pos))
    fig._pickers = [_picker_l, _picker_r]   # anclar al objeto figura

    plt.show()


def mode_info(G):
    from collections import Counter
    print("\n" + "═"*60)
    print("  CIRCUITO COMERCIAL — ENCARNACIÓN")
    print("═"*60)
    print(f"  Nodos:         {G.number_of_nodes()}")
    print(f"  Aristas:       {G.number_of_edges()}")
    zonas = Counter(d.get("zona","?") for _,d in G.nodes(data=True))
    print("\n  Nodos por zona:")
    for z,c in sorted(zonas.items()): print(f"    {z:<15} {c:>4}")
    sf = sum(1 for _,d in G.nodes(data=True) if d.get("tiene_semaforo"))
    print(f"\n  Con semáforo:  {sf}")
    print(f"  Sin semáforo:  {G.number_of_nodes()-sf}")
    cap = sum(d.get("capacidad",0) for _,d in G.nodes(data=True))
    print(f"  Cap. total:    {cap}")
    vels = Counter(d.get("vel_max",0) for _,_,d in G.edges(data=True))
    print("\n  Aristas por vel_max:")
    for v,c in sorted(vels.items()): print(f"    {v:>3} km/h → {c:>4}")
    deg = sorted(G.degree(), key=lambda x: -x[1])[:5]
    print("\n  Top 5 nodos por grado:")
    for n,d in deg: print(f"    [{d:>3}] {n[:55]}")
    print("═"*60 + "\n")


# ══════════════════════════════════════════════════════════════════════════
#  MAIN
# ══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    G   = build_graph()
    arg = sys.argv[1].lower() if len(sys.argv) > 1 else "--dual"

    if   arg == "--solo":    mode_solo(G, node_position)
    elif arg == "--overlay": mode_overlay(G, node_position)
    elif arg == "--info":    mode_info(G)
    else:                    mode_dual(G, node_position)
