import sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Polygon

out = sys.argv[1]
fig, ax = plt.subplots(figsize=(15, 6.6), dpi=130)
ax.set_xlim(0, 150); ax.set_ylim(0, 66); ax.axis("off")

lanes = [("Vendedor /\nemisor de nota", 50), ("Registrador\n(digitación)", 34), ("Revisor /\naprobador", 18), ("Reportes\ncomerciales", 2)]
for name, y in lanes:
    ax.add_patch(plt.Rectangle((0, y), 150, 16, fill=False, lw=1, ec="#555"))
    ax.add_patch(plt.Rectangle((0, y), 14, 16, fc="#e8eef6", ec="#555", lw=1))
    ax.text(7, y + 8, name, ha="center", va="center", fontsize=9, weight="bold")

def box(x, y, t, red=False, w=17, h=9):
    ax.add_patch(FancyBboxPatch((x - w/2, y - h/2), w, h, boxstyle="round,pad=0.4",
                 fc="#fde2e2" if red else "#ffffff", ec="#c00000" if red else "#003264", lw=2.2 if red else 1.3))
    ax.text(x, y, t, ha="center", va="center", fontsize=7.6)

def dia(x, y, t, red=False, w=19, h=12):
    ax.add_patch(Polygon([(x, y + h/2), (x + w/2, y), (x, y - h/2), (x - w/2, y)],
                 fc="#fde2e2" if red else "#fff7d6", ec="#c00000" if red else "#9c7a00", lw=2 if red else 1.2))
    ax.text(x, y, t, ha="center", va="center", fontsize=7)

def arr(x1, y1, x2, y2, t="", c="#333", ls="-"):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1), arrowprops=dict(arrowstyle="->", color=c, lw=1.2, ls=ls))
    if t: ax.text((x1 + x2)/2 + 0.8, (y1 + y2)/2 + 1, t, fontsize=7, color=c)

ax.add_patch(plt.Circle((20, 58), 2.3, fc="#003264")); ax.text(20, 62.5, "Inicio", ha="center", fontsize=7)
box(32, 58, "Emite nota de pedido\n(papel / imagen)")
box(32, 42, "Transcribe renglones\n(cantidad, precio, importe)", red=True)
dia(55, 42, "¿Campos\ncompletos?", red=True)
box(78, 42, "Marca estado de uso\nsin regla escrita", red=True)
dia(78, 26, "¿Nota en estado\nPEDIDO / dudosa?", red=True)
box(102, 26, "REVISAR (cola)\nsin motivo obligatorio", red=True)
box(102, 42, "Retrabajo: consultar\noriginal / imagen")
box(125, 26, "DISPONIBLE\no EXCLUIR")
box(125, 10, "Publica en reportes\n(Data Mart / Power BI)")
ax.add_patch(plt.Circle((143, 10), 2.3, fc="#003264")); ax.text(143, 4.2, "Fin", ha="center", fontsize=7)

arr(22.5, 58, 23, 58); arr(32, 53.5, 32, 46.5); arr(40.5, 42, 45.5, 42)
arr(64.5, 42, 69.5, 42); ax.text(60, 48.5, "Sí o No: no hay bloqueo,\nel vacío pasa igual", fontsize=7, color="#c00000")
arr(78, 37.5, 78, 32)
arr(87.5, 26, 93.5, 26, "Sí")
ax.plot([78, 78, 113], [20, 19.2, 19.2], color="#333", lw=1.2); arr(113, 19.2, 117, 22); ax.text(79, 16.5, "No", fontsize=7)
arr(102, 30.5, 102, 37.5, "retrabajo", c="#c00000", ls="--")
arr(110.5, 42, 125, 30.5, "", c="#333")
arr(125, 21.5, 125, 14.5); arr(133.5, 10, 140.7, 10)

ax.text(1, 65, "M1 · Flujo AS-IS del registro y validación de notas de pedido — HIDROCOM KALLPA (reconstruido de los archivos del lote; validar en Gemba)",
        fontsize=9.5, weight="bold", color="#003264")
ax.text(1, -0.5, "En rojo: dónde vive el defecto. 38 de 262 renglones (14,50 %) terminan en REVISAR: 13 por estado PEDIDO sin regla, 12 por campos vacíos o importe incoherente, 13 por motivo dudoso o no explicitado.",
        fontsize=7.6, color="#c00000")
plt.savefig(out, bbox_inches="tight"); print("ok", out)
