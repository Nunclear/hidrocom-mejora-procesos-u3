"""Compara, celda por celda, el valor en caché de cada fórmula con el valor tras recalcular en Excel
(CalculateFullRebuild sobre una COPIA del libro) y lista todas las fórmulas.

Uso: python -P auditoria_formulas.py <carpeta_con_copias>   (contiene X.xlsx y recalc_X.xlsx)
Escribe formulas_inventario.csv y formulas_comparacion.txt en esta carpeta.
"""
import csv, os, sys, re
import openpyxl
sys.stdout.reconfigure(encoding="utf-8")
src = sys.argv[1]; OUT = os.path.dirname(os.path.abspath(__file__))
rows = []; resumen = []
for f in sorted(os.listdir(src)):
    if not f.endswith(".xlsx") or f.startswith("recalc_"):
        continue
    wf = openpyxl.load_workbook(os.path.join(src, f))
    wc = openpyxl.load_workbook(os.path.join(src, f), data_only=True)
    wr = openpyxl.load_workbook(os.path.join(src, "recalc_" + f), data_only=True)
    n = dif = vacias = 0; externos = 0; volatiles = 0; constantes_en_formula = 0
    for ws in wf:
        for row in ws.iter_rows():
            for c in row:
                if isinstance(c.value, str) and c.value.startswith("="):
                    n += 1
                    v0 = wc[ws.title][c.coordinate].value; v1 = wr[ws.title][c.coordinate].value
                    same = (v0 == v1) or (isinstance(v0, (int, float)) and isinstance(v1, (int, float)) and abs(v0 - v1) < 1e-9)
                    if not same: dif += 1
                    if v0 is None: vacias += 1
                    if "[" in c.value and ".xls" in c.value: externos += 1
                    if re.search(r"\b(NOW|TODAY|RAND|OFFSET|INDIRECT)\(", c.value): volatiles += 1
                    rows.append([f, ws.title, c.coordinate, c.value, v0, v1, "OK" if same else "DIFERENTE"])
    resumen.append(f"{f}: fórmulas={n} | caché≠recalculado={dif} | caché vacía={vacias} | refs externas={externos} | volátiles={volatiles}")
with open(os.path.join(OUT, "formulas_inventario.csv"), "w", newline="", encoding="utf-8-sig") as fh:
    w = csv.writer(fh); w.writerow(["libro", "hoja", "celda", "formula", "valor_cache", "valor_recalculado_excel", "dictamen"]); w.writerows(rows)
open(os.path.join(OUT, "formulas_comparacion.txt"), "w", encoding="utf-8").write("\n".join(resumen))
print("\n".join(resumen)); print("total fórmulas:", len(rows))
