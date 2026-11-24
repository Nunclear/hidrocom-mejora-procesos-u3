# 05 · Auditoría DMAIC

Objeto:
- `03_DMAIC/` (`main`): PDF de 15 págs. y Excel de 13 hojas.
- `04_Producto_Final/` (rama `claude/excel-dmaic-oficial`): Excel con el formato oficial y presentación de 13 láminas.
- El informe Word con la plantilla oficial **no existe aún** en ninguna rama.

Hay **dos versiones del DMAIC con posturas distintas**:

| | `03_DMAIC` (`main`) | `04_Producto_Final` |
|---|---|---|
| Postura | Diagnóstico: todo lo no medido queda «pendiente» | Producto del curso: llena meta, roles, puntajes, simulación y beneficio como «propuesta» |
| Riesgo | Incumple la plantilla oficial (pide meta, causa confirmada, KPIs con dueño, beneficio en S/) | Sobreafirmación: causas definicionales, simulación circular, beneficio sensible al volumen |

Ninguna es aceptable sola. La versión final debe cumplir la plantilla **y** rotular con precisión la naturaleza de cada cifra.

## DEFINIR

| Elemento | 03_DMAIC | 04 | Dictamen |
|---|---|---|---|
| Problema | ✔ sin culpables | ✔ | Correcto. En 04 «1 de cada 7 renglones» = 38/262 es correcto. |
| Justificación / caso de negocio | ◐ «costo no medido» | ◐ S/ 47,50/mes por supuesto | Ver AUD-005 |
| Alcance | ✔ | ✔ | Coherentes |
| SIPOC | ✔ (6 pasos, tabla) | ✔ (marca el paso 3) | Ambos son propuestas; no fueron validados en campo |
| Charter | ✔ sin meta | ✔ con meta propuesta | La meta no está aprobada por la empresa (AUD-006) |
| VOC | ✘ | ✘ | AUD-013 |
| CTQ | ◐ pendiente | ◐ «propuesto» | Debe ser uno solo en los tres trabajos (AUD-002) |
| Objetivos general y específicos | ◐ solo general | ✘ | Añadir 3 o 4 objetivos específicos |
| Meta SMART | ✘ pendiente | ◐ 14,50 % → ≤ 5 % en 8 semanas, propuesta | Aceptable solo si se rotula «propuesta del equipo, pendiente de aprobación del dueño» |
| Interesados / restricciones | ◐ | ◐ | Suficiente para el nivel |

## MEDIR

| Elemento | Dictamen |
|---|---|
| Plan de recolección | ◐ El de 03 es bueno pero no tiene instrumento. Ver 12_DATOS_PENDIENTES. |
| Calidad de la información | ◐ La procedencia no está confirmada (AUD-001) |
| Definiciones operacionales | ◐ Hay dos criterios D (AUD-002) |
| Población | ✔ Población completa del lote: 262 renglones (no es muestra) |
| Línea base | ✔ 14,50 % reproducible. Falta el intervalo y la nota sobre el efecto de diseño (AUD-007). |
| Sistema de medición (MSA) | ✘ No se trata. **Sí es pertinente** un MSA por atributos: dos revisores clasifican la misma muestra de renglones (p. ej. 40) en DISPONIBLE, REVISAR o EXCLUIR y se calcula el acuerdo (kappa). El estado REVISAR lo asignó una sola persona y su repetibilidad se desconoce. **Requiere los originales.** |
| Inclusión / exclusión | ✔ Los 18 EXCLUIR se conservan |
| Reproducibilidad | ✔ Los conteos se reproducen exactamente (02_AUDITORIA_DATOS) |

## ANALIZAR

| Elemento | Dictamen |
|---|---|
| Pareto | ✔ Las categorías son **mutuamente excluyentes** por prioridad, **exhaustivas** (el resto cae en «motivo no explicitado») y **reproducibles** (0 discrepancias). Porcentajes 34,21 / 52,63 / 71,05 / 86,84 / 100 verificados. El orden de prioridad es arbitrario y cambia los tamaños. Hay que declararlo, cosa que 03 hace. |
| Ishikawa | ✔ en 03, como hipótesis. ◐ en 04, que marca causas «respaldadas». |
| 5 porqués | ◐ Solo en 04 (A2!A20). Los dos últimos porqués son especulativos («no hay dueño del proceso que apruebe criterios»). |
| Análisis descriptivo | ✔ |
| **Verificación de causa raíz** | **✘ en 04 (AUD-003).** «13/13 PEDIDO → REVISAR» y «21/22 numéricos → REVISAR» son asociaciones **por construcción**: quien digitalizó el lote asignó REVISAR precisamente a esos renglones. No verifican una causa; describen la regla de clasificación. Una causa raíz del proceso, como «la captura no tiene campos obligatorios», requiere observar la captura o revisar la herramienta usada por la empresa. |
| Estratificación | ◐ Solo por tipo de fecha. Fisher p = 0,47 con n efectivo ≈ 155: **no hay poder** para descartar la variable. Hay que decir «no se encontró evidencia», no «descartada». |
| Síntoma, condición y causa | En 03 se diferencian bien. En 04 se mezclan: la condición documental se presenta como causa. |

## MEJORAR

| Elemento | Dictamen |
|---|---|
| Alternativas | ✔ 8 ideas, coherentes en los tres trabajos |
| Matriz de priorización | ✘ sin puntajes en 03; ◐ con puntajes propuestos por el agente en 04 (AUD-006) |
| Factibilidad, costos, riesgos | ◐ 03 tiene una tabla de riesgos; falta factibilidad por idea |
| Piloto | ✘ No ejecutado (declarado) |
| **Simulación** | **◐ en 04 (AUD-004).** 14,50 % → 4,96 % elimina por construcción las 25 filas que los controles atacan y supone que el 100 % se corrige. Es el **máximo teórico**. Con 75 %, 50 % y 25 % de corrección efectiva resultan 7,35 %, 9,73 % y 12,12 %. Hay que presentarla como rango. |
| Impacto esperado / plan | ✔ PDCA en ambos |

## CONTROLAR

| Elemento | Dictamen |
|---|---|
| Plan de control | ◐ en 03: indicadores sin meta ni dueño. ✔ en 04: 4 KPIs con meta, fuente, frecuencia, responsable, umbral y reacción, todos **propuestos**. |
| Procedimientos estándar | ◐ descritos, no redactados como documento |
| Gestión de excepciones | ◐ PEDIDO, base kg y millar sin regla escrita (AUD-002) |
| Auditorías / trazabilidad | ✔ conciliación de hash propuesta |
| **Diseñado o operativo** | **Diseñado.** Ningún control opera hoy en la empresa. Los dos documentos lo dicen; mantenerlo. |
