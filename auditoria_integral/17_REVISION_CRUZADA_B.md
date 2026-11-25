# 17 · Revisión cruzada de C (Claude) sobre los entregables de B (Codex)

Objeto: commit `3b3da11` de `codex/informe-y-costo-beneficio`:
- `04_Producto_Final/U3_Informe_HIDROCOM.docx`
- `04_Producto_Final/Modelo_Costo_Beneficio_HIDROCOM.json`

Fecha: 24-11-2026. No se editó ningún archivo de B.

## Modelo de costo-beneficio (JSON)

**Método.** Se reimplementaron en Python las fórmulas del JSON y se recalcularon los 7 casos de prueba. También se replicaron en el Formato 04 (`C2_Beneficios_Lecciones!A21:G28`, con fórmulas) y se recalcularon en Excel.

| Caso | REVISAR esperado | % | Neto anual (S/) | VAN ilustrativo | Dictamen |
|---|---:|---:|---:|---:|---|
| Base (1 lote/mes, e = 100 %) | 13 | 4,96 | 255,00 | 224,04 | ✔ |
| e = 75 % | 19,25 | 7,35 | 161,25 | 138,03 | ✔ |
| e = 50 % | 25,5 | 9,73 | 67,50 | 52,02 | ✔ |
| e = 25 % | 31,75 | 12,12 | −26,25 | −33,99 | ✔ |
| Volumen bajo (1/13,3) | 13 | 4,96 | −91,80 | −94,13 | ✔ |
| e = 0 | 38 | 14,50 | −120,00 | −120,00 | ✔ |
| Equilibrio | 8 evitados = 12,16 iniciales = 0,32 lotes/mes | — | 0 | — | ✔ |

**Observaciones:**
- **R-B1 (P2).** `costo_recurrente_anual_pen = 0`. La regla del propio proyecto (`03_DMAIC › Beneficios!C11`) dice «Cero solo si está confirmado». Hay que rotularlo como «no estimado» y no como 0, o añadir un escenario con costo recurrente. En C2 se rotuló «costo recurrente: no estimado».
- **R-B2 (P3).** `tasa_descuento_ilustrativa = 0,09` no tiene fuente. Si el VAN aparece en el informe, debe decir «ilustrativo, tasa sin fuente», o retirarse. Con un horizonte de un año el VAN añade poco.

## Informe Word (13 págs.)

**Método.** Se exportó a PDF con Word, se revisaron las 13 páginas como miniaturas y se buscaron en el texto los términos del contrato.

**Cumple:**
- D = 30 como principal (38 167,94 / 3,2724), con 34 y 35 como sensibilidad;
- 73 notas, de las que 69 tienen detalle;
- 78,63 % distinguido del rendimiento de primera pasada;
- «causa candidata priorizada para el piloto»;
- fechas como «comparación descriptiva, sin veredicto causal»;
- simulación de 4,96 % a 12,12 % y beneficio de −S/ 91,80 a S/ 255;
- dos publicaciones del Data Mart conciliadas;
- sin nombres asignados a roles y sin recuadros [EQUIPO].

| ID | Observación | Prioridad | Propuesta |
|---|---|---|---|
| R-B3 | Las págs. 2 y 3 hablan de «meta técnica del piloto» y «meta de diseño», pero no dicen «pendiente de aprobación» (Q5) | P2 | Añadir «propuesta del equipo, pendiente de aprobación del dueño del proceso» |
| R-B4 | La portada dice «Juliaca, Perú · 2026». No se encontró la fuente de la sede en el material revisado | P2 | Confirmarlo con el equipo o retirarlo |
| R-B5 | No se mencionan el intervalo de confianza ni la dependencia intra-nota (PM-05 / AUD-007) | P3 | Una línea en el cap. 2: «IC Wilson nominal 10,75–19,28 % (supone independencia; ICC 0,246); el censo no acredita representatividad» |
| R-B6 | No incorpora el resultado de **PM-08**, publicado en `681b53d` después de su commit: los 30 vacíos ya estaban en la primera transcripción, 37/38 REVISAR se asignaron al transcribir y la digitalización fue el 17–18-11-2026 | P2 | Incorporarlo en el cap. 3 (verificación) y en el alcance |
| R-B7 | La figura Ishikawa (pág. 8) usa la leyenda antigua «respaldada por datos del lote» | P3 | `A2_Ishikawa_HIDROCOM.png` ya regenerado con la leyenda «condición documental asociada a REVISAR por construcción (no prueba causa)»; reemplazar la imagen |
| R-B8 | La presentación `U3_Presentacion_HIDROCOM.pptx` sigue con D = 35 / 3,20 σ como principal, roles con nombre y «causa respaldada» | P1 | Pendiente de B (archivo de su propiedad) |

**Dictamen:** el Word es apto para la integración tras corregir R-B3, R-B4 y R-B6. El modelo económico es correcto, con R-B1 y R-B2 como observaciones.

## Actualización: revisión de `f7f5dea` (24-11-2026, 18:11)

**Objeto:**
- Nuevo libro `05_Costo_Beneficio/Costo_Beneficio_HIDROCOM.xlsx` (propiedad de B).
- Word actualizado.

**Método:** se recalculó el libro en Excel sobre una copia y se leyeron todas sus fórmulas. Se cotejó contra la guía de costo-beneficio del curso y se buscaron los términos clave en el texto del Word.

| Comprobación | Resultado |
|---|---|
| Errores tras recalcular | 0 |
| Escenarios (hoja 4) | −91,80 · −26,25 · 67,50 · 161,25 · 255,00 · 255,00. **Idénticos** al JSON, a mi recálculo y a C2 del Formato 04 |
| Equilibrio | 8 evitados = 12,16 iniciales = 0,32 lotes/mes ✔ |
| Control interno «Coherencia del escenario base» | «Coincide» ✔ |
| **R-B2** (tasa del 9 % sin fuente) | **Resuelto.** La guía del curso, `Guia_Costo_Beneficio_Proyectos_Mejora.xlsx › 1. Supuestos` fila 8, indica «Tasa de descuento anual 9,0 %» |
| **R-B1** (costo recurrente = 0) | **Atenuado (P3).** Celda D15: «No incorporado… Introducir un monto si el piloto permite estimarlo». Se recomienda escribir «no estimado» en lugar de 0. |
| **R-B6** (PM-08 en el Word) | **Resuelto.** El cap. 3 dice que los 30 vacíos ya estaban en la primera captura y que 37 de 38 REVISAR… |
| **R-B3** (meta sin «pendiente de aprobación») | **Abierto.** El Word sigue diciendo «meta técnica del piloto» y «meta de diseño» |
| **R-B4** («Juliaca, Perú») | **Abierto** |
| **R-B8** (presentación desalineada) | **Abierto (P1)** |
| Nueva **R-B9 (P3)** | «TIR equivalente de un periodo» y «ROI simple» = 212,5 % salen de supuestos y del escenario más favorable. Hay que presentarlos junto al escenario de volumen bajo, con neto negativo, o rotularlos «escenario base supuesto». |

**Dictamen:** el libro de costo-beneficio es correcto y trazable. El Word queda apto para integrarse si se cierran R-B3 y R-B4. La presentación debe alinearse (R-B8).

## Actualización: `8187187`

Word: «Juliaca» retirado (R-B4 ✔), meta con «pendiente de aprobación» (R-B3 ✔) y mención al IC de Wilson (R-B5 ✔). Libro de costo-beneficio: costo recurrente vacío y rotulado «No estimado» (R-B1 ✔); escenarios sin cambios y control «Coincide», 0 errores tras recalcular. **Sigue abierta: R-B8 (P1, presentación).** R-B9 no se verificó.

## Actualización: `e2287cb`

R-B9 ✔. La hoja Evaluación compara el escenario base (S/ 255; ROI/TIR 212,50 %) con el de volumen bajo (−S/ 91,80; ROI/TIR −76,50 %). Comprobación aritmética: 255/120 = 2,125 y −91,80/120 = −0,765. **Solo queda abierta R-B8 (presentación).**
