"""Llena U3_Producto_Formato_DMAIC_UPeU.xlsx con el caso HIDROCOM KALLPA.
Uso: python llenar.py <plantilla.xlsx> <repo_dmaic.xlsx> <flujo.png> <salida.xlsx>"""
import sys
from collections import Counter
import openpyxl
from openpyxl.styles import Font, Alignment, PatternFill
from openpyxl.chart import BarChart, LineChart, Reference
from openpyxl.drawing.image import Image

tpl, src, png, out = sys.argv[1:5]
wb = openpyxl.load_workbook(tpl)
AM = PatternFill("solid", fgColor="FFFFF2CC")
NEG = Font(name="Calibri", size=10, color="FF000000")
WR = Alignment(wrap_text=True, vertical="top")

def put(ws, ref, val, fill=True, bold=False):
    c = ws[ref]
    c.value = val
    c.font = Font(name="Calibri", size=10, color="FF000000", bold=bold)
    c.alignment = WR
    if fill:
        c.fill = AM

# ---------- datos fuente (hoja Datos del Excel DMAIC del repo) ----------
s = openpyxl.load_workbook(src, data_only=True)["Datos"]
H = [c.value for c in s[5]]; ix = {h: i for i, h in enumerate(H)}
rows = [r for r in s.iter_rows(min_row=6, values_only=True) if r[0]]
g = lambda r, k: r[ix[k]]
E = lambda v: v is None or v == ""
NZ = lambda v: not E(v) and v != 0
U = len(rows)
uso = Counter(g(r, "uso_importe") for r in rows)
REV = uso["REVISAR"]
D = sum(E(g(r, "cantidad")) + E(g(r, "precio_unitario"))
        + (E(g(r, "subtotal_producto")) or NZ(g(r, "diferencia_importe"))) for r in rows)
ped = [r for r in rows if "PEDIDO" in (g(r, "estado_comprobante"), g(r, "estado_linea"))]
ped_rev = sum(g(r, "uso_importe") == "REVISAR" for r in ped)
num = [r for r in rows if E(g(r, "cantidad")) or E(g(r, "precio_unitario"))
       or E(g(r, "subtotal_producto")) or NZ(g(r, "diferencia_importe"))]
num_rev = sum(g(r, "uso_importe") == "REVISAR" for r in num)
est = [r for r in rows if g(r, "tipo_fecha") == "ESTIMADA"]; real = [r for r in rows if g(r, "tipo_fecha") == "REAL"]
r_est = sum(g(r, "uso_importe") == "REVISAR" for r in est); r_real = sum(g(r, "uso_importe") == "REVISAR" for r in real)
base_decl = sum(not E(g(r, "unidad_del_precio")) for r in rows)
assert (U, REV, D, len(ped), ped_rev, len(num), num_rev) == (262, 38, 35, 13, 13, 22, 21), (U, REV, D, len(ped), ped_rev, len(num), num_rev)
pct = lambda a, b: f"{a / b * 100:.2f}".replace(".", ",") + " %"

PROP = " [PROPUESTA — confirmar en DECISIONES.md]"
TEAM = "Gutierrez Morales Jhon Alex · Mullisaca Condori Carlos Augusto · Mamani Mamani Ciro Wagner"

# ---------- 0_Datos_y_Checklist ----------
ws = wb["0_Datos_y_Checklist"]
put(ws, "B6", "Reducción de renglones observados (REVISAR) en el registro y validación de notas de pedido")
put(ws, "B7", "GRUPO HIDROCOM KALLPA E.I.R.L. (Puno) · proceso de registro y validación de notas de pedido para información comercial")
put(ws, "B8", TEAM)
put(ws, "B9", "Gutierrez Morales Jhon Alex" + PROP)
put(ws, "B10", "Mullisaca Condori Carlos Augusto" + PROP)
put(ws, "B11", "Mamani Mamani Ciro Wagner" + PROP)
put(ws, "B12", "Titular / gerente de GRUPO HIDROCOM KALLPA E.I.R.L." + PROP)
put(ws, "B13", "26-11-2026")
checks = {18: "X", 19: "X", 20: "X", 21: "X", 22: "X", 23: "X", 24: "No aplica: sin serie temporal confiable (62 % fechas estimadas)",
          25: "X", 26: "X", 27: "X", 28: "X", 29: "X", 30: "X", 31: "X (simulación retrospectiva)", 32: "X", 33: "X", 34: "X"}
for r, v in checks.items():
    put(ws, f"E{r}", v, fill=False)

# ---------- D1 Charter ----------
ws = wb["D1_Project_Charter"]
put(ws, "A5", f"Los reportes comerciales de HIDROCOM se alimentan de las notas de pedido digitadas. En el lote revisado, {REV} de {U} renglones "
    f"({pct(REV, U)}) no pueden usarse sin revisión y cada uno exige volver al original (retrabajo). Mientras no se resuelvan, el importe "
    "publicado puede estar sub o sobreestimado y las decisiones de compra y reposición se toman con datos incompletos. CTQ: renglón completo y coherente para reporte.")
put(ws, "A9", f"El {pct(REV, U)} de los renglones de notas de pedido del lote revisado (corte 24-11-2026; {U} renglones, 69 notas con detalle) queda en estado "
    "REVISAR y no puede publicarse en los reportes comerciales sin retrabajo de verificación contra el documento original.")
put(ws, "A13", f"Reducir el % de renglones en estado REVISAR de {pct(REV, U)} a ≤ 5,00 % en el primer lote registrado con los nuevos controles "
    "(8 semanas desde la aprobación), medido como renglones REVISAR / renglones registrados." + PROP)
put(ws, "A16", "SÍ: desde la recepción de la nota de pedido (papel/imagen) hasta la publicación del renglón en los reportes comerciales "
    "(registro, validación, resolución de observaciones, aprobación de versión). NO: inventario físico, entregas/reparto, compras, "
    "evaluación de trabajadores, facturación electrónica.")
put(ws, "A19", "Champion: Gutierrez Morales Jhon Alex · Líder (BB): Mullisaca Condori Carlos Augusto · Analista (GB): Mamani Mamani Ciro Wagner · "
    "Dueño del proceso: titular/gerente de HIDROCOM KALLPA." + PROP)
put(ws, "A22", "D: 05-11 a 12-11 · M: 12-11 a 17-11 · A: 17-11 a 19-11 (avance con feedback 19-11) · I: 19-11 a 24-11 (simulación) · "
    "C: 24-11 a 26-11 (plan de control y presentación final 26-11-2026).")
put(ws, "A25", "Supuestos: el lote de 262 renglones representa el registro habitual; los originales siguen disponibles para resolver observaciones. "
    "Riesgos: 62 % de las fechas de emisión son estimadas o discordantes (no hay serie temporal); pertenencia del lote a la empresa por confirmar; "
    "costo hora y tiempos de revisión son supuestos, no medidos.")
put(ws, "A28", "Firma del Champion: ____________________  Fecha: ___/___/2026", fill=False)

# ---------- D2 5W2H ----------
ws = wb["D2_5W2H"]
for r, t in {
    5: f"{REV} de {U} renglones de notas de pedido quedan en REVISAR: no tienen dato confiable para el reporte comercial.",
    6: "Obliga a retrabajo (volver al original), retrasa la publicación y deja el importe comercial incierto para decidir compras y reposición.",
    7: "Proceso de registro y validación de notas de pedido: paso de transcripción y clasificación del estado de uso (antes de publicar en Data Mart / Power BI).",
    8: "Lote de notas fechadas del 27-01-2025 al 09-03-2026 (62 % con fecha estimada o discordante); el problema es transversal al lote, no de una campaña.",
    9: "Afecta a quien usa los reportes comerciales (gerencia, compras). Intervienen el emisor de la nota, quien digita y quien revisa/aprueba. Sin culpar personas.",
    10: f"Renglones con campos vacíos (5 sin cantidad, 16 sin precio, 9 sin importe), 5 importes que no cuadran y 13 renglones en estado PEDIDO sin regla.",
    11: "Estimado: 38 renglones × 10 min de revisión ≈ 6,3 h por lote ≈ S/ 47,50 por lote (supuesto S/ 7,50/h); además del riesgo de publicar importes errados (S/ 26 509,70 publicables en el lote).",
}.items():
    put(ws, f"C{r}", t)

# ---------- D3 SIPOC ----------
ws = wb["D3_SIPOC"]
sip = [
    ("Vendedor / emisor de la nota", "Nota de pedido (papel o imagen)", "1. Recibir e identificar la nota", "Nota con ID estable", "Registrador"),
    ("Cliente que hace el pedido", "Productos, cantidades, precios", "2. Registrar renglones (cantidad, precio, importe)", "Renglones digitados", "Revisor"),
    ("Responsable de catálogo", "Catálogo de productos y categorías", "3. Validar campos y estado (PEDIDO, anulado…)  ◄ AQUÍ VIVE EL DEFECTO", "Renglón DISPONIBLE / REVISAR / EXCLUIR", "Revisor / aprobador"),
    ("Custodio documental", "Original / imagen legible", "4. Resolver observaciones con evidencia", "Pendientes cerrados con evidencia", "Aprobador"),
    ("Aprobador", "Reglas de validación aprobadas", "5. Aprobar versión del lote", "Versión aprobada", "Publicador"),
    ("Data Mart (CSV) / auditoría", "Versión aprobada + huella (hash)", "6. Publicar y conciliar en reportes", "Reporte comercial confiable", "Gerencia y compras"),
]
for i, row in enumerate(sip):
    for j, v in enumerate(row):
        put(ws, f"{'ABCDE'[j]}{5 + i}", v)
ws.column_dimensions["C"].width = 44

# ---------- M1 Flujo ----------
ws = wb["M1_Flujo_SwimLane"]
for r in range(6, 10):
    put(ws, f"D{r}", "✔", fill=False)
img = Image(png); img.width, img.height = 1100, 497
ws.add_image(img, "A12")
put(ws, "A40", "Nota: flujo reconstruido a partir de los archivos del lote (Comprobantes, Data Mart, auditoría). Debe validarse observando el registro real en la empresa (Gemba).", fill=False)

# ---------- M2 Línea base ----------
ws = wb["M2_LineaBase_Sigma"]
put(ws, "B5", "CTQ propuesto para el análisis del lote (pendiente de aprobación): renglón completo y coherente (cantidad presente, precio presente, importe presente y = cantidad × precio / base). Y secundario: % renglones REVISAR = 14,50 %.")
put(ws, "B6", "Comprobantes_Revisados.xlsx (hoja Detalle_Productos) + Data Mart CSV; copia en 03_DMAIC/U3_DMAIC_HIDROCOM.xlsx, hoja Datos.")
put(ws, "B7", "Lote documental 27-01-2025 a 09-03-2026, corte de revisión 24-11-2026")
put(ws, "B8", U); put(ws, "B9", D); put(ws, "B10", 3)
put(ws, "A15", f"Bajo la regla CTQ propuesta, la línea base del lote es ≈ 3,20 σ (DPMO ≈ 44 529): en {U} renglones × 3 oportunidades hubo {D} defectos (16 precios vacíos, 9 importes vacíos, "
    f"5 cantidades vacías, 5 importes incoherentes) en {len(num)} renglones. Cae entre 3σ (66 807) y 3,5σ (22 750) de la Tabla_Sigma: de cada 1 000 datos "
    "críticos digitados, ~45 no sirven para el reporte. Para el cliente interno (gerencia) significa que 1 de cada 12 renglones no es confiable.")

# ---------- A1 Pareto ----------
ws = wb["A1_Pareto"]
par = [("Estado PEDIDO sin regla de inclusión", 13), ("Campos numéricos incompletos (cantidad/precio/importe)", 7),
       ("Observación o lectura dudosa documentada", 7), ("Motivo no explicitado en el detalle", 6),
       ("Diferencia de importe consignada en la fuente", 5)]
for i, (k, v) in enumerate(par):
    put(ws, f"A{5 + i}", k); put(ws, f"B{5 + i}", v)
ws.column_dimensions["A"].width = 50
put(ws, "B15", "Estado PEDIDO, campos incompletos y observación dudosa concentran el 71,05 % de los 38 REVISAR (27 de 38). "
    "Sumando 'campos incompletos' + 'diferencia de importe' (mismo origen: captura sin validación numérica) los dos vitales PEDIDO + captura numérica "
    "explican 25 de 38 (65,8 %). A ellos va el Ishikawa. No atacamos por ahora 'motivo no explicitado' (requiere originales).")
ws._charts = []
bar = BarChart(); bar.type = "col"; bar.title = "Pareto de renglones REVISAR (n = 38)"
bar.y_axis.title = "Renglones"; bar.x_axis.title = None
bar.add_data(Reference(ws, min_col=2, min_row=4, max_row=9), titles_from_data=True)
bar.set_categories(Reference(ws, min_col=1, min_row=5, max_row=9))
bar.y_axis.majorGridlines = None
line = LineChart()
line.add_data(Reference(ws, min_col=4, min_row=4, max_row=9), titles_from_data=True)
line.y_axis.axId = 200;line.y_axis.number_format = "0%"
line.y_axis.scaling.min = 0; line.y_axis.scaling.max = 1; line.y_axis.crosses = "max"
for ax_ in (bar.x_axis, bar.y_axis, line.y_axis, line.x_axis):
    ax_.delete = False
line.x_axis = bar.x_axis
line.series[0].graphicalProperties.line.solidFill = "C00000"
line.series[0].graphicalProperties.line.width = 28000
line.series[0].marker.symbol = "circle"
bar.series[0].graphicalProperties.solidFill = "003264"
bar.legend.position = "b"
bar += line
bar.height, bar.width = 9, 20
ws.add_chart(bar, "F4")

# ---------- A2 Ishikawa + verificación ----------
ws = wb["A2_Ishikawa_Verificacion"]
ish = {5: ("Criterio distinto entre quienes digitan para marcar REVISAR/EXCLUIR", "Sin capacitación escrita sobre campos obligatorios"),
       6: ("No existe regla escrita para el estado PEDIDO (¿se publica o no?)", "No se exige motivo al marcar REVISAR/EXCLUIR"),
       7: ("Hoja Excel de captura sin validación (permite dejar vacíos)", "Sin control de versión entre Excel y Data Mart (hash distinto)"),
       8: ("Notas en papel ilegibles o tachadas (12 tachadas, 3 anuladas)", "Base de precio no indicada en la nota (por unidad, kg o millar)"),
       9: ("CTQ y definición de defecto no acordados antes del registro", "Fechas estimadas (62 %) impiden medir por periodo"),
       10: ("Registro hecho en lote, tiempo después de la venta", "Interrupciones durante la digitación en tienda")}
for r, (a, b) in ish.items():
    put(ws, f"B{r}", a); put(ws, f"C{r}", b)
ver = [
    ("1. No existe regla escrita para el estado PEDIDO (Método)",
     "Hoja Datos: renglones con estado PEDIDO en nota o renglón vs. uso_importe",
     f"{ped_rev} de {len(ped)} renglones PEDIDO (100 %) terminan en REVISAR; son el 34,2 % de todos los REVISAR. Sin regla, todo PEDIDO se va a la cola.", "RESPALDADA por la evidencia documental del lote"),
    ("2. Captura sin validación de campos numéricos (Máquina/Sistema)",
     "Hoja Datos: vacíos en cantidad/precio/importe y diferencia_importe ≠ 0",
     f"{len(num)} renglones con ≥1 defecto numérico ({D} defectos); {num_rev} de ellos ({num_rev / len(num) * 100:.0f} %) están en REVISAR. La hoja permitió guardarlos.", "RESPALDADA por la evidencia documental del lote"),
    ("3. Las fechas estimadas generan renglones REVISAR (Medición)",
     "Hoja Datos: tasa REVISAR según tipo_fecha",
     f"REVISAR con fecha estimada: {r_est}/{len(est)} = {r_est / len(est) * 100:.1f} %; con fecha real: {r_real}/{len(real)} = {r_real / len(real) * 100:.1f} %. "
     "Comparación descriptiva: diferencia pequeña; no respalda priorizar la fecha. Verificación operativa pendiente.", "NO RESPALDADA (descriptivo)"),
    ("4. Base de precio no indicada (Material)",
     "Hoja Datos: unidad_del_precio declarada; diferencias de importe",
     f"Solo {base_decl} de {U} renglones declaran base; explica 1 de las 5 diferencias (NP-025138-01, millar). Causa contribuyente, no principal.", "PARCIAL"),
]
for i, row in enumerate(ver):
    for j, v in enumerate(row):
        put(ws, f"{'ABCD'[j]}{15 + i}", v)
put(ws, "A20", "5 porqués (vital PEDIDO): ¿Por qué hay REVISAR? → hay renglones PEDIDO → ¿por qué van a REVISAR? → nadie sabe si se publican → "
    "¿por qué? → no hay regla escrita → ¿por qué? → el proceso de registro nunca se estandarizó → ¿por qué? → no hay dueño del proceso que apruebe criterios.", fill=False)
put(ws, "A22", "CAUSA RAÍZ (confirmada con la evidencia documental del lote; verificación operativa pendiente del piloto): el registro no tiene reglas estandarizadas de captura y clasificación (sin regla para PEDIDO y sin campos obligatorios "
    f"validados), porque los datos del lote muestran que el estado PEDIDO y las incidencias numéricas se asocian con 25 de los 38 renglones REVISAR (65,8 %): "
    f"el 100 % de los PEDIDO y {num_rev} de {len(num)} renglones con defecto numérico están en REVISAR.", fill=False, bold=True)
ws.column_dimensions["B"].width = 48; ws.column_dimensions["C"].width = 48

# ---------- I1 Ideas + matriz ----------
ws = wb["I1_Ideas_Matriz"]
ideas = [("Regla escrita del estado PEDIDO (no publicable hasta confirmar venta) con estado propio", "C1 Método: sin regla PEDIDO", 5, 1),
         ("Poka-Yoke: validación de datos en la hoja de captura (cantidad, precio, importe obligatorios y coherentes)", "C2 Sistema: captura sin validación", 5, 2),
         ("Motivo obligatorio (lista desplegable) al marcar REVISAR o EXCLUIR", "Motivo no explicitado (6)", 4, 1),
         ("Campo 'base de precio' (unidad/kg/millar) obligatorio", "C4 Material: base no indicada", 3, 2),
         ("Evidencia y aprobación registradas al cerrar cada pendiente", "Cierres sin fundamento", 3, 2),
         ("Catálogo estable de productos y categorías (lista cerrada)", "Categorías distintas entre capas", 3, 3),
         ("5S digital: carpetas originales / trabajo / publicado con nombres estándar", "Desorden documental", 2, 2),
         ("Kaizen semanal de 15 min sobre la cola REVISAR", "Sostener la mejora", 3, 2)]
for i, (a, b, im, es) in enumerate(ideas):
    put(ws, f"B{5 + i}", a); put(ws, f"C{5 + i}", b); put(ws, f"D{5 + i}", im); put(ws, f"E{5 + i}", es)
ws.column_dimensions["B"].width = 55; ws.column_dimensions["C"].width = 32
put(ws, "D14", "Elegidas: 1 (prioridad 25), 2 y 3 (20 c/u). La idea 2 es un Poka-Yoke de PREVENCIÓN (validación de datos que impide guardar vacíos o importes "
    "incoherentes); la idea 3 es Poka-Yoke de DETECCIÓN (lista obligatoria). Se sostienen con 5S digital (idea 7) y Kaizen (idea 8). Puntajes" + PROP)

# ---------- I2 PDCA ----------
ws = wb["I2_Plan_Accion"]
pdca = [("P · Redactar y aprobar la regla del estado PEDIDO y la lista de motivos", "Mullisaca C. (BB) + dueño del proceso", "26-11-2026", "% REVISAR por PEDIDO", "13 → 0 renglones", "P (hecho en borrador)"),
        ("H · Configurar validación de datos en la hoja de captura (Poka-Yoke, hoja Validar)", "Mamani C. (GB)", "03-12-2026", "Defectos numéricos (D)", "35 → ≤ 5", "H (prototipo listo)"),
        ("H · Simular los controles sobre los 262 renglones del lote", "Equipo", "24-11-2026", "% REVISAR", "14,50 % → 4,96 %", "V (simulado)"),
        ("V · Piloto real: registrar 1 lote nuevo con los controles y medir", "Dueño del proceso + BB", "Ene-2027", "% REVISAR y DPMO", "14,50 % → ≤ 5 %", "Pendiente"),
        ("A · Estandarizar: instructivo de 1 página + plantilla bloqueada", "Gutierrez J. (Champion)", "Ene-2027", "Cumplimiento del instructivo", "— → 100 % lotes", "Pendiente")]
for i, row in enumerate(pdca):
    for j, v in enumerate(row):
        put(ws, f"{'ABCDEF'[j]}{5 + i}", v)
ws.column_dimensions["A"].width = 52
put(ws, "A13", f"SIMULACIÓN RETROSPECTIVA (prueba de escritorio, no piloto en campo): aplicamos los controles a los {U} renglones del lote. "
    f"La regla PEDIDO reclasifica automáticamente los 13 PEDIDO (dejan de ir a REVISAR); la validación numérica habría bloqueado en la captura los "
    "12 REVISAR por campos vacíos o importe incoherente (7 + 5), obligando a corregir contra el original en el momento. Quedan 13 REVISAR "
    "(observación dudosa 7 + motivo no explicitado 6), ahora con motivo obligatorio. Resultado: REVISAR pasa de 38/262 = 14,50 % a 13/262 = 4,96 % "
    "(−65,8 %) y el DPMO del CTQ bajaría de ≈ 44 529 a ≈ 0 en datos guardados. Límite: supone que el registrador corrige con el original; falta el piloto real.")

# ---------- C1 Control ----------
ws = wb["C1_Plan_Control"]
kpis = [("% renglones REVISAR por lote", "≤ 5,00 %", "COUNTIF(uso_importe='REVISAR') / renglones del lote (hoja de captura)", "Por lote (semanal)", "Dueño del proceso", "> 7 % en un lote o > 5 % dos lotes seguidos", "Kaizen de 15 min: Pareto de motivos y ajuste de la regla"),
        ("DPMO del CTQ (renglón completo y coherente)", "≤ 6 210 (≥ 4σ)", "Vacíos + importes incoherentes / (renglones × 3) × 10^6", "Mensual", "Líder BB", "> 22 750 (< 3,5σ)", "Revisar que la validación de datos siga activa (no desbloqueada)"),
        ("% renglones REVISAR/EXCLUIR con motivo", "100 %", "Celdas 'motivo' llenas / renglones REVISAR+EXCLUIR", "Por lote", "Analista GB", "< 100 %", "Devolver el lote al registrador antes de publicar"),
        ("% publicaciones conciliadas (hash Excel = hash Data Mart)", "100 %", "auditoria.json vs. hash del archivo publicado", "Por publicación", "Champion", "Cualquier desalineación", "Bloquear la publicación y reprocesar la versión aprobada")]
for i, row in enumerate(kpis):
    for j, v in enumerate(row):
        put(ws, f"{'ABCDEFG'[j]}{5 + i}", v)
put(ws, "H5", None, fill=False)
put(ws, "A11", "Estandarización (Seiketsu): instructivo de 1 página con la regla PEDIDO y los campos obligatorios; plantilla de captura con validación de datos y hojas "
    "protegidas; lista de motivos cerrada; carpetas 5S originales/trabajo/publicado. AUTOMATIZACIÓN posible: formato condicional que pinta en rojo el renglón "
    "incompleto; columna 'Estado' calculada (hoja Validar); script que compara el hash antes de publicar; tarjeta de Power BI con % REVISAR y alerta si > 5 %.", fill=False)

# ---------- C2 Beneficios ----------
ws = wb["C2_Beneficios_Lecciones"]
vol, mins, ch = 1, 10, 7.5   # lotes/mes, min por renglón REVISAR, S/ por hora
antes = round(REV * mins / 60 * ch * vol, 2); despues = round(13 * mins / 60 * ch * vol, 2)
put(ws, "B5", antes); put(ws, "B6", despues); put(ws, "B7", 120)
put(ws, "A11", f"Supuestos (todos por validar con el dueño del proceso): 1 lote de ~{U} renglones por mes; 10 min para resolver cada renglón REVISAR contra el original; "
    "costo hora del asistente S/ 7,50 (≈ remuneración mínima mensual / 150 h). ANTES = 38 × 10/60 × 7,50 = S/ 47,50/mes; DESPUÉS = 13 × 10/60 × 7,50 = S/ 16,25/mes "
    "(resultado de la simulación). Costo de implementar = 16 h del equipo × S/ 7,50 = S/ 120 (configurar validación, instructivo, capacitación). "
    "Beneficio anual neto estimado en el ESCENARIO BASE: S/ 255. Beneficio modesto y defendible (horas liberadas, no caja directa); el beneficio mayor —no cuantificado— es evitar publicar importes errados sobre S/ 26 509,70 del lote.")
lec = ["Técnica: definir el CTQ y la unidad ANTES de contar; 151 'incidencias' no eran 151 defectos y casi nos llevan a un DPMO falso.",
       "Técnica: el Pareto con regla de clasificación exclusiva evita doble conteo; comparar con datos mostró que una causa que parecía obvia (fechas estimadas) no estaba respaldada.",
       "Equipo: separar hallazgos de supuestos y dejar decisiones con dueño (DECISIONES.md); si empezáramos de nuevo, iríamos antes al Gemba a cronometrar el registro."]
for i, t in enumerate(lec):
    put(ws, f"B{16 + i}", t)
ws.column_dimensions["B"].width = 90

# =====================================================================================
# v2 · Contrato de datos del issue #1 (comentarios 7146745531 y 7146867353)
#   Q4: principal D = 30 (completitud sintáctica exploratoria; no CTQ aprobado);
#       D = 34 / 35 = sensibilidad separada; NP-025138-01 conserva su incidencia.
#   Q5: roles por función, nombres pendientes; meta y puntajes NO aprobados.
#   PM-02/03/04: causa candidata; simulación en rango; beneficio en escenarios.
#   C5: hoja Datos + fórmulas vivas (U, D, Pareto).
# =====================================================================================
from openpyxl.utils import get_column_letter
NA = " [PROPUESTA NO APROBADA — ver DECISIONES.md]"
PEND = "Pendiente de designación nominal"

# ---------- Hoja Datos (copia literal de 03_DMAIC › Datos) + columna derivada ----------
wd = wb.create_sheet("Datos")
wd.append(H + ["condicion_principal (derivada)"])
for r in rows:
    wd.append(list(r))
n = len(rows); last = n + 1
for i in range(2, last + 1):
    wd[f"Y{i}"] = (f'=IF(T{i}<>"REVISAR","",IF(OR(R{i}="PEDIDO",S{i}="PEDIDO"),"Estado PEDIDO sin regla de inclusión",'
                   f'IF(OR(I{i}="",K{i}="",L{i}=""),"Campos numéricos incompletos (cantidad/precio/importe)",'
                   f'IF(AND(V{i}<>"",V{i}<>0),"Diferencia de importe consignada en la fuente",'
                   f'IF(OR(W{i}<>"",S{i}="DUDOSA"),"Observación o lectura dudosa documentada","Motivo no explicitado en el detalle")))))')
for c in wd[1]:
    c.font = Font(bold=True, color="FFFFFFFF"); c.fill = PatternFill("solid", fgColor="FF003264")
wd.freeze_panes = "A2"
for i in range(2, last + 1):
    wd[f"C{i}"].number_format = "dd/mm/yyyy"
R_ = lambda col: f"Datos!${col}$2:${col}${last}"

# ---------- 0 y D1: roles por función (Q5) ----------
ws = wb["0_Datos_y_Checklist"]
put(ws, "B9", PEND + " (función: patrocina, aprueba alcance y recursos)")
put(ws, "B10", PEND + " (función: lidera medición, análisis y pruebas)")
put(ws, "B11", PEND + " (función: reproduce conteos y documenta contrastes)")
put(ws, "B12", PEND + " (función: aprueba CTQ, excepciones y estándar; persona de HIDROCOM)")
put(ws, "E24", "No aplica: sin orden temporal confiable (45/73 notas = 61,64 % con fecha estimada o año discordante)", fill=False)
ws = wb["D1_Project_Charter"]
put(ws, "A13", "Meta candidata: reducir el % de renglones REVISAR de 14,50 % a ≤ 5,00 % en el primer lote con controles (8 semanas)." + NA)
put(ws, "A19", "Integrantes del equipo (manual): " + TEAM + ". Champion, líder, analista y dueño del proceso: " + PEND +
    ". El manual no acredita esa asignación ni certificaciones de cinturón.")
put(ws, "A25", "Supuestos: los originales siguen disponibles para resolver observaciones. Riesgos: procedencia del lote sin confirmar (70 de 73 notas tienen "
    "fecha anterior al inicio de actividades reportado, 09/03/2026); 45/73 notas = 61,64 % con fecha estimada o año discordante (no hay serie temporal); "
    "tiempos, costos y volumen no medidos. Alcance: diagnóstico de un lote documental, no desempeño empresarial actual.")
ws = wb["D2_5W2H"]
put(ws, "C8", "Lote de notas fechadas del 27-01-2025 al 09-03-2026 (45/73 notas = 61,64 % con fecha estimada o año discordante); procedencia por confirmar.")
put(ws, "C11", "No medido. Escenario con supuestos (hoja C2): 38 renglones × 10 min × S/ 7,50/h ≈ S/ 47,50 por lote. El importe DISPONIBLE del lote "
    "(S/ 26 509,70) es documental, no ventas ni costo de mala calidad.")

# ---------- M2: principal D = 30 con fórmulas vivas + sensibilidad ----------
ws = wb["M2_LineaBase_Sigma"]
put(ws, "B5", "Completitud sintáctica exploratoria: celdas nulas en cantidad, precio e importe (3 campos por renglón). NO es un CTQ aprobado ni un nivel "
    "sigma empresarial. Indicador descriptivo aparte: % renglones REVISAR = 14,50 % (estado documental, no defecto).")
put(ws, "B6", "03_DMAIC/U3_DMAIC_HIDROCOM.xlsx › Datos (= Comprobantes_Revisados.xlsx › Detalle_Productos, 0 celdas distintas, SHA-256 ac6ab323…). Copia en la hoja Datos de este libro.")
ws["B8"] = f'=COUNTA({R_("A")})'
ws["B9"] = f'=COUNTBLANK({R_("I")})+COUNTBLANK({R_("K")})+COUNTBLANK({R_("L")})'
ws["B10"] = 3
for c in ("B8", "B9", "B10"):
    ws[c].fill = AM; ws[c].font = NEG
put(ws, "A15", "Bajo la regla de completitud sintáctica, el lote tiene 30 celdas nulas en 786 campos: 38 167,94 por millón y sigma equivalente ≈ 3,27 "
    "(convención +1,5). Es un descriptor de la tabla, no del desempeño de HIDROCOM: 17 de 262 renglones tienen al menos un campo vacío; un campo lleno "
    "no significa dato correcto y un vacío puede ser una excepción legítima.")
put(ws, "A19", "Sensibilidad (análisis separados; ningún criterio es CTQ aprobado)", fill=False, bold=True)
hdr = ["Criterio", "U", "D", "U × O", "DPMO", "σ equivalente (+1,5)"]
for j, h_ in enumerate(hdr):
    c = ws.cell(row=20, column=1 + j, value=h_); c.font = Font(bold=True, color="FFFFFFFF"); c.fill = PatternFill("solid", fgColor="FF003264")
L_, V_, M_, T_ = R_("L"), R_("V"), R_("M"), R_("T")
dif = f'SUMPRODUCT(({L_}<>"")*({V_}<>"")*({V_}<>0))'
dif_millar = f'SUMPRODUCT(({L_}<>"")*({V_}<>"")*({V_}<>0)*({M_}="millar"))'
blank_sin_ex = (f'SUMPRODUCT(({T_}<>"EXCLUIR")*({R_("I")}=""))+SUMPRODUCT(({T_}<>"EXCLUIR")*({R_("K")}=""))'
                f'+SUMPRODUCT(({T_}<>"EXCLUIR")*({L_}=""))')
sens = [("D = 30 · solo vacíos, todo el lote (PRINCIPAL)", "=B8", "=B9"),
        ("D = 27 · solo vacíos, sin EXCLUIR", f'=COUNTIFS({T_},"<>EXCLUIR")', "=" + blank_sin_ex),
        ("D = 35 · vacíos + 5 diferencias de importe (regla de coherencia)", "=B8", "=B9+" + dif),
        ("D = 34 · como D = 35 sin NP-025138-01 (base «millar» ambigua: escenario, la incidencia se conserva)", "=B8", "=B9+" + dif + "-" + dif_millar)]
for k, (lab, u, d) in enumerate(sens):
    r = 21 + k
    put(ws, f"A{r}", lab, fill=False)
    ws[f"B{r}"] = u; ws[f"C{r}"] = d; ws[f"D{r}"] = f"=B{r}*3"
    ws[f"E{r}"] = f"=C{r}/D{r}*1000000"; ws[f"F{r}"] = f"=NORMSINV(1-E{r}/1000000)+1.5"
    ws[f"E{r}"].number_format = "#,##0.00"; ws[f"F{r}"].number_format = "0.0000"
put(ws, "A26", "Notas de medición: 73 notas en Comprobantes, 69 con renglones (4 sin detalle: NP-025111, -127, -137, -140). % REVISAR = 38/262 = 14,50 %; "
    "IC 95 % de Wilson NOMINAL 10,75–19,28 % (supone renglones independientes; ICC intra-nota 0,246, efecto de diseño 1,69). El censo del lote no "
    "acredita representatividad empresarial.", fill=False)
ws.column_dimensions["A"].width = 62

# ---------- A1: Pareto vivo desde Datos ----------
ws = wb["A1_Pareto"]
for i in range(5, 10):
    ws[f"B{i}"] = f'=COUNTIF({R_("Y")},A{i})'
    ws[f"B{i}"].fill = AM; ws[f"B{i}"].font = NEG
put(ws, "B15", "Regla exclusiva por prioridad (PEDIDO > vacíos > diferencia > observación > resto; columna Datos!Y). Las tres primeras categorías "
    "suman 27 de 38 (71,05 %). Son CONDICIONES DOCUMENTALES de la clasificación del lote, no causas: el orden de prioridad cambia sus tamaños.")

# ---------- A2: condición documental, asociación y causa candidata (PM-02) ----------
ws = wb["A2_Ishikawa_Verificacion"]
put(ws, "C7", "Versiones distintas del Data Mart circulan sin identificar (AUD-012)")
put(ws, "C9", "45/73 notas (61,64 %) con fecha estimada o año discordante impiden medir por periodo")
put(ws, "D14", "Tipo de evidencia", fill=False)
veredictos = ["Condición documental confirmada [H]; asociación POR CONSTRUCCIÓN (el estado REVISAR se asignó por esta condición): NO prueba causa",
              "Condición documental confirmada [H]; asociación POR CONSTRUCCIÓN: NO prueba causa",
              "Comparación descriptiva (Fisher p = 0,47, n efectivo ≈ 155): sin evidencia para priorizarla; no se descarta",
              "Ambigüedad documentada (1 de 5 diferencias depende de la base); por resolver con el original"]
for i, v in enumerate(veredictos):
    put(ws, f"D{15 + i}", v)
put(ws, "A20", "5 porqués (HIPÓTESIS por verificar en el registro real): ¿Por qué hay REVISAR? → hay renglones PEDIDO y con datos vacíos → ¿por qué? → "
    "no hay regla escrita para PEDIDO ni campos obligatorios en la captura (causa candidata) → ¿por qué? → el registro no se ha estandarizado (por verificar).", fill=False)
put(ws, "A22", "CONCLUSIÓN: los datos del lote NO permiten verificar una causa raíz operativa. El estado PEDIDO y las incidencias numéricas son condiciones "
    "documentales que la clasificación asocia por construcción a 25 de los 38 REVISAR (13 PEDIDO, 21 numéricos, 9 con ambas). CAUSA CANDIDATA: ausencia de "
    "reglas de captura y clasificación; se verificará observando el registro real y comparando la captura original con la revisada (PM-08).", fill=False, bold=True)

# ---------- I1 / I2: puntajes no aprobados, responsables por función, simulación en rango ----------
ws = wb["I1_Ideas_Matriz"]
put(ws, "D14", "Selección candidata: 1 (prioridad 25), 2 y 3 (20 c/u). La idea 2 es un Poka-Yoke de PREVENCIÓN; la 3, de DETECCIÓN; se sostienen con "
    "5S digital (7) y Kaizen (8). Los puntajes son una propuesta de trabajo" + NA)
ws = wb["I2_Plan_Accion"]
for r_, resp in zip(range(5, 10), ["Líder del proyecto + dueño del proceso (pendientes)", "Analista (pendiente)", "Equipo",
                                   "Dueño del proceso + líder (pendientes)", "Champion (pendiente)"]):
    put(ws, f"B{r_}", resp)
put(ws, "E7", "14,50 % → 4,96–12,12 % (escenarios)")
put(ws, "A13", "SIMULACIÓN RETROSPECTIVA DECLARADA (no es piloto): si las reglas resolvieran los 25 REVISAR asociados a PEDIDO o a incidencias numéricas "
    "con una eficacia e, quedarían 38 − 25·e renglones. Tabla de escenarios abajo (la eficacia es un supuesto, no una observación). El máximo teórico "
    "(e = 100 %) da 4,96 %. Límites: supone que el registrador corrige con el original; la clasificación es la del lote; falta el piloto.")
put(ws, "A17", "Eficacia supuesta (e)", fill=False, bold=True); put(ws, "B17", "REVISAR restantes", fill=False, bold=True); put(ws, "C17", "% REVISAR", fill=False, bold=True)
for k, e in enumerate([1, 0.75, 0.5, 0.25]):
    r = 18 + k
    ws[f"A{r}"] = e; ws[f"A{r}"].number_format = "0%"
    ws[f"B{r}"] = f"=38-25*A{r}"; ws[f"C{r}"] = f"=B{r}/262"; ws[f"C{r}"].number_format = "0.00%"

# ---------- C2: beneficio en escenarios (PM-04) ----------
ws = wb["C2_Beneficios_Lecciones"]
put(ws, "A11", "Escenario BASE de la plantilla (B5:B8): 1 lote de ~262 renglones por mes (38 REVISAR/mes), 10 min por renglón y S/ 7,50/h → S/ 47,50 antes y "
    "S/ 16,25 después; costo de implementar S/ 120 (16 h) → S/ 255/año. TODO es supuesto, no medición: el volumen derivado del rango de fechas (13,3 meses) "
    "tampoco mide la cadencia real. Ver la tabla de escenarios (filas 20–28; igual al modelo de B, Modelo_Costo_Beneficio_HIDROCOM.json, 3b3da11): con volumen bajo el resultado es negativo y se conserva.")
put(ws, "A20", "Escenarios (S/; supuestos editables)", fill=False, bold=True)
hdr = ["Escenario", "REVISAR/mes", "Eficacia e", "Min/renglón", "S/ por hora", "Costo inicial (costo recurrente: no estimado)", "Beneficio anual neto"]
for j, h_ in enumerate(hdr):
    c = ws.cell(row=21, column=1 + j, value=h_); c.font = Font(bold=True, color="FFFFFFFF"); c.fill = PatternFill("solid", fgColor="FF003264")
esc = [("Base: 1 lote/mes, eficacia máxima", 38, 1), ("Eficacia 75 %", 38, 0.75), ("Eficacia 50 %", 38, 0.5), ("Eficacia 25 %", 38, 0.25),
       ("Eficacia 0 %", 38, 0), ("Volumen bajo: 1 lote en 13,3 meses", "=38/13.3", 1),
       ("Punto de equilibrio (REVISAR iniciales/mes)", "=F28/((25/38)*D28/60*E28*12)", 1)]
for k, (lab, rv, e) in enumerate(esc):
    r = 22 + k
    put(ws, f"A{r}", lab, fill=False)
    ws[f"B{r}"] = rv; ws[f"C{r}"] = e; ws[f"D{r}"] = 10; ws[f"E{r}"] = 7.5; ws[f"F{r}"] = 120
    ws[f"G{r}"] = f"=B{r}*(25/38)*C{r}*D{r}/60*E{r}*12-F{r}"
    for col in "BCDEF":
        ws[f"{col}{r}"].fill = AM
    ws[f"B{r}"].number_format = "0.00"; ws[f"G{r}"].number_format = "#,##0.00"; ws[f"C{r}"].number_format = "0%"
put(ws, "B16", "Técnica: definir el criterio de defecto y la unidad ANTES de contar; 151 «incidencias» no eran 151 defectos, y 30, 34 o 35 «defectos» "
    "dependen de la regla elegida.")
put(ws, "B17", "Técnica: una asociación creada por la propia clasificación (13/13, 21/22) no verifica causas; las fechas estimadas no mostraron diferencia "
    "relevante con los datos disponibles (descriptivo).")
for nm in ("C2_Beneficios_Lecciones",):
    wb[nm].column_dimensions["A"].width = 46

wb.save(out)
print("ok", out, "U", U, "D", D, "antes", antes, "despues", despues)
