# 08 · Auditoría documental y visual

Se revisaron visualmente las 29 páginas de los tres PDF (miniaturas en `14_EVIDENCIAS_AUDITORIA/miniaturas_*.png`; páginas sueltas en `pdf_paginas/`), las 13 láminas de la presentación (renderizadas con PowerPoint) y el texto extraído (`pdf_texto/`).

## Cumplimiento del formato oficial (ZIP del curso, Sesión 7)

| Entregable oficial | Estado | Dictamen |
|---|---|---|
| Informe Word con `U3_Producto_Plantilla_Informe_UPeU.docx` (12–18 págs.) | **No existe.** `main` tiene un PDF de 15 págs. generado con ReportLab, con estructura propia. | ✘ **AUD-014 (P1).** Asignado a Codex; no publicado al corte. |
| Excel con `U3_Producto_Formato_DMAIC_UPeU.xlsx` | ✔ en 04 | Cumple la estructura D1–C2 |
| Presentación con `U3_Producto_Plantilla_Presentacion_UPeU.pptx` | ✔ en 04. `main` enlaza una presentación externa de ChatGPT. | El enlace externo depende de permisos y no es reproducible. Hay que retirarlo o reemplazarlo. |

## Revisión visual de los PDF

| Aspecto | Lean | Seis Sigma | DMAIC |
|---|---|---|---|
| Portada institucional | ✘ (encabezado en la pág. 1) | ✘ | ✘ |
| Índice | ✘ | ✘ | ✘ (15 págs. sin índice) |
| Jerarquía y numeración | ✔ secciones 01–07 | ✔ | ✔ 01–15 |
| Tablas | ✔ legibles | ✔ | ✔ |
| Figuras | ✘ ninguna | ✘ ninguna | ◐ solo barras de estados (pág. 5) |
| Márgenes y tipografía | ✔ | ✔ | ✔ (mucho espacio en blanco al pie de varias páginas) |
| Ortografía y redacción | ✔ cuidada; registro académico | ✔ | ✔ |
| Terminología | ✔ consistente | ✔ | ✔ |
| Citas | ◐ fuentes web (PMI, LEI, ASQ) sin formato APA ni bibliografía final | ◐ ídem; Anbari y Kwak (2004) bien contextualizado | ◐ fuentes del caso F1–F5, sin bibliografía metodológica |
| Conclusiones frente a resultados | ✔ prudentes | ✔ | ✔ |

## Representaciones visuales faltantes o mejorables

Solo se listan las que respaldan una conclusión:

| Herramienta | Lean | Seis Sigma | DMAIC (03) | 04 | Acción |
|---|---|---|---|---|---|
| SIPOC | — | — | tabla | tabla (paso 3 marcado) | Suficiente |
| VSM actual | **falta** (tabla) | — | — | — | **Crear** con iconografía VSM y «t = por medir» |
| VSM futuro | **falta** | — | — | — | **Crear**, rotulado como diseño |
| Diagrama de flujo / swim lane | — | — | **falta** | ✔ (reconstruido) | Llevar a 03 y rotular «no observado» |
| Pareto con curva acumulada | — | — | ◐ barras | ✔ combinado | Usar el de 04 |
| Ishikawa (espina) | — | — | tabla | ✔ figura | Usar la figura con la leyenda corregida |
| Árbol CTQ | — | **falta** (tabla) | — | — | Diagrama de árbol simple |
| Matriz RACI | — | ✔ tabla | — | — | Suficiente |
| Matriz de priorización | sin puntajes | — | sin puntajes | ✔ (propuesta) | Puntuar en equipo |
| Plan de control | — | — | tabla | ✔ tabla | Suficiente |
| Cronograma | ✘ | ✘ | ✘ (hitos sin fechas) | ◐ hitos en el charter | Gantt simple del piloto |
| Tablero | — | — | — | — | Opcional (Power BI) |

## Consistencia transversal (resumen; detalle en la matriz de hallazgos)

- **Empresa, proceso, población, fuentes y unidades:** consistentes en los tres trabajos y en 04.
- **Inconsistencias:**
  - Criterio D y sigma: 3,27 frente a 3,20 (AUD-002).
  - Roles, meta y puntajes: «pendiente» en los PDF de `main`, «propuesta» en 04 (AUD-006).
  - Postura sobre la causa raíz: hipótesis en 03, «respaldada» en 04 (AUD-003).
  - Beneficio: «no se presenta ahorro» en 03, S/ 255 en 04 (AUD-005).
- **Independencia:** los tres trabajos se pueden leer por separado. Repiten de forma idéntica el bloque «Datos y límites comunes» en los README; es aceptable.
