"""Recálculo independiente de los indicadores del proyecto HIDROCOM (auditoría integral).

Uso (desde la raíz del repositorio):
    python -P auditoria_integral/14_EVIDENCIAS_AUDITORIA/recalculo_independiente.py

Lee las hojas fuente copiadas en 03_DMAIC/U3_DMAIC_HIDROCOM.xlsx (Datos, Comprobantes, Fechas,
Pendientes) y compara con los Datos de los libros Lean y Seis Sigma. No modifica ningún archivo
original. Escribe resultados_recalculo.json y resultados_recalculo.txt en esta carpeta.
"""
import json, math, os, sys, unicodedata, datetime as dt
from collections import Counter, defaultdict
import openpyxl
from scipy import stats

sys.stdout.reconfigure(encoding="utf-8")
OUT = os.path.dirname(os.path.abspath(__file__))
R = {}
log = []
def p(*a):
    s = " ".join(str(x) for x in a); print(s); log.append(s)

def load(path, sheet, header_row=5):
    ws = openpyxl.load_workbook(path, data_only=True)[sheet]
    H = [c.value for c in ws[header_row]]
    rows = [dict(zip(H, r)) for r in ws.iter_rows(min_row=header_row + 1, values_only=True) if r[0] is not None]
    return H, rows

E = lambda v: v is None or (isinstance(v, str) and v.strip() == "")
NZ = lambda v: not E(v) and abs(float(v)) > 1e-9
def wilson(k, n, z=1.959964):
    ph = k / n; d = 1 + z * z / n
    c = (ph + z * z / (2 * n)) / d; h = z * math.sqrt(ph * (1 - ph) / n + z * z / (4 * n * n)) / d
    return round(c - h, 4), round(c + h, 4)
sigma = lambda dpmo: stats.norm.ppf(1 - dpmo / 1e6) + 1.5

DM = "03_DMAIC/U3_DMAIC_HIDROCOM.xlsx"
H, D = load(DM, "Datos")
_, C = load(DM, "Comprobantes")
_, F = load(DM, "Fechas")
_, P = load(DM, "Pendientes")

# ---------- A. Población e identificadores ----------
ids = [r["id_detalle"] for r in D]; notas_det = {r["id_comprobante"] for r in D}
notas = [r["id_comprobante"] for r in C]
A = {
    "renglones": len(D), "id_detalle_unicos": len(set(ids)), "id_detalle_duplicados": [k for k, v in Counter(ids).items() if v > 1],
    "notas_comprobantes": len(notas), "notas_unicas": len(set(notas)), "notas_con_detalle": len(notas_det),
    "notas_sin_detalle": sorted(set(notas) - notas_det), "renglones_sin_nota": sorted(notas_det - set(notas)),
    "id_detalle_no_coincide_con_nota": [r["id_detalle"] for r in D if not str(r["id_detalle"]).startswith(str(r["id_comprobante"]) + "-")],
    "fechas_hoja_Fechas": len(F),
}
R["A_poblacion"] = A
p("A. Población:", json.dumps(A, ensure_ascii=False, default=str))

# notas sin detalle: estado
A2 = {n: next((c["estado_comprobante"], c["total"], c["observacion"]) for c in C if c["id_comprobante"] == n) for n in A["notas_sin_detalle"]}
R["A_notas_sin_detalle_estado"] = A2; p("   notas sin detalle:", A2)

# ---------- B. Estados de uso ----------
uso = Counter(r["uso_importe"] for r in D)
B = {k: {"n": v, "pct": round(v / len(D) * 100, 2), "IC95_Wilson": wilson(v, len(D))} for k, v in uso.items()}
B["importe_DISPONIBLE"] = round(sum(r["subtotal_producto"] or 0 for r in D if r["uso_importe"] == "DISPONIBLE"), 2)
R["B_estados"] = B; p("B. Estados:", B)

# ---------- C. Vacíos, oportunidades, DPMO ----------
def met(rows, incluir_dif):
    vq = sum(E(r["cantidad"]) for r in rows); vp = sum(E(r["precio_unitario"]) for r in rows); vs = sum(E(r["subtotal_producto"]) for r in rows)
    dif_only = sum(1 for r in rows if not E(r["subtotal_producto"]) and NZ(r["diferencia_importe"]))
    Dd = vq + vp + vs + (dif_only if incluir_dif else 0)
    U = len(rows); O = 3; dpmo = Dd / (U * O) * 1e6
    und = sum(1 for r in rows if E(r["cantidad"]) or E(r["precio_unitario"]) or E(r["subtotal_producto"]) or (incluir_dif and NZ(r["diferencia_importe"])))
    return {"U": U, "O": O, "UxO": U * O, "vacios_cant": vq, "vacios_precio": vp, "vacios_importe": vs, "dif_importe_no_vacio": dif_only,
            "D": Dd, "DPU": round(Dd / U, 4), "DPO": round(Dd / (U * O), 6), "DPMO": round(dpmo, 2), "sigma_1_5": round(sigma(dpmo), 4),
            "unidades_defectuosas": und, "yield_unidad": round(1 - und / U, 4), "yield_oportunidad": round(1 - Dd / (U * O), 4)}
sinex = [r for r in D if r["uso_importe"] != "EXCLUIR"]
C_ = {"criterio_30_solo_vacios_todo": met(D, False), "criterio_30_solo_vacios_sin_EXCLUIR": met(sinex, False),
      "criterio_35_vacios_mas_diferencia_todo": met(D, True), "criterio_35_sin_EXCLUIR": met(sinex, True)}
R["C_dpmo"] = C_
for k, v in C_.items(): p("C.", k, v)

# ---------- D. Coherencia aritmética independiente ----------
def base(r):
    u = (r.get("unidad_del_precio") or "").strip().lower()
    return 1000 if u == "millar" else 1
inc = []
for r in D:
    q, pr, st = r["cantidad"], r["precio_unitario"], r["subtotal_producto"]
    if E(q) or E(pr) or E(st):
        continue
    calc = float(q) * float(pr) / base(r)
    if abs(calc - float(st)) > 0.01:
        inc.append({"id": r["id_detalle"], "cant": q, "precio": pr, "base": r.get("unidad_del_precio"), "subtotal": st, "calc": round(calc, 4),
                    "diferencia_importe_fuente": r["diferencia_importe"], "importe_calculado_fuente": r["importe_calculado"], "uso": r["uso_importe"]})
flag_src = [r["id_detalle"] for r in D if NZ(r["diferencia_importe"])]
R["D_aritmetica"] = {"incoherentes_recalculo": inc, "n_incoherentes_recalculo": len(inc), "marcados_fuente_diferencia": flag_src,
                     "recalculo_no_marcados_en_fuente": [x["id"] for x in inc if x["id"] not in flag_src]}
p("D. Incoherencias recalculadas:", len(inc), "| marcadas en fuente:", len(flag_src))
for x in inc: p("   ", x)

# ---------- E. Notas: total vs suma de renglones ----------
tot = defaultdict(float); faltan = defaultdict(int)
for r in D:
    if E(r["subtotal_producto"]): faltan[r["id_comprobante"]] += 1
    else: tot[r["id_comprobante"]] += float(r["subtotal_producto"])
dif_notas = []
for c in C:
    n = c["id_comprobante"]
    if n in notas_det and c["total"] is not None and abs(tot[n] - float(c["total"])) > 0.01:
        dif_notas.append({"nota": n, "total": c["total"], "suma_renglones": round(tot[n], 2), "renglones_sin_importe": faltan[n], "estado": c["estado_comprobante"]})
R["E_notas_total_vs_renglones"] = {"n": len(dif_notas), "detalle": dif_notas}
p("E. Notas cuyo total ≠ suma de renglones:", len(dif_notas))

# ---------- F. Fechas ----------
est_f = Counter(f["estado"] for f in F)
fechas = sorted(c["fecha_emision"] for c in C if c["fecha_emision"])
inicio = dt.datetime(2026, 3, 9)
F_ = {"estado_notas_hoja_Fechas": dict(est_f), "tipo_fecha_notas_Comprobantes": dict(Counter(c["tipo_fecha"] for c in C)),
      "tipo_fecha_renglones": dict(Counter(r["tipo_fecha"] for r in D)), "rango": [str(fechas[0].date()), str(fechas[-1].date())],
      "notas_anteriores_al_inicio_09_03_2026": sum(1 for x in fechas if x < inicio), "meses_rango": round((fechas[-1] - fechas[0]).days / 30.44, 1)}
R["F_fechas"] = F_; p("F. Fechas:", F_)

# ---------- G. Pareto recalculado desde Datos ----------
def cond(r):
    if "PEDIDO" in (r["estado_comprobante"], r["estado_linea"]): return "Estado PEDIDO"
    if E(r["cantidad"]) or E(r["precio_unitario"]) or E(r["subtotal_producto"]): return "Campos numéricos incompletos"
    if NZ(r["diferencia_importe"]): return "Diferencia de importe"
    if not E(r["observacion"]) or r["estado_linea"] == "DUDOSA": return "Observación o lectura dudosa"
    return "Motivo no explicitado"
rev = [r for r in D if r["uso_importe"] == "REVISAR"]
G = Counter(cond(r) for r in rev)
pend = Counter(r["Condición principal"] for r in P)
mism = [r["id_detalle"] for r in rev if cond(r).split()[0] not in next(x["Condición principal"] for x in P if x["ID"] == r["id_detalle"])]
R["G_pareto"] = {"recalculado": dict(G), "hoja_Pendientes": dict(pend), "ids_con_clasificacion_distinta": mism,
                 "ids_REVISAR_igual_Pendientes": sorted(r["id_detalle"] for r in rev) == sorted(x["ID"] for x in P)}
p("G. Pareto recalculado:", dict(G), "| Pendientes:", dict(pend), "| discrepancias:", mism)

# solapamiento PEDIDO / numéricas
pedido = {r["id_detalle"] for r in D if "PEDIDO" in (r["estado_comprobante"], r["estado_linea"])}
numer = {r["id_detalle"] for r in D if E(r["cantidad"]) or E(r["precio_unitario"]) or E(r["subtotal_producto"]) or NZ(r["diferencia_importe"])}
revs = {r["id_detalle"] for r in rev}
R["G_solapamiento"] = {"pedido": len(pedido), "pedido_en_REVISAR": len(pedido & revs), "numericas": len(numer), "numericas_en_REVISAR": len(numer & revs),
                       "ambas_en_REVISAR": len(pedido & numer & revs), "union_en_REVISAR": len((pedido | numer) & revs),
                       "numericas_fuera_de_REVISAR": sorted(numer - revs)}
p("G2. Solapamiento:", R["G_solapamiento"])

# ---------- H. Asociaciones y dependencia intra-nota ----------
def tabla(pred):
    a = sum(1 for r in D if pred(r) and r["uso_importe"] == "REVISAR"); b = sum(1 for r in D if pred(r)) - a
    c = sum(1 for r in D if not pred(r) and r["uso_importe"] == "REVISAR"); d = sum(1 for r in D if not pred(r)) - c
    odds, pf = stats.fisher_exact([[a, b], [c, d]])
    chi = stats.chi2_contingency([[a, b], [c, d]], correction=True)
    return {"tabla": [[a, b], [c, d]], "tasa_si": round(a / (a + b), 4), "tasa_no": round(c / (c + d), 4), "fisher_p": round(pf, 4),
            "chi2_yates_p": round(chi.pvalue, 4), "esperados_min": round(float(chi.expected_freq.min()), 2)}
Hh = {"fecha_estimada": tabla(lambda r: r["tipo_fecha"] == "ESTIMADA"),
      "pedido": tabla(lambda r: r["id_detalle"] in pedido), "numerica": tabla(lambda r: r["id_detalle"] in numer)}
por_nota = Counter(r["id_comprobante"] for r in rev)
Hh["REVISAR_por_nota"] = {"notas_con_REVISAR": len(por_nota), "max_en_una_nota": max(por_nota.values()), "top": por_nota.most_common(6)}
# tasa por nota (cluster): proporción de notas con al menos un REVISAR
n_por_nota = Counter(r["id_comprobante"] for r in D)
Hh["renglones_por_nota"] = {"media": round(len(D) / len(n_por_nota), 2), "max": max(n_por_nota.values()), "min": min(n_por_nota.values())}
# efecto de diseño aproximado (ICC por ANOVA de un factor sobre indicador REVISAR)
grupos = defaultdict(list)
for r in D: grupos[r["id_comprobante"]].append(1 if r["uso_importe"] == "REVISAR" else 0)
k = len(grupos); N = len(D); m0 = (N - sum(len(g) ** 2 for g in grupos.values()) / N) / (k - 1)
gm = sum(sum(g) for g in grupos.values()) / N
msb = sum(len(g) * (sum(g) / len(g) - gm) ** 2 for g in grupos.values()) / (k - 1)
msw = sum(sum((x - sum(g) / len(g)) ** 2 for x in g) for g in grupos.values()) / (N - k)
icc = (msb - msw) / (msb + (m0 - 1) * msw)
deff = 1 + (N / k - 1) * icc
Hh["ICC_REVISAR_intra_nota"] = round(icc, 3); Hh["efecto_diseno"] = round(deff, 2); Hh["n_efectivo"] = round(N / deff, 1)
R["H_asociaciones"] = Hh
for kk, v in Hh.items(): p("H.", kk, v)

# ---------- I. Consistencia entre los tres libros ----------
def datos(path):
    ws = openpyxl.load_workbook(path, data_only=True)["Datos"]
    return [tuple(c for c in r) for r in ws.iter_rows(min_row=5, values_only=True)]
dl = datos("01_Lean/U3_Lean_HIDROCOM.xlsx"); ds = datos("02_Seis_Sigma/U3_Seis_Sigma_HIDROCOM.xlsx"); dd = datos(DM)
R["I_libros"] = {"Lean_igual_DMAIC": dl == dd, "SeisSigma_igual_DMAIC": ds == dd, "filas": len(dd)}
p("I. Datos idénticos Lean/DMAIC:", dl == dd, "SeisSigma/DMAIC:", ds == dd)

# ---------- J. Categorías / productos ----------
def norm(s): return "".join(ch for ch in unicodedata.normalize("NFD", str(s).lower().strip()) if unicodedata.category(ch) != "Mn")
prods = Counter(r["producto_normalizado"] for r in D)
var = defaultdict(set)
for pnm in prods: var[norm(pnm).rstrip("s")].add(pnm)
R["J_productos"] = {"productos_distintos": len(prods), "grupos_con_variantes_ortograficas": {k: sorted(v) for k, v in var.items() if len(v) > 1},
                    "producto_original_distinto_normalizado": sum(1 for r in D if r["producto_original"] != r["producto_normalizado"])}
p("J. Productos:", R["J_productos"]["productos_distintos"], "| variantes:", len(R["J_productos"]["grupos_con_variantes_ortograficas"]))

# ---------- K. Sensibilidad del beneficio (supuestos del Excel oficial) ----------
meses = F_["meses_rango"]
def benef(vol_rev_mes, despues_frac=13 / 38, mins=10, ch=7.5, costo=120):
    return round((vol_rev_mes - vol_rev_mes * despues_frac) * mins / 60 * ch * 12 - costo, 2)
R["K_beneficio"] = {"supuesto_1_lote_por_mes": benef(38), "volumen_segun_rango_de_fechas": benef(38 / meses), "REVISAR_por_mes_segun_rango": round(38 / meses, 2),
                    "punto_equilibrio_REVISAR_mes": round(120 / ((1 - 13 / 38) * 10 / 60 * 7.5 * 12), 2),
                    "mins_5": benef(38, mins=5), "mins_20": benef(38, mins=20)}
p("K. Beneficio:", R["K_beneficio"])

json.dump(R, open(os.path.join(OUT, "resultados_recalculo.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1, default=str)
open(os.path.join(OUT, "resultados_recalculo.txt"), "w", encoding="utf-8").write("\n".join(log))
print("OK ->", OUT)
