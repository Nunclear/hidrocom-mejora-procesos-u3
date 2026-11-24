"""Genera Ishikawa y matriz impacto x esfuerzo. Uso: python figuras.py <carpeta_salida>"""
import sys, os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

out = sys.argv[1]
NAVY, RED, GREY, OCHRE = "#003264", "#C00000", "#666666", "#9C7A00"

# ---------- Ishikawa ----------
fig, ax = plt.subplots(figsize=(13, 6), dpi=160)
ax.set_xlim(0, 130); ax.set_ylim(-4, 62); ax.axis("off")
ax.annotate("", xy=(107, 30), xytext=(3, 30), arrowprops=dict(arrowstyle="-|>", lw=2.8, color=NAVY, mutation_scale=24))
ax.add_patch(plt.Rectangle((107.5, 20), 21, 20, fc=NAVY, ec=NAVY))
ax.text(118, 30, "38 de 262\nrenglones\nen REVISAR\n(14,50 %)", ha="center", va="center", color="white", fontsize=14, weight="bold")
bones = {
    (38, True): ("Mano de obra", [("Criterio distinto al marcar", 0), ("Sin instructivo escrito", 0)]),
    (72, True): ("Método", [("Sin regla para PEDIDO", 1), ("Motivo no obligatorio", 0)]),
    (106, True): ("Máquina / Sistema", [("Captura sin validación", 1), ("Sin control de versión", 0)]),
    (38, False): ("Material", [("Notas tachadas o ilegibles", 0), ("Base de precio no indicada", 2)]),
    (72, False): ("Medición", [("CTQ no acordado", 0), ("Fechas estimadas (62 %)", 3)]),
    (106, False): ("Medio ambiente", [("Registro en lote, tarde", 0), ("Interrupciones en tienda", 0)]),
}
STY = {0: ("#222222", "", "normal"), 1: (RED, "✔ ", "bold"), 2: (OCHRE, "◐ ", "normal"), 3: (GREY, "✘ ", "normal")}
for (x, up), (m, causes) in bones.items():
    y1 = 54 if up else 6
    ax.plot([x, x - 9], [30, y1], color=NAVY, lw=2)
    ax.text(x - 9, y1 + (3.2 if up else -3.2), m, ha="center", va="center", fontsize=13, weight="bold", color=NAVY,
            bbox=dict(boxstyle="round,pad=0.35", fc="#E8EEF6", ec=NAVY, lw=1))
    for k, (c, v) in enumerate(causes):
        t = 0.33 + 0.36 * k
        cx = x - 9 * t; cy = 30 + (y1 - 30) * t
        col, pre, w = STY[v]
        ax.text(cx - 0.8, cy, pre + c, ha="right", va="center", fontsize=11, color=col, weight=w)
ax.text(3, -3, "✔ condición documental asociada a REVISAR por construcción (no prueba causa)     ◐ ambigüedad documentada     ✘ sin diferencia relevante (descriptivo)     (sin marca: hipótesis no verificada)",
        fontsize=10.5, color="#333")
plt.savefig(os.path.join(out, "A2_Ishikawa_HIDROCOM.png"), bbox_inches="tight", facecolor="white"); plt.close()

# ---------- Matriz impacto x esfuerzo ----------
ideas = [(1, "Regla escrita del estado PEDIDO", 5, 1, 0), (2, "Poka-Yoke: validación en la captura", 5, 2, 0),
         (3, "Motivo obligatorio al marcar", 4, 1, 0), (4, "Base de precio obligatoria", 3, 2, -0.26),
         (5, "Evidencia y aprobación al cerrar", 3, 2, 0), (6, "Catálogo estable de productos", 3, 3, 0),
         (7, "5S digital de carpetas", 2, 2, 0), (8, "Kaizen semanal de la cola", 3, 2, 0.26)]
fig, ax = plt.subplots(figsize=(7.4, 2.75), dpi=220)
fig.subplots_adjust(left=0.08, right=0.5, bottom=0.17, top=0.97)
ax.add_patch(plt.Rectangle((0.5, 3.5), 2.5, 2.1, color="#E3F1E3", zorder=0))
ax.axvline(3, color="#999", lw=0.8, ls="--"); ax.axhline(3.5, color="#999", lw=0.8, ls="--")
for n, t, im, es, j in ideas:
    win = n in (1, 2, 3)
    ax.scatter(es + j, im, s=300, color=RED if win else NAVY, zorder=3, edgecolor="white")
    ax.text(es + j, im, str(n), color="white", ha="center", va="center", fontsize=9, weight="bold", zorder=4)
ax.set_xlim(0.5, 5.5); ax.set_ylim(0.5, 5.6); ax.set_xticks(range(1, 6)); ax.set_yticks(range(1, 6))
ax.set_xlabel("Esfuerzo (1-5)", fontsize=10); ax.set_ylabel("Impacto (1-5)", fontsize=10)
ax.text(0.6, 5.35, "Ganar rápido", fontsize=9, color="#2E7D32", style="italic")
for s in ("top", "right"): ax.spines[s].set_visible(False)
fig.text(0.54, 0.92, "Idea  (prioridad = I × (6 − E))", fontsize=10, weight="bold", color=NAVY)
for k, (n, t, im, es, j) in enumerate(ideas):
    win = n in (1, 2, 3)
    fig.text(0.54, 0.83 - k * 0.1, f"{n}. {t}  ({im * (6 - es)})", fontsize=10, color=RED if win else "#222", weight="bold" if win else "normal")
plt.savefig(os.path.join(out, "I1_Matriz_HIDROCOM.png"), facecolor="white"); plt.close()
print("ok")
