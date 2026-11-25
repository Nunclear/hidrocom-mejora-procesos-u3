# 04 — Producto Final U3 (formato oficial del curso)

Entrega del 26-11-2026: **informe Word + Excel formato DMAIC + presentación PPTX**, usando las plantillas oficiales de la carpeta "Proyecto final - Sesión 7".

| Archivo | Estado | Responsable |
|---|---|---|
| `U3_Formato_DMAIC_HIDROCOM.xlsx` | Lleno (hojas 0, D1-D3, M1-M2, A1-A2, I1-I2, C1-C2) | Claude |
| `M1_Flujo_AS-IS_HIDROCOM.png` | Diagrama swim lane con el defecto en rojo (pegado en M1) | Claude |
| `U3_Informe_HIDROCOM.docx` | Completo: 13 páginas con la plantilla oficial; revisado por C y A | Codex B |
| `U3_Informe_HIDROCOM.pdf` | Exportado desde Word; 13 páginas revisadas visualmente por A | A |
| `U3_Presentacion_HIDROCOM.pptx` | Corregida: 13 láminas, S30 principal, escenarios y funciones pendientes; idéntica a 03 | A |
| `A2_Ishikawa_HIDROCOM.png`, `I1_Matriz_HIDROCOM.png` | Figuras usadas en la presentación (y disponibles para el informe) | Claude |
| `scripts/` | Código histórico de versiones previas; no ejecutar encima de los entregables activos | — |

## Cifras clave (contrato de datos del issue #1, comentarios 7146745531 y 7146867353)

| Indicador | Valor | Naturaleza |
|---|---|---|
| Población | 73 notas (69 con renglones), 262 renglones; 206 / 38 / 18 | Hecho |
| % REVISAR | 38/262 = 14,50 % (IC Wilson nominal 10,75–19,28 %, supone independencia) | Estado documental, no defecto |
| **Principal**: completitud sintáctica exploratoria | D = 30 de 786 campos → 38 167,94 por millón → σ equivalente 3,2724 (+1,5) | Calculado; **no es CTQ aprobado ni sigma empresarial** |
| Sensibilidad | D = 27 (sin EXCLUIR) 3,288 · D = 35 (con 5 diferencias) 3,2004 · D = 34 (sin NP-025138-01) 3,2141 | Análisis separados |
| Pareto de los 38 REVISAR | 13 / 7 / 7 / 6 / 5 (regla exclusiva; Datos!Y) | Condiciones documentales, no causas |
| Causa | Candidata: ausencia de reglas de captura y clasificación; **sin verificar** | Hipótesis |
| Simulación retrospectiva | 4,96 % (e = 100 %) · 7,35 % · 9,73 % · 12,12 % (e = 25 %) | Escenario |
| Beneficio anual neto | S/ 255 (base) · −S/ 91,80 (volumen según el rango de fechas) · S/ 67,50 (e = 50 %) · equilibrio 12,16 REVISAR/mes | Escenarios con supuestos |
| Roles, meta, puntajes | Pendientes de aprobación humana (Q5) | — |

El Excel calcula U, D, el Pareto, la sensibilidad, la simulación y los escenarios **con fórmulas** sobre la hoja `Datos`. Se puede verificar recalculando el libro.

La presentación activa está alineada por A: S30 principal, S34/S35 como sensibilidades, roles nominales pendientes, hipótesis sin causalidad demostrada y economía como escenarios. La revisión independiente final B/C sigue solicitada. El Word/PDF y PPTX de esta carpeta coinciden con las copias DMAIC de 03. Véanse el [contrato](../coordinacion/CONTRATO_DE_DATOS.md), el [informe de integración](../coordinacion/INFORME_INTEGRACION.md) y las [instrucciones de reproducción](../herramientas/README.md).
