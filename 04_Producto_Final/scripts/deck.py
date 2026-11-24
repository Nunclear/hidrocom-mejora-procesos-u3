"""Llena U3_Producto_Plantilla_Presentacion_UPeU.pptx con el caso HIDROCOM.
Uso: python deck.py <plantilla.pptx> <carpeta_04_Producto_Final> <salida.pptx>"""
import sys, os, copy
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE, XL_LEGEND_POSITION, XL_LABEL_POSITION
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.oxml.ns import qn
from lxml import etree

tpl, folder, out = sys.argv[1:4]
prs = Presentation(tpl)
NAVY, GOLD, RED, TEAL, INK, MUTED = "003264", "F3C133", "C00000", "005E80", "1F2937", "5B6472"
rgb = RGBColor.from_string

# ---------- utilidades ----------
def shp(slide, sid):
    for s in slide.shapes:
        if s.shape_id == sid:
            return s
    raise KeyError(sid)

def remove(*shapes):
    for s in shapes:
        s._element.getparent().remove(s._element)

def write(shape, paras, size=11, anchor=None):
    """paras: lista de párrafos; cada párrafo es str o lista de (texto, {bold,color,size,italic})."""
    tf = shape.text_frame
    tf.word_wrap = True
    if anchor is not None:
        tf.vertical_anchor = anchor
    for p in list(tf.paragraphs)[1:]:
        p._p.getparent().remove(p._p)
    first = tf.paragraphs[0]
    kept_ppr = False
    for ch in list(first._p):
        if ch.tag == qn("a:pPr") and not kept_ppr:
            kept_ppr = True
            continue
        if ch.tag != qn("a:endParaRPr"):
            first._p.remove(ch)   # runs, saltos y pPr duplicados de la plantilla
    for i, para in enumerate(paras):
        p = first if i == 0 else tf.add_paragraph()
        p.alignment = PP_ALIGN.LEFT
        p.space_after = Pt(3)
        runs = [(para, {})] if isinstance(para, str) else para
        for text, st in runs:
            r = p.add_run(); r.text = text
            f = r.font; f.name = "Calibri"; f.size = Pt(st.get("size", size))
            f.bold = st.get("bold", False); f.italic = st.get("italic", False)
            f.color.rgb = rgb(st.get("color", INK))

def card(rect, fill="F4F7FB", line="C9D4E3"):
    """Convierte el recuadro punteado [EQUIPO] en tarjeta sólida."""
    sp = rect._element.spPr
    for tag in ("a:solidFill", "a:ln"):
        for e in sp.findall(qn(tag)):
            sp.remove(e)
    rect.fill.solid(); rect.fill.fore_color.rgb = rgb(fill)
    rect.line.color.rgb = rgb(line); rect.line.width = Pt(1)

L = lambda t, c=NAVY: (t, {"bold": True, "color": c, "size": 10.5})  # etiqueta
B = lambda t, **k: (t, k)

def key(slide, rect_id, text_id, msg):
    write(shp(slide, text_id), [[("Mensaje clave: ", {"bold": True, "color": TEAL, "size": 10.5}), (msg, {"italic": True, "size": 10.5})]],
          anchor=MSO_ANCHOR.MIDDLE)

def table(slide, x, y, w, h, data, widths, size=9, head_fill=NAVY, hl_rows=(), hl_fill="FDE2E2"):
    gf = slide.shapes.add_table(len(data), len(data[0]), Inches(x), Inches(y), Inches(w), Inches(h))
    t = gf.table
    tblPr = t._tbl.tblPr
    tblPr.set("bandRow", "0"); tblPr.set("firstRow", "1")
    for j, cw in enumerate(widths):
        t.columns[j].width = Inches(cw)
    for i, row in enumerate(data):
        for j, val in enumerate(row):
            c = t.cell(i, j)
            c.margin_left = c.margin_right = Inches(0.05); c.margin_top = c.margin_bottom = Inches(0.03)
            c.fill.solid()
            c.fill.fore_color.rgb = rgb(head_fill if i == 0 else (hl_fill if i in hl_rows else ("FFFFFF" if i % 2 else "F4F7FB")))
            tf = c.text_frame; tf.word_wrap = True
            p = tf.paragraphs[0]; p.text = ""
            r = p.add_run(); r.text = str(val)
            r.font.name = "Calibri"; r.font.size = Pt(size); r.font.bold = (i == 0 or (j == 0 and len(row) == 2))
            r.font.color.rgb = rgb("FFFFFF" if i == 0 else (RED if i in hl_rows else INK))
    hh = min(0.32, h / len(data))
    t.rows[0].height = Inches(hh)
    for i in range(1, len(data)):
        t.rows[i].height = Inches((h - hh) / (len(data) - 1))
    return gf

def picture(slide, path, x, y, w, h):
    """Inserta la imagen ajustada dentro de la caja (x, y, w, h) manteniendo proporción, centrada."""
    from PIL import Image as PI
    iw, ih = PI.open(path).size
    s = min(w / iw, h / ih); pw, ph = iw * s, ih * s
    return slide.shapes.add_picture(path, Inches(x + (w - pw) / 2), Inches(y + (h - ph) / 2), Inches(pw), Inches(ph))

def style_axis_text(chart, size=9):
    chart.font.name = "Calibri"; chart.font.size = Pt(size); chart.font.color.rgb = rgb(MUTED)

# ---------- quitar la lámina de instrucciones ----------
sldIdLst = prs.slides._sldIdLst
sid2 = sldIdLst[1]
prs.part.drop_rel(sid2.rId); sldIdLst.remove(sid2)
S = list(prs.slides)  # S[0]=portada, S[1]=A3, ... S[12]=Gracias

# ---------- 1. Portada ----------
s = S[0]
write(shp(s, 8), [[("Menos renglones observados en las notas de pedido", {"bold": True, "color": "FFFFFF", "size": 24})]])
write(shp(s, 9), [[("GRUPO HIDROCOM KALLPA E.I.R.L. · Registro y validación de notas de pedido", {"italic": True, "color": GOLD, "size": 13})]])
write(shp(s, 10), [[("Champion: ", {"bold": True, "color": GOLD, "size": 11}), ("Gutierrez Morales Jhon Alex", {"color": "FFFFFF", "size": 11})],
                   [("Líder BB: ", {"bold": True, "color": GOLD, "size": 11}), ("Mullisaca Condori Carlos Augusto", {"color": "FFFFFF", "size": 11})],
                   [("Analista GB: ", {"bold": True, "color": GOLD, "size": 11}), ("Mamani Mamani Ciro Wagner", {"color": "FFFFFF", "size": 11})],
                   [("Dueño del proceso: ", {"bold": True, "color": GOLD, "size": 11}), ("gerencia de HIDROCOM KALLPA", {"color": "FFFFFF", "size": 11})]])
shp(s, 10).top = Inches(3.62); shp(s, 10).height = Inches(1.15)
s.notes_slide.notes_text_frame.text = ("Champion (30 s): presenta al equipo y el proceso. Este proyecto trata de cuánta información de las notas de pedido "
                                       "llega lista para el reporte comercial y cuánta necesita retrabajo.")

# ---------- 2. A3 ----------
s = S[1]
for rid in (10, 12, 14, 16):
    card(shp(s, rid))
write(shp(s, 11), [[L("PROBLEMA Y COSTO")],
                   [("14,50 %", {"bold": True, "color": RED, "size": 26}), ("  de renglones en REVISAR", {"size": 11, "bold": True})],
                   "38 de 262 renglones del lote no pueden publicarse sin volver al original: ≈ 6,3 h de retrabajo por lote (≈ S/ 47,50/mes)."])
write(shp(s, 13), [[L("META Y LÍNEA BASE")],
                   [("14,50 % → ≤ 5 %", {"bold": True, "color": NAVY, "size": 22})],
                   "en 8 semanas desde que se aprueben las reglas. Línea base del CTQ: DPMO 44 529 ≈ 3,20 σ."])
write(shp(s, 15), [[L("CAUSA RAÍZ CONFIRMADA", RED)],
                   [("El registro no tiene reglas fijas de captura y clasificación.", {"bold": True, "size": 11.5})],
                   "Datos: 13 de 13 renglones PEDIDO y 21 de 22 renglones con datos vacíos o importe incoherente terminan en REVISAR (25 de 38)."])
write(shp(s, 17), [[L("MEJORAS Y RESULTADO")],
                   "Regla escrita del estado PEDIDO · Poka-Yoke de validación en la captura · motivo obligatorio.",
                   [("Simulación: 14,50 % → 4,96 %", {"bold": True, "color": NAVY, "size": 12}), ("  ·  beneficio ≈ S/ 255/año", {"bold": True, "size": 12})]])
key(s, 18, 19, "el problema no es la gente sino la ausencia de reglas; con 3 controles simples la cola de revisión baja dos tercios.")
s.notes_slide.notes_text_frame.text = "Champion (2 min): problema, meta, causa, mejora y beneficio. Decir el 14,50 % y el 4,96 % sin leer."

# ---------- 3. Charter ----------
s = S[2]
remove(shp(s, 10), shp(s, 11))
table(s, 0.70, 1.20, 5.60, 3.30, [
    ["Charter", "Contenido"],
    ["Caso de negocio", "Los reportes comerciales se alimentan de las notas digitadas; 1 de cada 7 renglones llega sin dato confiable y exige retrabajo."],
    ["Problema", "El 14,50 % de los renglones del lote (38 de 262; corte 24-11-2026) queda en REVISAR y no puede publicarse sin verificar el original."],
    ["Meta SMART", "Reducir el % de renglones REVISAR de 14,50 % a ≤ 5 % en el primer lote con controles (8 semanas)."],
    ["Alcance", "SÍ: de la recepción de la nota a su publicación. NO: inventario, reparto, compras, evaluación de personas."],
    ["Hitos", "D 05-11 · M 12-11 · A 17-11 · I 19-11 · C 24-11 · presentación 26-11-2026"],
], [1.25, 4.35], size=9.5)
card(shp(s, 12)); card(shp(s, 14))
write(shp(s, 13), [[L("¿POR QUÉ ESTE PROCESO?")],
                   "Es el único proceso de HIDROCOM con registros reproducibles (262 renglones trazables). Reparto e inventario no tienen datos suficientes."], size=10)
write(shp(s, 15), [[L("EQUIPO Y ROLES")],
                   [B("Champion: ", bold=True, size=10), B("Gutierrez M. Jhon Alex", size=10)],
                   [B("Líder BB: ", bold=True, size=10), B("Mullisaca C. Carlos A.", size=10)],
                   [B("Analista GB: ", bold=True, size=10), B("Mamani M. Ciro W.", size=10)],
                   [B("Dueño: ", bold=True, size=10), B("gerencia de HIDROCOM", size=10)]], size=10)
key(s, 16, 17, "el problema se enuncia sin culpables ni soluciones: describe el % de renglones en REVISAR, nada más.")
s.notes_slide.notes_text_frame.text = "Líder BB (2 min): leer el enunciado del problema y la meta. Explicar por qué se eligió el registro de notas."

# ---------- 4. SIPOC ----------
s = S[3]
remove(shp(s, 10), shp(s, 11))
table(s, 0.70, 1.20, 8.60, 3.30, [
    ["S · Proveedores", "I · Entradas", "P · Proceso", "O · Salidas", "C · Clientes"],
    ["Vendedor / emisor", "Nota de pedido (papel o imagen)", "1. Recibir e identificar la nota", "Nota con ID estable", "Registrador"],
    ["Cliente que pide", "Productos, cantidades, precios", "2. Registrar renglones", "Renglones digitados", "Revisor"],
    ["Responsable de catálogo", "Catálogo de productos", "3. Validar campos y estado  ◄ DEFECTO", "DISPONIBLE / REVISAR / EXCLUIR", "Revisor / aprobador"],
    ["Custodio documental", "Original legible", "4. Resolver observaciones", "Pendientes con evidencia", "Aprobador"],
    ["Aprobador", "Reglas aprobadas", "5. Aprobar versión del lote", "Versión aprobada", "Publicador"],
    ["Data Mart / auditoría", "Versión + huella (hash)", "6. Publicar y conciliar", "Reporte comercial", "Gerencia y compras"],
], [1.6, 1.85, 2.15, 1.65, 1.35], size=10, hl_rows=(3,))
key(s, 12, 13, "el defecto vive en el macropaso 3: ahí se decide si un renglón sirve o se va a la cola de REVISAR.")
s.notes_slide.notes_text_frame.text = "Analista GB (1 min): recorrer los 6 macropasos y señalar el paso 3."

# ---------- 5. Medir ----------
s = S[4]
remove(shp(s, 11))
card(shp(s, 10), fill="FFFFFF")
picture(s, os.path.join(folder, "M1_Flujo_AS-IS_HIDROCOM.png"), 0.76, 1.26, 5.48, 3.18)
card(shp(s, 12)); card(shp(s, 14), fill="EAF0F8", line=NAVY)
write(shp(s, 13), [[L("LÍNEA BASE (CTQ)")],
                   [B("U = 262 ", bold=True), B("renglones")],
                   [B("O = 3 ", bold=True), B("cantidad, precio, importe")],
                   [B("D = 35 ", bold=True), B("defectos en 22 renglones")],
                   [B("Fuente: Comprobantes_Revisados.xlsx, lote 01-2025 a 03-2026", size=9, color=MUTED, italic=True)]], size=10.5)
write(shp(s, 15), [[L("EL NÚMERO GRANDE")],
                   [("DPMO 44 529", {"bold": True, "color": NAVY, "size": 20})],
                   [("≈ 3,20 σ", {"bold": True, "color": RED, "size": 20})],
                   [B("De cada 1 000 datos críticos digitados, ~45 no sirven para el reporte.", size=10)]], size=10)
key(s, 16, 17, "datos de la hoja Detalle_Productos (262 renglones). Sin gráfica de control: el 62 % de las fechas son estimadas.")
s.notes_slide.notes_text_frame.text = ("Analista GB (2 min): flujo como es; en rojo dónde nace el defecto. DPMO = 35 / (262 × 3) × 10^6 = 44 529 → 3,20 sigma. "
                                       "Si preguntan por la gráfica de control: no hay serie temporal confiable.")

# ---------- 6. Pareto (gráfico nativo combinado) ----------
s = S[5]
remove(shp(s, 11))
card(shp(s, 10), fill="FFFFFF")
cats = ["Estado PEDIDO", "Campos incompletos", "Lectura dudosa", "Motivo no explícito", "Diferencia de importe"]
freq = [13, 7, 7, 6, 5]
acc, t = [], 0
for f in freq:
    t += f; acc.append(round(t / 38, 4))
cd = CategoryChartData(); cd.categories = cats
cd.add_series("Renglones", freq); cd.add_series("% acumulado", acc)
gf = s.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED, Inches(0.8), Inches(1.25), Inches(5.7), Inches(3.2), cd)
ch = gf.chart
style_axis_text(ch)
ch.has_legend = True; ch.legend.position = XL_LEGEND_POSITION.BOTTOM; ch.legend.include_in_layout = False
plot = ch.plots[0]; plot.gap_width = 60
ser = plot.series[0]; ser.format.fill.solid(); ser.format.fill.fore_color.rgb = rgb(NAVY)
plot.has_data_labels = True; plot.data_labels.font.size = Pt(9); plot.data_labels.font.bold = True
plot.data_labels.position = XL_LABEL_POSITION.OUTSIDE_END
va = ch.value_axis; va.has_major_gridlines = False; va.maximum_scale = 14
# mover la 2.ª serie a un lineChart con eje secundario
cs = ch._chartSpace; C = "http://schemas.openxmlformats.org/drawingml/2006/chart"
plotArea = cs.find(f".//{{{C}}}plotArea"); bar = plotArea.find(f"{{{C}}}barChart")
sers = bar.findall(f"{{{C}}}ser"); s2 = sers[1]; bar.remove(s2)
line = etree.SubElement(plotArea, f"{{{C}}}lineChart")
plotArea.remove(line); plotArea.insert(list(plotArea).index(bar) + 1, line)
etree.SubElement(line, f"{{{C}}}grouping").set("val", "standard")
etree.SubElement(line, f"{{{C}}}varyColors").set("val", "0")
line.append(s2)
for e in s2.findall(f"{{{C}}}invertIfNegative"):
    s2.remove(e)
spPr = s2.find(f"{{{C}}}spPr")
if spPr is not None:
    s2.remove(spPr)
spPr = etree.fromstring(f'<c:spPr xmlns:c="{C}" xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"><a:ln w="28575"><a:solidFill><a:srgbClr val="{RED}"/></a:solidFill></a:ln></c:spPr>')
s2.insert(list(s2).index(s2.find(f"{{{C}}}tx")) + 1, spPr)
mk = etree.fromstring(f'<c:marker xmlns:c="{C}" xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"><c:symbol val="circle"/><c:size val="6"/><c:spPr><a:solidFill><a:srgbClr val="{RED}"/></a:solidFill><a:ln><a:noFill/></a:ln></c:spPr></c:marker>')
s2.insert(list(s2).index(spPr) + 1, mk)
dl = etree.fromstring(f'<c:dLbls xmlns:c="{C}" xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"><c:numFmt formatCode="0%" sourceLinked="0"/><c:spPr><a:noFill/><a:ln><a:noFill/></a:ln></c:spPr><c:txPr><a:bodyPr/><a:lstStyle/><a:p><a:pPr><a:defRPr sz="900" b="1"><a:solidFill><a:srgbClr val="{RED}"/></a:solidFill></a:defRPr></a:pPr><a:endParaRPr lang="es-PE"/></a:p></c:txPr><c:dLblPos val="t"/><c:showLegendKey val="0"/><c:showVal val="1"/><c:showCatName val="0"/><c:showSerName val="0"/><c:showPercent val="0"/><c:showBubbleSize val="0"/></c:dLbls>')
s2.insert(list(s2).index(mk) + 1, dl)
etree.SubElement(s2, f"{{{C}}}smooth").set("val", "0")
etree.SubElement(line, f"{{{C}}}marker").set("val", "1")
etree.SubElement(line, f"{{{C}}}axId").set("val", "900001")
etree.SubElement(line, f"{{{C}}}axId").set("val", "900002")
last_ax = plotArea.findall(f"{{{C}}}valAx")[-1]
idx = list(plotArea).index(last_ax) + 1
catAx2 = etree.fromstring(f'<c:catAx xmlns:c="{C}"><c:axId val="900001"/><c:scaling><c:orientation val="minMax"/></c:scaling><c:delete val="1"/><c:axPos val="b"/><c:majorTickMark val="none"/><c:minorTickMark val="none"/><c:tickLblPos val="nextTo"/><c:crossAx val="900002"/><c:crosses val="autoZero"/><c:auto val="1"/><c:lblAlgn val="ctr"/><c:lblOffset val="100"/><c:noMultiLvlLbl val="0"/></c:catAx>')
valAx2 = etree.fromstring(f'<c:valAx xmlns:c="{C}" xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"><c:axId val="900002"/><c:scaling><c:orientation val="minMax"/><c:max val="1"/><c:min val="0"/></c:scaling><c:delete val="0"/><c:axPos val="r"/><c:numFmt formatCode="0%" sourceLinked="0"/><c:majorTickMark val="out"/><c:minorTickMark val="none"/><c:tickLblPos val="nextTo"/><c:txPr><a:bodyPr/><a:lstStyle/><a:p><a:pPr><a:defRPr sz="900"><a:solidFill><a:srgbClr val="{MUTED}"/></a:solidFill></a:defRPr></a:pPr><a:endParaRPr lang="es-PE"/></a:p></c:txPr><c:crossAx val="900001"/><c:crosses val="max"/><c:crossBetween val="between"/></c:valAx>')
plotArea.insert(idx, catAx2); plotArea.insert(idx + 1, valAx2)
card(shp(s, 12))
write(shp(s, 13), [[L("LECTURA")],
                   [B("PEDIDO + incompletos + dudosa = ", size=10.5), B("71 %", bold=True, color=RED, size=14), B(" de los 38.", size=10.5)],
                   [B("Si se agrupa la captura numérica (incompletos + diferencia de importe), PEDIDO y captura explican ", size=10.5), B("25 de 38 (66 %)", bold=True, size=10.5), B(".", size=10.5)],
                   [B("No atacamos aún «motivo no explícito»: requiere los originales.", italic=True, color=MUTED, size=10)]], size=10.5)
key(s, 14, 15, "dos pocos vitales: el estado PEDIDO sin regla y la captura numérica sin validar.")
s.notes_slide.notes_text_frame.text = "Líder BB (1,5 min): decir 71 % y 66 % sin leer. Clasificación con regla exclusiva: cada renglón cuenta una sola vez."

# ---------- 7. Ishikawa ----------
s = S[6]
remove(shp(s, 11))
card(shp(s, 10), fill="FFFFFF")
picture(s, os.path.join(folder, "A2_Ishikawa_HIDROCOM.png"), 0.76, 1.26, 5.18, 3.18)
card(shp(s, 12)); card(shp(s, 14), fill="FDECEC", line=RED)
write(shp(s, 13), [[L("VERIFICACIÓN CON DATOS")],
                   [B("✔ Regla PEDIDO: ", bold=True, color=RED, size=9.5), B("13/13 van a REVISAR", size=9.5)],
                   [B("✔ Captura sin validación: ", bold=True, color=RED, size=9.5), B("21/22 con defecto van a REVISAR", size=9.5)],
                   [B("✘ Fechas estimadas: ", bold=True, color=MUTED, size=9.5), B("16,0 % vs 12,0 % con fecha real", size=9.5)],
                   [B("◐ Base de precio: ", bold=True, color="9C7A00", size=9.5), B("explica 1 de 5 diferencias", size=9.5)]], size=9.5)
write(shp(s, 15), [[L("CONCLUSIÓN", RED)],
                   [B("La causa raíz confirmada es la falta de reglas estandarizadas de captura y clasificación, ", bold=True, size=10.5),
                    B("porque 25 de los 38 renglones en REVISAR provienen de PEDIDO sin regla o de datos que la hoja dejó guardar incompletos.", size=10.5)]], size=10.5)
key(s, 16, 17, "no saltamos a la solución: verificamos 4 causas y descartamos una que parecía obvia (las fechas).")
s.notes_slide.notes_text_frame.text = "Analista GB (2 min): Ishikawa 6M; explicar las 4 verificaciones. Leer la conclusión en voz alta."

# ---------- 8. Mejorar ----------
s = S[7]
remove(shp(s, 11), shp(s, 15))
card(shp(s, 10), fill="FFFFFF")
picture(s, os.path.join(folder, "I1_Matriz_HIDROCOM.png"), 0.74, 1.23, 4.17, 1.54)
card(shp(s, 12))
write(shp(s, 13), [[L("LAS 3 MEJORAS ELEGIDAS")],
                   [B("1. Regla escrita PEDIDO: ", bold=True, size=9.5), B("estado propio, no publicable hasta confirmar venta (Kaizen).", size=9.5)],
                   [B("2. Validación en la captura: ", bold=True, size=9.5), B("no se guarda un renglón vacío o incoherente (Poka-Yoke de prevención).", size=9.5)],
                   [B("3. Motivo obligatorio: ", bold=True, size=9.5), B("lista cerrada al marcar REVISAR/EXCLUIR (Poka-Yoke de detección).", size=9.5)]], size=9.5)
table(s, 0.70, 2.95, 8.60, 1.55, [
    ["PDCA · acción", "Responsable", "Fecha", "Indicador · antes → meta", "Estado"],
    ["P · Aprobar regla PEDIDO y lista de motivos", "BB + dueño", "26-11-2026", "REVISAR por PEDIDO · 13 → 0", "Borrador listo"],
    ["H · Validación de datos en la hoja de captura", "Analista GB", "03-12-2026", "Defectos D · 35 → ≤ 5", "Prototipo listo"],
    ["V · Simular controles sobre los 262 renglones", "Equipo", "24-11-2026", "% REVISAR · 14,50 % → 4,96 %", "Hecho (simulado)"],
    ["A · Piloto real con un lote nuevo + instructivo", "Dueño + Champion", "Enero 2027", "% REVISAR · ≤ 5 %", "Pendiente"],
], [3.0, 1.3, 1.0, 2.1, 1.2], size=9, hl_rows=())
key(s, 16, 17, "cada mejora ataca una causa verificada: 1 → regla PEDIDO, 2 → captura sin validación, 3 → motivo no explícito.")
s.notes_slide.notes_text_frame.text = "Líder BB (2 min): matriz, por qué ganan 1, 2 y 3, y el estado real del plan PDCA hoy."

# ---------- 9. Resultados (simulación) ----------
s = S[8]
_runs = shp(s, 4).text_frame.paragraphs[0].runs
_runs[0].text = "MEJORAR · RESULTADO DE LA SIMULACIÓN"
for _r in _runs[1:]:
    _r._r.getparent().remove(_r._r)
remove(shp(s, 11))
card(shp(s, 10), fill="FFFFFF")
cd = CategoryChartData()
cd.categories = ["Estado PEDIDO", "Incompletos", "Diferencia importe", "Lectura dudosa", "Sin motivo"]
cd.add_series("Antes (lote real)", [13, 7, 5, 7, 6]); cd.add_series("Después (simulación)", [0, 0, 0, 7, 6])
gf = s.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED, Inches(0.8), Inches(1.6), Inches(5.7), Inches(2.85), cd)
ch = gf.chart; style_axis_text(ch)
ch.has_legend = True; ch.legend.position = XL_LEGEND_POSITION.BOTTOM; ch.legend.include_in_layout = False
pl = ch.plots[0]; pl.gap_width = 70; pl.overlap = -10
for sr, col in zip(pl.series, (NAVY, GOLD)):
    sr.format.fill.solid(); sr.format.fill.fore_color.rgb = rgb(col)
pl.has_data_labels = True; pl.data_labels.font.size = Pt(9); pl.data_labels.position = XL_LABEL_POSITION.OUTSIDE_END
ch.value_axis.has_major_gridlines = False; ch.value_axis.maximum_scale = 15; ch.value_axis.minimum_scale = 0; ch.value_axis.major_unit = 5
tb = s.shapes.add_textbox(Inches(0.9), Inches(1.22), Inches(5.5), Inches(0.4))
write(tb, [[B("% REVISAR:  ", bold=True, size=13), B("14,50 %", bold=True, color=NAVY, size=16), B("  →  ", bold=True, size=13),
            B("4,96 %", bold=True, color=RED, size=16), B("   (38 → 13 renglones, −66 %)", size=11, color=MUTED)]])
card(shp(s, 12), fill="FFF8E1", line=GOLD)
write(shp(s, 13), [[L("HONESTIDAD METODOLÓGICA")],
                   [B("Qué es: ", bold=True, size=10), B("una prueba de escritorio: aplicamos los 3 controles a los 262 renglones del lote.", size=10)],
                   [B("Qué NO prueba: ", bold=True, size=10), B("que el registrador corrija bien contra el original, ni el tiempo real ahorrado.", size=10)],
                   [B("Qué falta: ", bold=True, size=10), B("piloto con un lote nuevo (enero 2027) y medir % REVISAR y minutos.", size=10)]], size=10)
key(s, 14, 15, "es una estimación con supuestos visibles, no un resultado de campo; la meta ≤ 5 % se confirma con el piloto.")
s.notes_slide.notes_text_frame.text = "Champion o BB (1,5 min): insistir en que es simulación. Lo que queda (13) son casos que sí necesitan el original."

# ---------- 10. Control ----------
s = S[9]
remove(shp(s, 10), shp(s, 11))
table(s, 0.70, 1.20, 8.60, 2.20, [
    ["KPI", "Meta", "Fuente", "Frecuencia", "Responsable", "Umbral", "Reacción"],
    ["% renglones REVISAR", "≤ 5 %", "Hoja de captura", "Por lote", "Dueño del proceso", "> 7 % o > 5 % dos lotes", "Kaizen 15 min con Pareto de motivos"],
    ["DPMO del CTQ", "≤ 6 210 (4 σ)", "Vacíos e incoherentes", "Mensual", "Líder BB", "> 22 750 (< 3,5 σ)", "Revisar que la validación siga activa"],
    ["% REVISAR/EXCLUIR con motivo", "100 %", "Columna motivo", "Por lote", "Analista GB", "< 100 %", "Devolver el lote antes de publicar"],
    ["% publicaciones conciliadas", "100 %", "Hash Excel vs Data Mart", "Por publicación", "Champion", "Cualquier diferencia", "Bloquear y reprocesar la versión"],
], [1.75, 0.95, 1.3, 0.9, 1.15, 1.25, 1.3], size=9)
card(shp(s, 12))
write(shp(s, 13), [[L("PARA SISTEMAS · QUÉ SE AUTOMATIZA")],
                   "Validación de datos y hoja protegida (prevención) · formato condicional en rojo para renglones incompletos · "
                   "script que compara el hash antes de publicar · tarjeta de Power BI con % REVISAR y alerta si supera 5 %."], size=10)
key(s, 14, 15, "cada KPI tiene dueño y umbral; el instructivo de una página y la plantilla bloqueada estandarizan la mejora (Seiketsu).")
s.notes_slide.notes_text_frame.text = "Analista GB (1,5 min): quién mira cada KPI el mes siguiente y qué hace si se cruza el umbral."

# ---------- 11. Beneficio ----------
s = S[10]
card(shp(s, 10), fill="EAF0F8", line=NAVY); card(shp(s, 12))
write(shp(s, 11), [[L("BENEFICIO ANUALIZADO ESTIMADO")],
                   [("S/ 255", {"bold": True, "color": NAVY, "size": 48})],
                   [B("= (47,50 − 16,25) × 12 − 120", bold=True, size=14)],
                   [B("Antes: 38 renglones × 10 min × S/ 7,50/h = S/ 47,50/mes", size=12)],
                   [B("Después: 13 renglones × 10 min × S/ 7,50/h = S/ 16,25/mes", size=12)],
                   [B("Costo de implementar: 16 h del equipo = S/ 120", size=12)]], size=12)
write(shp(s, 13), [[L("SUPUESTOS (¿ES CAJA REAL?)")],
                   [B("No es caja directa: ", bold=True, size=12), B("son horas de revisión liberadas.", size=12)],
                   [B("Supuestos por validar: ", bold=True, size=12), B("1 lote de ~262 renglones al mes; 10 min por renglón; S/ 7,50/h (≈ remuneración mínima / 150 h).", size=12)],
                   [B("Beneficio no cuantificado: ", bold=True, size=12), B("evitar publicar importes errados sobre S/ 26 509,70 disponibles del lote.", size=12)],
                   [B("Fuente: hoja C2 del Excel DMAIC.", italic=True, color=MUTED, size=11)]], size=12)
key(s, 14, 15, "preferimos un beneficio modesto y defendible a un número que no resiste la pregunta de finanzas.")
s.notes_slide.notes_text_frame.text = "Champion (1 min): decir S/ 255 y aclarar que son horas liberadas, no caja. Los supuestos están en la hoja C2."

# ---------- 12. Lecciones ----------
s = S[11]
card(shp(s, 10)); card(shp(s, 12))
write(shp(s, 11), [[L("LECCIONES TÉCNICAS")],
                   [B("1. Definir el CTQ antes de contar. ", bold=True, size=12.5), B("Las 151 «incidencias» no eran 151 defectos; contar sin definir nos habría dado un DPMO falso.", size=12.5)],
                   [B("2. Verificar con datos cambia la historia. ", bold=True, size=12.5), B("Las fechas estimadas parecían la causa y los datos la descartaron.", size=12.5)],
                   [B("3. Regla exclusiva en el Pareto. ", bold=True, size=12.5), B("Cada renglón cuenta una vez; así el 100 % suma 38.", size=12.5)]], size=12.5)
write(shp(s, 13), [[L("LECCIONES DE EQUIPO")],
                   [B("Separar hallazgos de supuestos ", bold=True, size=12.5), B("y dejar cada decisión con dueño evitó discusiones sin datos.", size=12.5)],
                   [B("¿Qué haríamos distinto? ", bold=True, size=12.5), B("Ir antes al Gemba a cronometrar el registro real, para medir tiempos en lugar de suponerlos.", size=12.5)]], size=12.5)
key(s, 14, 15, "el método nos obligó a demostrar antes de proponer, y eso cambió la mejora que habríamos elegido.")
s.notes_slide.notes_text_frame.text = "Todos (1 min): cada integrante dice una lección."

# ---------- 13. Gracias ----------
s = S[12]
card(shp(s, 5), fill="0A3E78", line=GOLD)
write(shp(s, 6), [[("«El 14,50 % de los renglones de nuestras notas de pedido necesitaba retrabajo. ", {"italic": True, "color": "FFFFFF", "size": 15}),
                   ("No faltaba esfuerzo: faltaban reglas. ", {"bold": True, "color": GOLD, "size": 15}),
                   ("Con tres controles simples la cola baja a 4,96 % y liberamos S/ 255 al año.»", {"italic": True, "color": "FFFFFF", "size": 15})],
                  [("Quedamos atentos a sus preguntas.", {"bold": True, "color": "FFFFFF", "size": 13})]])
s.notes_slide.notes_text_frame.text = "Champion (30 s): cierre y pase a preguntas."

prs.save(out)
print("ok", out)

# corregir content type "image/jpg" (no estándar) heredado de la plantilla
import zipfile, shutil
tmp = out + ".tmp"
with zipfile.ZipFile(out) as zi, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zo:
    for it in zi.infolist():
        data = zi.read(it.filename)
        if it.filename == "[Content_Types].xml":
            import re as _re
            data = _re.sub(rb'<Override PartName="/ppt/media/[^"]+\.jpg" ContentType="image/jpg"/>', b'', data)
            if b'Extension="jpg"' not in data:
                data = data.replace(b'<Default ', b'<Default Extension="jpg" ContentType="image/jpeg"/><Default ', 1)
        zo.writestr(it, data)
shutil.move(tmp, out)
print("content types ok")
