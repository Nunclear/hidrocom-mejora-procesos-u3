"""Actualiza navegación y evidencia de integración con rutas relativas."""
from pathlib import Path
from zipfile import ZipFile
from xml.etree import ElementTree as ET
from collections import Counter
import hashlib,json,csv,shutil
R=Path(__file__).resolve().parents[1]
for folder,stem in [('01_Lean','U3_Lean_HIDROCOM'),('02_Seis_Sigma','U3_Seis_Sigma_HIDROCOM'),('03_DMAIC','U3_DMAIC_HIDROCOM')]:
    shutil.copyfile(R/'.qa/word'/(stem+'.pdf'),R/folder/(stem+'.pdf'))
shutil.copyfile(R/'03_DMAIC/U3_DMAIC_HIDROCOM.pdf',R/'04_Producto_Final/U3_Informe_HIDROCOM.pdf')
qa=json.loads((R/'validacion/pdf_word.json').read_text(encoding='utf8'))
for x in qa:x['revision_visual']='A inspeccionó todas las páginas renderizadas con PDFium; sin recortes ni superposición observados.'
(R/'validacion/pdf_word.json').write_text(json.dumps(qa,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
gen=json.loads((R/'documentacion/generacion_word.json').read_text(encoding='utf8'))
for x in gen:x['revision_visual']='Exportado en Microsoft Word y revisado por A; 9 páginas.'
(R/'documentacion/generacion_word.json').write_text(json.dumps(gen,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
# Public summary retains checks and hashes, without machine-specific private paths.
ppt=json.loads((R/'validacion/presentaciones_exportacion.json').read_text(encoding='utf8'))
for x in ppt['receipts']:
    f=x['finalization'];x['validacion']={'integridad':f['packageIntegrity']['status'],'hallazgos_integridad':f['packageIntegrity']['findingCount'],'hallazgos_geometria':f['presentationLayout']['findingCount'],'fuentes':f['fontSelection']['approvedFamilies'],'importacion_artifact_tool':f['firstPartyImport']['passed'],'revision_visual':'A inspeccionó todas las láminas renderizadas; contenido coherente con los informes.','prueba_powerpoint_nativo':'No ejecutada; importación y render Artifact Tool no la sustituyen.'};del x['finalization']
(R/'validacion/presentaciones_exportacion.json').write_text(json.dumps(ppt,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
read=R/'README.md';t=read.read_text(encoding='utf8')
start=t.index('## Tres trabajos independientes');end=t.index('### Distinciones necesarias')
t=t[:start]+'''## Tres trabajos independientes

| Trabajo | Word editable | PDF | Excel | Presentación |
|---|---|---|---|---|
| [01 Lean](01_Lean/README.md) | [Word](01_Lean/U3_Lean_HIDROCOM.docx) | [9 páginas](01_Lean/U3_Lean_HIDROCOM.pdf) | [Libro](01_Lean/U3_Lean_HIDROCOM.xlsx) | [10 láminas](01_Lean/U3_Lean_HIDROCOM.pptx) |
| [02 Seis Sigma](02_Seis_Sigma/README.md) | [Word](02_Seis_Sigma/U3_Seis_Sigma_HIDROCOM.docx) | [9 páginas](02_Seis_Sigma/U3_Seis_Sigma_HIDROCOM.pdf) | [Libro](02_Seis_Sigma/U3_Seis_Sigma_HIDROCOM.xlsx) | [12 láminas](02_Seis_Sigma/U3_Seis_Sigma_HIDROCOM.pptx) |
| [03 DMAIC](03_DMAIC/README.md) | [Word](03_DMAIC/U3_DMAIC_HIDROCOM.docx) | [13 páginas](03_DMAIC/U3_DMAIC_HIDROCOM.pdf) | [Libro](03_DMAIC/U3_DMAIC_HIDROCOM.xlsx) | [13 láminas](03_DMAIC/U3_DMAIC_HIDROCOM.pptx) |

Lean estudia valor y flujo. Seis Sigma desarrolla las definiciones, funciones y medición. DMAIC organiza las cinco fases. Los tres trabajos pueden leerse por separado y comparten el mismo lote de estudio. El Word/PDF y PPTX de DMAIC se reproducen sin cambios en `04_Producto_Final` para la entrega oficial; son copias identificadas, no otros proyectos.

Apoyos comunes: [dashboard de calidad](06_Dashboard/README.md), [modelo costo-beneficio](05_Costo_Beneficio/Costo_Beneficio_HIDROCOM.xlsx), [contrato de datos](coordinacion/CONTRATO_DE_DATOS.md), [instrumentos sin diligenciar](instrumentos/README.md), [matriz de tareas](coordinacion/MATRIZ_TAREAS.csv) e [informe de integración y rúbrica](coordinacion/INFORME_INTEGRACION.md).

La [presentación anterior en ChatGPT](https://chatgpt.com/space/page_ca61c7120d948191aaa3a90517d367db) es una versión histórica y puede contener definiciones anteriores. Para la revisión actual se usan los archivos enlazados en la tabla.

El usuario confirmó que no puede acreditar proveedor, procedencia original ni autenticidad empresarial de las 73 notas. Tampoco hay constancia oficial para el inicio reportado del 09/03/2026. Se mantienen pendientes y se trabaja con un lote documental, sin atribuir representatividad empresarial.

''' + t[end:]
t=t.replace('La muestra contiene','El lote contiene').replace('de la muestra completa','del lote completo').replace('en la muestra.','en el lote.').replace('origen de la muestra','origen del lote').replace('la muestra completa','el lote completo')
t=t.replace('El Excel no coincide con su hash declarado','El Excel del paquete ZIP v3 no coincide con su hash declarado')
t=t.replace('El hash del Excel actual difiere del declarado en `auditoria.json`; los nueve CSV coinciden con sus huellas registradas.','En el ZIP v3, el hash del Excel difiere del declarado en `auditoria.json`; los nueve CSV coinciden con sus huellas registradas. Otra copia de C usa el mismo Excel y una publicación diferente.').replace('Se confirma la diferencia entre archivos, no su autor o fecha de origen.','Diferencia reproducida en ZIP v3; otra publicación de C reporta su corrección. No se atribuye autor o fecha.')
a=t.index('## Evaluación económica');b=t.index('## Próximos pasos',a)
t=t[:a]+'''## Evaluación económica y sensibilidad

El [modelo parametrizable](05_Costo_Beneficio/Costo_Beneficio_HIDROCOM.xlsx) usa supuestos explícitos: 10 minutos por REVISAR, S/ 7,50 por hora y S/ 120 iniciales. Con 25 casos alcanzables y un lote mensual, la capacidad valorizada neta del escenario de eficacia máxima es S/ 255 al año. Con un lote distribuido en 13,3 meses resulta −S/ 91,80. El equilibrio condicionado es 12,16 REVISAR iniciales por mes. El costo recurrente figura «No estimado»; omitirlo del escenario no acredita que sea cero. La tasa de 9 % procede del caso guía del curso y no de la empresa.

La simulación aplica eficacias de 100 %, 75 %, 50 % y 25 % sobre la unión de 25 renglones y produce 13; 19,25; 25,50 y 31,75 REVISAR esperados. Son expectativas del modelo, no resultados observados. Tiempos, costos reales y recurrencia siguen pendientes. Los importes comerciales no se convierten en ahorros.

## Métrica principal y límites estadísticos

La completitud sintáctica principal registra 30 campos vacíos (5 cantidades, 16 precios y 9 importes) de 786 inspeccionados: 38 167,94 equivalentes por millón y sigma equivalente 3,2724 con convención +1,5. S34 y S35 son sensibilidades combinadas diferentes, con 43 257,00 / 3,2141 y 44 529,26 / 3,2004. No representan CTQ aprobado, capacidad operativa ni nivel sigma empresarial.

El intervalo Wilson nominal 95 % para 38/262 es 10,75–19,28 % bajo independencia. ICC ≈ 0,246 y DEFF ≈ 1,69 son aproximaciones exploratorias por agrupamiento en notas. No existe diseño muestral que permita generalizar estos resultados a toda la empresa. DISPONIBLE no es FPY y no se calcula RTY sin mediciones secuenciales.

## Verificación y reproducción

Los PDF fueron exportados desde Microsoft Word y A revisó sus 31 páginas. Se revisaron las 35 láminas únicas. Los PPTX contienen tablas y gráficos editables y pasaron controles de integridad, geometría, fuentes de la plantilla e importación Artifact Tool. No se afirma haberlos probado en PowerPoint o Google Slides.

Con Python y las dependencias de `requirements-validacion.txt`:

```powershell
python -m pip install -r requirements-validacion.txt
python herramientas/ejecutar_pruebas.py
python herramientas/validar_integracion.py --final --revision revision-examinada
```

La validación compara las fuentes con el [corte congelado](datos_control/corte_documental_73_262.json), reproduce métricas y escenarios, inspecciona cachés de fórmulas, paquetes y enlaces locales. Leer cachés no equivale a recalcular Excel. C reportó recálculo nativo de sus cuatro libros y B/C del económico; A realizó cálculos independientes. El dashboard se calculó y probó con Artifact Tool. [Resultados](validacion/resultados_integracion.json), [pruebas funcionales](validacion/pruebas_modelos.json), [dashboard](validacion/dashboard_pruebas.json), [PDF/Word](validacion/pdf_word.json) y [PPTX](validacion/presentaciones_exportacion.json).

La conciliación distingue el ZIP v3 verificado por A y la copia posterior reportada por C. Véanse [huellas y límites](coordinacion/TRAZABILIDAD_FUENTES.csv). PM08 describe cambios entre capturas según el análisis de C; A no dispuso de los bytes de la primera captura y no lo presenta como reproducción propia.

''' + t[b:]
read.write_text(t,encoding='utf8')
for folder,stem in [('01_Lean','U3_Lean_HIDROCOM'),('02_Seis_Sigma','U3_Seis_Sigma_HIDROCOM'),('03_DMAIC','U3_DMAIC_HIDROCOM')]:
    f=R/folder/'README.md';s=f.read_text(encoding='utf8');s=s.replace('- [Informe PDF]',f'- [Word editable]({stem}.docx)\n- [Presentación PowerPoint]({stem}.pptx)\n- [Informe PDF]',1)
    s=s.replace('La muestra suministrada','El lote documental suministrado')
    s=s.replace('El Excel no coincide con su hash declarado, aunque los nueve CSV sí coinciden con los suyos.','En el ZIP v3 de A, el Excel difiere de su huella declarada, aunque los nueve CSV coinciden con las suyas. C reportó otra publicación del mismo Excel. La discrepancia se conserva como específica de versión.')
    s=s.replace('No se aportaron las imágenes originales citadas.','A no accedió a todas las imágenes originales citadas. La retrospectiva de C no equivale a cotejo físico ni verificación empresarial.')
    s=s.replace('[Presentación editable de las cinco fases](https://chatgpt.com/space/page_ca61c7120d948191aaa3a90517d367db) (sujeta a los permisos de ChatGPT). El informe y Excel conservan el desarrollo verificado de 15 páginas y 13 hojas.','El informe actual tiene 13 páginas y el PowerPoint 13 láminas. El Word/PDF y PPTX coinciden con las copias del producto oficial 04; el Excel independiente conserva sus hojas propias.')
    s+='\nLa procedencia original y la fecha reportada 09/03/2026 siguen sin verificar por indicación expresa del usuario. [Contrato común](../coordinacion/CONTRATO_DE_DATOS.md) e [instrumentos pendientes](../instrumentos/README.md).\n';f.write_text(s,encoding='utf8')
tr=R/'coordinacion/TRAZABILIDAD_FUENTES.csv'
with tr.open('a',encoding='utf8',newline='') as f:
    w=csv.writer(f);w.writerows([['C-copia-reportada','ZIP posterior de C','e5507f7a8e69787a67e650bf9dbf8c22e4d96634789b50cc69cd4161d32fc1ff','36d23a8','Reportado por C; bytes no disponibles a A','Específica de versión'],['C-copia-reportada','DataMart/Publicado/auditoria.json','a858d11b6ec0da3e17f8a79c42c7a45488d44c4f45f9ea46960710947ad0c598','36d23a8','Reportado por C; fecha_carga 2026-11-21T17:10:45Z; declara ac6ab323…','Específica de versión']])
print('PDF, navegación y trazabilidad actualizados')
