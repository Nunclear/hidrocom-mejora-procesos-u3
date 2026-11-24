"""PM-08 · Comparación de solo lectura: Original_Comprobantes.xlsx vs Comprobantes_Revisados.xlsx (+ Historial_Correcciones).

Uso: python -P pm08_original_vs_revisado.py <carpeta_Fuente_del_paquete>
- No modifica los archivos (read_only). Registra SHA-256 de ambos.
- Publica solo agregados e identificadores ya públicos en el repositorio (id_detalle / id_comprobante).
- Alcance (issue #1, Q3): describe transformaciones de la transcripción; NO prueba una causa operativa
  ni la corrección de cada dato frente al original físico.
Salida: pm08_resultados.json y pm08_resultados.md en esta carpeta.
"""
import hashlib, json, os, sys
from collections import Counter, defaultdict
import openpyxl
sys.stdout.reconfigure(encoding="utf-8")
SRC = sys.argv[1]; OUT = os.path.dirname(os.path.abspath(__file__))
fo, fr = os.path.join(SRC, "Original_Comprobantes.xlsx"), os.path.join(SRC, "Comprobantes_Revisados.xlsx")
sha = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()

def tabla(path, hoja):
    ws = openpyxl.load_workbook(path, read_only=True, data_only=True)[hoja]
    it = ws.iter_rows(values_only=True); H = list(next(it))
    return H, [dict(zip(H, r)) for r in it if r and r[0]]

E = lambda v: v is None or str(v).strip() == ""
def num(v):
    try: return float(str(v).replace(",", "."))
    except Exception: return None

Ho, O = tabla(fo, "Detalle_Productos"); Hr, Rv = tabla(fr, "Detalle_Productos")
_, CO = tabla(fo, "Comprobantes"); _, CR = tabla(fr, "Comprobantes")
_, HC = tabla(fr, "Historial_Correcciones")
o = {r["id_detalle"]: r for r in O}; rv = {r["id_detalle"]: r for r in Rv}
comunes = sorted(set(o) & set(rv)); solo_o = sorted(set(o) - set(rv)); solo_r = sorted(set(rv) - set(o))
CAMPOS = ["cantidad", "precio_unitario", "subtotal_producto"]
res = {"sha256": {"Original_Comprobantes.xlsx": sha(fo), "Comprobantes_Revisados.xlsx": sha(fr)},
       "columnas_original_no_en_revisado": [c for c in Ho if c not in Hr], "columnas_revisado_no_en_original": [c for c in Hr if c not in Ho],
       "renglones": {"original": len(o), "revisado": len(rv), "comunes": len(comunes), "solo_original": len(solo_o), "solo_revisado": len(solo_r)},
       "notas": {"original": len(CO), "revisado": len(CR)}}

# Transiciones por campo numérico en los renglones comunes
trans = {c: Counter() for c in CAMPOS}
for i in comunes:
    for c in CAMPOS:
        a, b = o[i].get(c), rv[i].get(c)
        if E(a) and E(b): k = "vacío → vacío"
        elif E(a): k = "vacío → completado"
        elif E(b): k = "dato → vacío"
        else: k = "igual" if num(a) == num(b) else "valor cambiado"
        trans[c][k] += 1
res["transiciones_campos_numericos"] = {c: dict(v) for c, v in trans.items()}

# Los 30 vacíos del revisado: ¿ya estaban vacíos en la captura original?
vacios_rev = [(i, c) for i in rv for c in CAMPOS if E(rv[i].get(c))]
origen = Counter("vacío también en original" if i in o and E(o[i].get(c)) else ("sin renglón en original" if i not in o else "tenía dato en original")
                 for i, c in vacios_rev)
res["vacios_revisado"] = {"total": len(vacios_rev), "origen": dict(origen)}

# Estado PEDIDO y uso_importe
def ped(r): return "PEDIDO" in (str(r.get("estado_comprobante")), str(r.get("estado_linea")))
res["pedido"] = {"en_original": sum(ped(o[i]) for i in comunes), "en_revisado": sum(ped(rv[i]) for i in comunes),
                 "uso_importe_en_original": "uso_importe" in Ho}
rev_ids = [i for i in rv if rv[i].get("uso_importe") == "REVISAR"]
res["REVISAR_revisado"] = {"total": len(rev_ids), "presentes_en_original": sum(i in o for i in rev_ids)}
if "uso_importe" in Ho:
    res["REVISAR_revisado"]["uso_importe_original_de_esos"] = dict(Counter(str(o[i].get("uso_importe")) for i in rev_ids if i in o))

# Historial de correcciones
res["historial"] = {"registros": len(HC), "rango_fechas": [min(str(h["fecha"]) for h in HC), max(str(h["fecha"]) for h in HC)],
                    "por_hoja": dict(Counter(str(h["hoja"]) for h in HC).most_common()),
                    "por_campo_top": dict(Counter(f'{h["hoja"]}.{h["campo"]}' for h in HC).most_common(15))}
num_campos = {"cantidad", "precio_unitario", "subtotal_producto"}
res["historial"]["cambios_en_campos_numericos_detalle"] = sum(1 for h in HC if str(h["hoja"]) == "Detalle_Productos" and str(h["campo"]) in num_campos)

json.dump(res, open(os.path.join(OUT, "pm08_resultados.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(json.dumps(res, ensure_ascii=False, indent=1))
