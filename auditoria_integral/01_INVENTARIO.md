# 01 · Inventario de archivos y dependencias

**Alcance auditado** (24-11-2026, America/Lima):

| Rama | Commit | Contenido |
|---|---|---|
| `main` | `e3b5a60` | Trabajos Lean, Seis Sigma y DMAIC (PDF + Excel), README raíz |
| `claude/excel-dmaic-oficial` | `4d1ec0d` | `main` + `04_Producto_Final/` + `COORDINACION_AGENTES.md` + `PROMPT_AUDITORIA_INTEGRAL_HIDROCOM.md` |
| `codex/informe-y-costo-beneficio` | `b9d921b` | `main` + `COORDINACION_AGENTES.md`. **No contiene aún informe Word ni costo-beneficio publicados.** |

También se inspeccionó el ZIP del curso `B-Learning_Mejora_de_procesos_Unidades_2_y_3.zip` (19 archivos: diapositivas, guías, datos de talleres y las 4 plantillas del producto final de la Sesión 7), que define los requisitos oficiales.

Listado completo con tamaños por rama: `14_EVIDENCIAS_AUDITORIA/inventario_git.txt`. Historial: `14_EVIDENCIAS_AUDITORIA/historial_git.txt`.

## Inventario

| Archivo | Ruta | Función | Trabajo | Fuente de datos | Estado | Problemas |
|---|---|---|---|---|---|---|
| README.md | raíz | Contexto, datos, DMAIC narrado, fuentes | Transversal | Paquete suministrado (no versionado) | Completo | Enlace a presentación en ChatGPT (externa, no reproducible) — AUD-014 |
| U3_Lean_HIDROCOM.pdf | 01_Lean | Informe Lean (7 págs.) | Lean | Datos del lote | Completo como diagnóstico | Sin VSM con tiempos; sin figuras; no usa plantilla Word — AUD-010, AUD-022 |
| U3_Lean_HIDROCOM.xlsx | 01_Lean | Lean, VSM, desperdicios, 5S, Kaizen, Poka-Yoke, Datos (25 fórmulas) | Lean | Hoja Datos (262 filas) | Plantillas sin entradas | Fechas como texto — AUD-015; Kaizen sin puntajes |
| Evidencia_5S.csv | 01_Lean | Puntaje 5S antes/después del repositorio | Lean | Elaboración propia | Completo | 5S sobre carpeta académica, no sobre la empresa — AUD-011 |
| README.md | 01_Lean | Guía | Lean | — | Completo | — |
| U3_Seis_Sigma_HIDROCOM.pdf | 02_Seis_Sigma | Informe Seis Sigma (7 págs.) | Seis Sigma | Datos del lote | Completo como diagnóstico | Sin VOC; DPMO exploratorio 3,27 σ distinto del 3,20 σ de 04 — AUD-002, AUD-013 |
| U3_Seis_Sigma_HIDROCOM.xlsx | 02_Seis_Sigma | Selección, roles/RACI, CTQ, métricas (1 328 fórmulas), Datos | Seis Sigma | Hoja Datos | Completo | Fechas como texto — AUD-015 |
| README.md | 02_Seis_Sigma | Guía | Seis Sigma | — | Completo | — |
| U3_DMAIC_HIDROCOM.pdf | 03_DMAIC | Informe DMAIC (15 págs.) | DMAIC | Datos del lote | Completo como diagnóstico | Formato no oficial; sin Pareto gráfico, Ishikawa gráfico ni flujo — AUD-014, AUD-022 |
| U3_DMAIC_HIDROCOM.xlsx | 03_DMAIC | 13 hojas, 94 fórmulas, fuente principal de datos | DMAIC | **Fuente de verdad versionada**: Datos, Comprobantes, Fechas | Completo | Pareto depende de clasificación tecleada en Pendientes!H — AUD-016 |
| README.md | 03_DMAIC | Guía | DMAIC | — | Completo | — |
| U3_Formato_DMAIC_HIDROCOM.xlsx | 04_Producto_Final | Plantilla oficial llena (D1–C2) | DMAIC (producto final) | Valores copiados por script desde 03_DMAIC | Completo | Valores tecleados sin vínculo a datos — AUD-017; afirmaciones causales y simulación — AUD-003/004/005 |
| U3_Presentacion_HIDROCOM.pptx | 04_Producto_Final | Presentación oficial 13 láminas | DMAIC (producto final) | Excel oficial | Completo | Hereda AUD-003/004/005/006 |
| M1/A2/I1 *.png | 04_Producto_Final | Flujo, Ishikawa, matriz | DMAIC | Elaboración propia | Completo | Flujo AS-IS reconstruido, no observado — AUD-010 |
| DECISIONES.md | 04_Producto_Final | Decisiones pendientes del equipo | DMAIC | — | Abierto | Ninguna decisión aprobada — AUD-006 |
| scripts/*.py | 04_Producto_Final/scripts | Regeneran Excel, PPTX y figuras | DMAIC | 03_DMAIC xlsx + plantillas del ZIP | Completo | Dependen de plantillas del ZIP no versionadas — AUD-019 |
| COORDINACION_AGENTES.md | raíz (ramas) | Coordinación | — | — | Informativo | — |
| PROMPT_AUDITORIA_INTEGRAL_HIDROCOM.md | raíz (rama claude) | Encargo de esta auditoría | — | — | Informativo | — |

## Fuente de verdad por conjunto de datos

| Conjunto | Fuente original (declarada) | Copia versionada usada | ¿Disponible para el auditor? |
|---|---|---|---|
| Detalle de renglones (262) | `Comprobantes_Revisados.xlsx` › Detalle_Productos | `03_DMAIC/U3_DMAIC_HIDROCOM.xlsx` › Datos (copias idénticas en Lean y Seis Sigma, salvo el tipo de dato de la fecha) | Solo la copia |
| Notas (73) | › Comprobantes | DMAIC › Comprobantes | Solo la copia |
| Fechas (73) | › Fechas_y_Series | DMAIC › Fechas | Solo la copia |
| Pendientes (38) | Derivado | DMAIC › Pendientes | Sí |
| Fuente Excel, Data Mart (9 CSV), `auditoria.json` | Paquete suministrado | **No versionado** | **Sí, copia local del usuario** (entrega Power BI 22-11-2026). Hashes verificados (02_AUDITORIA_DATOS). |
| Imágenes originales, manual `SEM2_…COMPLETADO.docx`, `Antecedentes_y_alcance.md` | Paquete suministrado | No versionado | **No localizados**; no revisados |
| Versión ampliada «DataCompleta» (510 comprobantes, 1 846 renglones) | Equipo del usuario | No versionada | Solo se leyeron los totales de su `auditoria.json` (AUD-018) |

## Archivos duplicados, obsoletos o sin referencia

- La hoja Datos está triplicada (Lean, Seis Sigma, DMAIC). El contenido es idéntico, pero en Lean y Seis Sigma la fecha está guardada como texto.
- Las versiones integradas previas solo existen en el historial Git (commit `3c42ce7`). No hay archivos obsoletos activos.
- La presentación DMAIC de `main` es un enlace externo, no un archivo del repositorio.
