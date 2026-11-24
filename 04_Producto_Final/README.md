# 04 — Producto Final U3 (formato oficial del curso)

Entrega del 26-11-2026: **informe Word + Excel formato DMAIC + presentación PPTX**, usando las plantillas oficiales de la carpeta "Proyecto final - Sesión 7".

| Archivo | Estado | Responsable |
|---|---|---|
| `U3_Formato_DMAIC_HIDROCOM.xlsx` | Lleno (hojas 0, D1-D3, M1-M2, A1-A2, I1-I2, C1-C2) | Claude |
| `M1_Flujo_AS-IS_HIDROCOM.png` | Diagrama swim lane con el defecto en rojo (pegado en M1) | Claude |
| `U3_Informe_HIDROCOM.docx` | Por hacer, con la plantilla oficial; las cifras se toman SOLO de este Excel | Codex (propuesto) |
| `U3_Presentacion_HIDROCOM.pptx` | Por hacer, con la plantilla oficial | Claude (propuesto) |
| `scripts/` | `llenar.py` y `flujo.py` regeneran el Excel y el diagrama a partir de `03_DMAIC/U3_DMAIC_HIDROCOM.xlsx` | — |

## Cifras clave (fuente única: este Excel)

| Indicador | Valor |
|---|---|
| Renglones del lote (U) | 262 |
| REVISAR (Y del proyecto) | 38 = 14,50 % |
| CTQ | renglón completo y coherente: 3 oportunidades (cantidad, precio, importe) |
| Defectos (D) | 35, en 22 renglones |
| DPMO / sigma | 44 529 / ≈ 3,20 σ |
| Pareto | PEDIDO 13 · incompletos 7 · dudosa 7 · sin motivo 6 · diferencia 5 |
| Causa raíz confirmada | sin reglas estandarizadas de captura y clasificación: 13/13 PEDIDO y 21/22 renglones con defecto numérico van a REVISAR (25 de 38 = 65,8 %) |
| Causa descartada | fechas estimadas: 16,0 % vs. 12,0 % REVISAR (real) |
| Simulación de los controles | REVISAR 14,50 % → 4,96 % (13/262) |
| Beneficio anualizado estimado | (47,50 − 16,25) × 12 − 120 = **S/ 255** (horas liberadas, con supuestos) |

La simulación es una **prueba de escritorio retrospectiva**, no un piloto en campo. Los textos con `[PROPUESTA — confirmar en DECISIONES.md]` deben aprobarse por el equipo antes de la entrega.
