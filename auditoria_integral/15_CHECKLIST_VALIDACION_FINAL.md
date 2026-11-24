# 15 · Checklist de validación final

Marquen ✔ cuando se cumpla, o «PD» si queda como pendiente declarado (solo para los ítems R1 y R2).

| # | Verificación | Hallazgo / tarea | Método | Estado |
|---|---|---|---|---|
| 1 | Los resúmenes de los tres informes y de la lámina 2 declaran el origen confirmado del lote **o** la limitación | AUD-001 / T01 | Lectura | ☐ |
| 2 | La población del estudio está decidida y justificada en DECISIONES.md | AUD-018 / T02 | Lectura | ☐ |
| 3 | Las evidencias de hash y «herramietas» citan la versión del Data Mart (v3 `598f0ac1…` o posterior `a858d11b…`) | AUD-012 / T03 | `sha256sum`, `grep` | ☐ |
| 4 | Hay tabla de conciliación de totales de nota (13 notas) | AUD-008 / T04 | Anexo | ☐ |
| 5 | Medir declara «73 notas; 69 con detalle» | AUD-009 / T05 | `grep "69"` | ☐ |
| 6 | Las fechas de Lean y Seis Sigma son de tipo fecha | AUD-015 / T06 | `ISNUMBER` | ☐ |
| 7 | Principal según el contrato Q4: D = 30, 38 167,94 y 3,2724 σ («completitud sintáctica exploratoria»), igual en Seis Sigma, M2, lámina 5 e informe; D = 34 y D = 35 como sensibilidad separada | AUD-002 / T07 | `grep "3,2"` en todos | ☐ |
| 8 | Ningún documento afirma una causa raíz «confirmada» o «respaldada» basada solo en las asociaciones PEDIDO→REVISAR o numérica→REVISAR | AUD-003 / T08 | Lectura de A2, lámina 7, cap. 3 | ☐ |
| 9 | La simulación aparece como rango 4,96–12,12 % y rotulada «retrospectiva declarada» | AUD-004 / T09 | I2, lámina 9 | ☐ |
| 10 | El beneficio muestra 3 escenarios, incluido el negativo (−S/ 91,80) | AUD-005 / T10 | C2, lámina 11, costo-beneficio | ☐ |
| 11 | Roles, meta y puntajes aprobados y **consistentes** en los 3 trabajos y en 04 | AUD-006 / T11 | `grep "Pendiente de designación"` frente a los roles | ☐ |
| 12 | Hay acta de VOC **o** pendiente declarado | AUD-013 / T12 | Lectura | ☐ |
| 13 | La 5S está rotulada como ejercicio del taller | AUD-011 / T13 | Lean pág. 5 | ☐ |
| 14 | La línea base tiene IC (10,75–19,28 %) y nota sobre el efecto de diseño (1,69) | AUD-007 / T14 | Medir | ☐ |
| 15 | Hay tabla de vacíos por estrato | T15 | Analizar | ☐ |
| 16 | Hay tabla de variantes de catálogo | AUD-020 / T16 | Mejorar | ☐ |
| 17 | Kappa reportado **o** pendiente declarado | AUD-023 / T17 | Medir | ☐ |
| 18 | VSM actual y futuro con rótulos observado / derivado / hipotético | AUD-010 / T18 | Lean | ☐ |
| 19 | Existe `U3_Informe_HIDROCOM.docx` con la plantilla oficial, 12–18 págs., sin [EQUIPO] | AUD-014 / T19 | Abrir en Word | ☐ |
| 20 | El README no enlaza presentaciones externas | AUD-014 / T20 | `grep chatgpt` | ☐ |
| 21 | Los informes tienen portada, índice, bibliografía APA y figuras clave | AUD-022 / T21 | Inspección visual | ☐ |
| 22 | Cada «62 %» indica su unidad | AUD-021 / T22 | `grep "62 %"` | ☐ |
| 23 | Formato 04: M2 y A1 son fórmulas sobre una hoja Datos | AUD-017 / T23 | Inspeccionar celdas | ☐ |
| 24 | DMAIC 03: el Pareto se actualiza al cambiar Datos | AUD-016 / T24 | Prueba en una copia | ☐ |
| 25 | Formularios protegidos; tolerancia definida o pendiente declarado | AUD-024 / T25 | Prueba con 5 casos | ☐ |
| 26 | Un clon limpio regenera Excel, PPTX y figuras con `REPRODUCIR.md` | AUD-019 / T26 | Carpeta limpia | ☐ |
| 27 | Piloto real ejecutado **o** pendiente declarado en los 3 informes | T27 | Lectura | ☐ |
| 28 | `recalculo_independiente.py` reproduce todas las cifras publicadas | T28 | Ejecutar | ☐ |
| 29 | `auditoria_formulas.py`: 0 diferencias entre caché y recálculo, 0 errores | T28 | Ejecutar con copias recalculadas en Excel | ☐ |
| 30 | Comentario en el issue #1 con el commit final | — | GitHub | ☐ |
