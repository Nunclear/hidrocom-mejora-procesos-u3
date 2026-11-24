# 00 · Resumen ejecutivo — Auditoría integral HIDROCOM KALLPA

- **Auditor:** Claude (Claude Code), por encargo transmitido en el issue #1 (prompt en el commit `c92ce0b`).
- **Fecha:** 24-11-2026.
- **Ramas auditadas:** `main` @ `e3b5a60`, `claude/excel-dmaic-oficial` @ `4d1ec0d`, `codex/informe-y-costo-beneficio` @ `b9d921b` (sin entregables propios publicados al corte).
- **Originales:** no se modificaron.

## Calificaciones (escenario: propuesta académica de mejora)

| Trabajo | Nota actual | Potencial sin datos nuevos | Potencial con datos de la empresa + piloto |
|---|---:|---:|---:|
| Lean | **12,0 / 20** | 15,0 | 18,5 |
| Seis Sigma | **13,0 / 20** | 16,0 | 18,5 |
| DMAIC (03 + producto final 04) | **13,0 / 20** | 16,5 | 19,0 |
| **Global** | **12,7 / 20** | ≈ 15,8 | ≈ 18,7 |

La evaluación previa de 16,5 no se tomó como referencia. La diferencia se explica sobre todo por la procedencia del lote, las evidencias no reproducibles, las afirmaciones causales y económicas del producto final y la falta del informe Word oficial.

## Cobertura

- **Archivos inspeccionados:**
  - 24 del repositorio (3 ramas);
  - 19 del ZIP del curso (requisitos y plantillas);
  - 12 del paquete local del usuario (hashes; 1 comparado celda por celda).
- **Fórmulas verificadas:** **1 475**, todas recalculadas en Excel. 0 diferencias entre caché y recálculo, 0 errores. Además, todos los indicadores publicados se recalcularon de forma independiente en Python.
- **Hallazgos:** **24**. **P0 = 1 · P1 = 9 · P2 = 9 · P3 = 5** (`09_MATRIZ_HALLAZGOS.csv`).

## Resultados recalculados (todos coinciden con lo publicado)

- 73 notas (**69 con renglones**) · 262 renglones · 206 / 38 / 18 · 14,50 % REVISAR (IC 95 % 10,8–19,3 %) · S/ 26 509,70.
- D = 30 → DPMO 38 167,94 → 3,2724 σ.
- D = 35 → 44 529,26 → 3,2004 σ.
- D = 34 (propuesto, sin el artefacto millar) → 43 257,0 → 3,2141 σ.
- Pareto 13/7/7/6/5 reproducible (0 discrepancias). 45/73 = 61,64 % de fechas estimadas o discordantes.
- **Nuevo:** ICC intra-nota 0,246 (efecto de diseño 1,69). 10 notas con total ≠ suma de renglones, con 3 discrepancias entre hojas. 169 nombres de producto con 6 grupos de variantes ortográficas.

## Principales problemas

1. **P0 · AUD-001:** **70 de 73 notas** son anteriores al inicio de actividades declarado (09/03/2026). Los datos describen la calidad documental de un lote digitalizado retrospectivamente, **no el proceso actual de la empresa**, hasta que el dueño confirme su origen.
2. **P1 · AUD-012:** las dos «evidencias verificadas» que repiten los tres trabajos («hash del Excel distinto» y «herramietas» en el CSV) **no se reproducen**. Con la copia del paquete del usuario, el hash coincide con `auditoria.json`, los 9 CSV también, y «herramietas» no aparece.
3. **P1 · AUD-003, -004, -005 (producto final 04):**
   - la «causa raíz respaldada» se apoya en asociaciones **por construcción** (13/13 y 21/22);
   - la simulación 14,50 → 4,96 % es el máximo teórico (el rango real es 4,96–12,12 %);
   - el beneficio de S/ 255 pasa a **−S/ 91,80** con el volumen implícito en el rango de fechas.
4. **P1 · AUD-002:** hay dos sigmas en circulación (3,27 y 3,20) sin conciliar; además, una diferencia de importe es un artefacto de la base «millar».
5. **P1 · AUD-014, -006, -010, -018:**
   - falta el informe Word oficial;
   - roles y meta son contradictorios entre `main` y 04;
   - el VSM no tiene tiempos ni estado futuro;
   - existe una versión ampliada de los datos (510 notas) no considerada al definir la población.

## Fortalezas

- Disciplina excepcional para no inventar datos y separar hecho de hipótesis (`main`).
- Cifras 100 % reproducibles y fórmulas robustas: manejan los vacíos y la división entre cero.
- Pareto excluyente bien documentado; DPMO correctamente rotulado como exploratorio.
- Producto final 04 en el formato oficial con plan de control completo.

## Correcciones ejecutables ya, sin la empresa

Reformular la causa (T08), simulación como rango (T09), sensibilidad del beneficio (T10), un único CTQ (T07), IC y efecto de diseño (T14), estratificación de faltantes y catálogo (T15, T16), VSM derivado y futuro (T18), informe Word (T19), formatos y reproducibilidad (T20–T26).

## Correcciones que requieren a la empresa o al equipo

Origen del lote (T01), población (T02), copia del paquete del compañero (T03), roles y meta aprobados (T11), VOC (T12), MSA con originales (T17), piloto real (T27).

## Limitaciones de esta auditoría

- No se revisaron las 74 imágenes originales, el manual `SEM2_…COMPLETADO.docx` ni `Antecedentes_y_alcance.md`: no se localizaron.
- No se analizó el contenido de la versión ampliada «DataCompleta». Solo se leyeron los totales de su `auditoria.json`, para no exponer material marcado como privado en un repositorio público.
- Los formularios Poka-Yoke se evaluaron por su lógica, sin entradas reales.
- El auditor es también autor del producto final 04: hay riesgo de sesgo. Se mitigó aplicando la misma vara, y 4 de los 9 hallazgos P1 son sobre ese trabajo.
- No se verificó la rúbrica oficial con puntajes (no está en el ZIP).

## Entregables

Carpeta `auditoria_integral/` (00–15). Evidencias y scripts en `14_EVIDENCIAS_AUDITORIA/`:
- `recalculo_independiente.py` y `resultados_recalculo.json`;
- `auditoria_formulas.py` y `formulas_inventario.csv`;
- `verificacion_hashes_paquete_local.txt`;
- texto y miniaturas de los PDF;
- `generar_hallazgos.py`.
