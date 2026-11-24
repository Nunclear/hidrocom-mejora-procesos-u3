# 07 · Auditoría de Excel y automatización

## Método

1. Se hicieron copias de los 4 libros (los originales quedaron intactos).
2. Se recalcularon en **Microsoft Excel** (COM, `CalculateFullRebuild`) y se guardaron como `recalc_*.xlsx`.
3. Con `14_EVIDENCIAS_AUDITORIA/auditoria_formulas.py` se comparó, fórmula por fórmula, el valor en caché frente al valor recalculado por el motor.
4. Se buscaron celdas con error (`SpecialCells(xlCellTypeFormulas, xlErrors)`), referencias externas y funciones volátiles.
5. Los indicadores clave se contrastaron con un cálculo independiente en Python (`recalculo_independiente.py`).

Inventario completo de fórmulas con su dictamen: `14_EVIDENCIAS_AUDITORIA/formulas_inventario.csv` (1 475 filas).

| Libro | Fórmulas | Caché ≠ recálculo | Errores | Externas | Volátiles | Validación de datos | Formato condicional | Protección |
|---|---:|---:|---:|---:|---:|---|---|---|
| U3_Lean_HIDROCOM.xlsx | 25 | 0 | 0 | 0 | 0 | 2 hojas | 0 | No |
| U3_Seis_Sigma_HIDROCOM.xlsx | 1 328 | 0 | 0 | 0 | 0 | 0 | 0 | No |
| U3_DMAIC_HIDROCOM.xlsx | 94 | 0 | 0 | 0 | 0 | 3 hojas | 1 | No |
| U3_Formato_DMAIC_HIDROCOM.xlsx (04) | 28 | 0 | 0 | 0 | 0 | 0 | 0 | No |
| **Total** | **1 475** | **0** | **0** | **0** | **0** | | | |

**Verificado:** las 1 475 fórmulas se ejecutaron en Excel y coinciden con su caché. Las fórmulas de los indicadores publicados (DPMO, sigma, Pareto, proporciones, 61,64 %, conteos) coinciden además con el cálculo independiente en Python.

**No verificado:**
- Comportamiento de los formularios Validar y PokaYoke con entradas reales: están vacíos y solo se revisó su lógica.
- Compatibilidad con LibreOffice o Google Sheets.

## Revisión lógica

| Libro / hoja | Fórmula | Dictamen |
|---|---|---|
| DMAIC › Medir B6:B15 | COUNTA / COUNTIFS sobre Datos y Fechas | ✔ Rangos completos (filas 6–267 y 6–78) |
| DMAIC › Medir B25:B26 | DPMO y sigma con validación de entradas e «n.a.: extremo» | ✔ Robusta (evita la inversa normal en 0 y 10⁶) |
| DMAIC › Analizar B6:D10 | COUNTIFS sobre **Pendientes!H** | ◐ H contiene la clasificación **tecleada como valor**, no derivada por fórmula desde Datos. Es reproducible (0 discrepancias con el recálculo), pero no es dinámica (AUD-016). |
| DMAIC › Control B8 | Evita dividir entre 0 («n.a.: sin cierres») | ✔ |
| DMAIC › Beneficios B13:B14 | Validación de rangos y «PENDIENTE» | ✔ Buena práctica: no convierte vacíos en cero |
| DMAIC › Validar / Lean › PokaYoke K9:K13 | Estado del registro con tolerancia | ✔ La lógica es correcta. ◐ La tolerancia (B4 / B5) está vacía, así que los formularios no pueden emitir «VALIDADO». |
| Lean › VSM B16:B20 | Lead time, VA y PCE con controles de signo | ✔ Correcto; sin datos |
| Lean › 5S C13:D13 | SUM/5 | ✔ 0,2 → 0,8 |
| Seis Sigma › Metricas C30:E291 | `IF(ISBLANK(Datos!I6),1,0)` | ✔ Equivale a «celda nula». No detecta "" ni espacios, pero no los hay. |
| Seis Sigma › Metricas C6 | O = 3 constante | ✔ Declarado |
| Formato 04 › M2 B8:B10 | U, D y O **tecleados por script** | ◐ No hay vínculo con los datos (la plantilla no tiene hoja de datos). Solo se reproducen ejecutando `llenar.py` (AUD-017). |
| Formato 04 › A1 B5:B9 | Frecuencias del Pareto tecleadas | ◐ Ídem |
| Formato 04 › C2 B8 | `(B5−B6)×12−B7` | ✔ La fórmula de la plantilla es correcta; los supuestos son el problema (AUD-005) |

## Otros problemas

- **Fechas como texto** en las hojas Datos de Lean y Seis Sigma (AUD-015). No se pueden filtrar por fecha ni calcular con ellas.
- **Sin protección** de fórmulas en ningún libro. Un usuario puede sobrescribir los cálculos.
- **Sin tablas estructuradas** (ListObjects). Los rangos son fijos (6–267), así que un lote nuevo exige editar las fórmulas.
- **Gráficos:** el Pareto del Formato 04 es combinado y nativo (barras + % acumulado). El de DMAIC 03 solo tiene barras. Lean y Seis Sigma no tienen gráficos.

## Oportunidades de automatización

Todas son ejecutables con los archivos existentes.

1. Convertir Datos en una **tabla estructurada** y escribir las fórmulas con referencias estructuradas, para que funcionen con cualquier número de renglones.
2. **Derivar la «condición principal»** con una fórmula IFS que replique la regla de prioridad, en lugar del valor tecleado en Pendientes!H.
3. Añadir al libro oficial una **hoja Datos** y vincular U, D y O y el Pareto con COUNTIFS. Así se elimina la dependencia del script.
4. **Tabla de sensibilidad del DPMO** (D = 30/34/35 × con o sin EXCLUIR) y **del beneficio** (volumen, minutos, costo hora y eficacia).
5. **Reporte de excepciones** con formato condicional sobre Datos:
   - vacío en cantidad, precio o importe;
   - diferencia ≠ 0;
   - base kg o millar;
   - nota con total ≠ suma de renglones.
6. **Validación de datos** en Validar: listas cerradas para base y motivo, y números ≥ 0.
7. Proteger las hojas de cálculo y dejar desbloqueadas solo las celdas amarillas.
8. **Tablero de calidad** (hoja o Power BI, que el equipo ya usa) con % REVISAR por lote, DPMO, cola por motivo y antigüedad.
