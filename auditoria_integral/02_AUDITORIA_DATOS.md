# 02 · Auditoría de datos

Recálculo independiente con `14_EVIDENCIAS_AUDITORIA/recalculo_independiente.py` (Python + openpyxl + SciPy) sobre las hojas Datos, Comprobantes, Fechas y Pendientes de `03_DMAIC/U3_DMAIC_HIDROCOM.xlsx`. La salida completa está en `resultados_recalculo.json` y `resultados_recalculo.txt`.

**Acceso a fuentes.** El repositorio no versiona los originales. Con autorización del usuario se localizó en su equipo una copia del paquete (`Fuente/` y `DataMart/Publicado/` de la entrega de Power BI del 22-11-2026). Resultado:

- `Comprobantes_Revisados.xlsx` › Detalle_Productos coincide con `03_DMAIC/.../Datos`: **0 celdas distintas** en 262 × 24.
- La huella SHA-256 local del Excel fuente (`ac6ab323…`) **coincide** con la declarada en `auditoria.json`. **También coinciden los 9 CSV y las 5 fuentes.**
- «herramietas» **no aparece** en ningún CSV publicado. NP-025089-02 figura con la categoría «herramientas».

Las dos «evidencias verificadas» que repiten los tres informes y el README («hash del Excel distinto del declarado» y «categoría herramietas en el CSV») **no se reproducen con la copia del paquete del usuario**. Ver `14_EVIDENCIAS_AUDITORIA/verificacion_hashes_paquete_local.txt`.

**Conciliación posterior (comentario 7146745531 del issue #1):** el Excel fuente es idéntico en ambas copias (`ac6ab323…`). Lo que difiere es la **publicación del Data Mart**. En el paquete usado en `main` (`Grupo_Hidrocom_Kallpa_Recopilacion.zip` → `PowerBI_y_Data_Corregida_20261121_v3.zip`), `auditoria.json` (`598f0ac1…`) declara `sha256_fuente = 4bd79c0b…`, distinto del Excel, y Productos.csv (`7a362e0e…`) contiene «herramietas» para NP-025089-02. En la copia del usuario (entrega Power BI del 22-11-2026, `auditoria.json` `a858d11b…`, Productos.csv `6eb47b29…`), ambas cosas están corregidas. **Las dos evidencias son válidas para la versión v3 y no aplican a la versión posterior.** AUD-012 queda como «dos versiones del Data Mart sin identificar en los informes» (P2).

Las imágenes originales (74 fotos referidas) no se revisaron.

**Hallazgo de alcance (AUD-018).** En el mismo equipo existe una versión ampliada del Data Mart (entrega «DataCompleta» del 22-11-2026). Su `auditoria.json` declara 510 comprobantes, 1 846 renglones y fechas de 2021-01-03 a 2026-08-07. El proyecto analiza solo el lote de 73 notas. El equipo debe decidir y justificar cuál es la población del estudio. Esta auditoría no analizó la versión ampliada; solo se leyeron sus totales agregados.

## Matriz de trazabilidad

| Indicador | Fuente | Fórmula | Publicado | Recalculado | Dif. | Dictamen |
|---|---|---|---|---|---|---|
| Notas | Comprobantes | filas únicas | 73 | 73 | 0 | Verificado |
| Notas con al menos un renglón | Datos | id_comprobante distintos | no publicado | **69** | — | Hallazgo AUD-009: 4 notas sin detalle (NP-025111, -127, -137, -140; tres de ellas en estado PEDIDO) |
| Renglones | Datos | filas, id_detalle únicos | 262 | 262 (0 duplicados; todos los id_detalle coinciden con su nota) | 0 | Verificado |
| DISPONIBLE / REVISAR / EXCLUIR | Datos.uso_importe | conteo | 206 / 38 / 18 | 206 / 38 / 18 | 0 | Verificado |
| % REVISAR | | 38/262 | 14,50 % | 14,50 % (IC 95 % Wilson 10,8–19,3 %; con efecto de diseño 1,69 el intervalo es más ancho) | 0 | Verificado; falta comunicar la incertidumbre (AUD-007) |
| Importe DISPONIBLE | Datos.subtotal | suma | S/ 26 509,70 | S/ 26 509,70 | 0 | Verificado (es importe documental, no ventas) |
| Oportunidades U×O | | 262×3 | 786 | 786 | 0 | Verificado (oportunidades sintácticas, ver Seis Sigma) |
| Vacíos cantidad/precio/importe | Datos | celdas nulas | 5/16/9 = 30 | 5/16/9 = 30 | 0 | Verificado |
| Renglones con ≥1 vacío | | | 17 | 17 | 0 | Verificado |
| DPMO (solo vacíos) | | 30/786×10⁶ | 38 167,94 | 38 167,94 | 0 | Verificado |
| Sigma (solo vacíos, +1,5) | | NORM.S.INV(1−DPO)+1,5 | 3,2724 | 3,2724 | 0 | Verificado; la convención está declarada |
| Sin EXCLUIR (sensibilidad) | | 27/732 | 36 885,25 / 3,288 | 36 885,25 / 3,288 | 0 | Verificado |
| D con diferencias de importe | Datos | 30 + 5 | 35 (04) | 35 | 0 | Verificado, pero **AUD-002**: una de las 5 diferencias es un artefacto de la base millar |
| DPMO / sigma (criterio 35) | | 35/786 | 44 529 / 3,20 | 44 529,26 / 3,2004 | 0 | Verificado; criterio distinto del de Seis Sigma |
| Pareto de los 38 REVISAR | Datos (regla exclusiva) | prioridad PEDIDO > vacíos > diferencia > observación > resto | 13/7/7/6/5 | 13/7/7/6/5; **0 discrepancias** contra Pendientes!H | 0 | Verificado y reproducible |
| PEDIDO ∩ REVISAR | | | 13/13 | 13/13 | 0 | Verificado (asociación **definicional**, AUD-003) |
| Numéricas ∩ REVISAR | | | 21/22 | 21/22 (la restante es NP-025128-06, EXCLUIR) | 0 | Verificado (asociación definicional) |
| Unión PEDIDO ∪ numéricas en REVISAR | | | 25 | 25 (9 cumplen ambas) | 0 | Verificado |
| Fechas: estimada / real / año discordante (notas) | Fechas | conteo | 39/28/6 | 39/28/6 | 0 | Verificado |
| Fechas estimadas o discordantes / notas | | 45/73 | 61,64 % | 61,64 % | 0 | Verificado |
| Renglones con fecha estimada | Datos.tipo_fecha | | «62 %» (04) | 162/262 = 61,83 % | — | Mezcla de unidades en 04 (AUD-021) |
| Rango de fechas | Comprobantes | | 27/01/2025–09/03/2026 | igual | 0 | Verificado |
| Notas anteriores al inicio declarado (09/03/2026) | Comprobantes | | no cuantificado | **70 de 73** | — | **AUD-001 (P0)** |
| REVISAR según tipo de fecha | Datos | 2×2 | 16,0 % vs 12,0 % | 26/162 vs 12/100; Fisher p = 0,47 | 0 | Verificado; comparación descriptiva sin poder para concluir |

## Integridad: hallazgos no reportados por el proyecto

1. **Coherencia aritmética.** Se recalculó cantidad × precio / base frente al subtotal. Hay 7 incoherencias:
   - 5 están marcadas en la fuente.
   - 2 no lo están: NP-025066-04 y NP-025066-06, ambas con base «kg», EXCLUIR. La fuente calcula 375 con un factor no documentado. La regla de conversión por kg no está escrita (AUD-002).
   - **NP-025138-01** (2 000 × 0,24 con base «millar») es una «diferencia» de S/ 479,52 que desaparece si el precio es unitario: 2 000 × 0,24 = 480 coincide con el subtotal. Es un defecto de la etiqueta de base, no del importe.
2. **Total de nota frente a renglones.** La fuente marca 10 notas con `diferencia_total ≠ 0`. El recálculo con el detalle también da 10, pero **el conjunto es distinto**:
   - NP-025126 (total 430 frente a 1 130 en renglones) no está marcada.
   - NP-025068 y NP-025084 sí están marcadas, pero su suma de detalle no coincide con `suma_importes_legibles`.

   Hay inconsistencia entre las hojas Comprobantes y Detalle (AUD-008). 23 notas no tienen total.
3. **Dependencia entre renglones.** Los 38 REVISAR se concentran en 22 notas (máximo 5 en NP-025131). ICC = 0,246, efecto de diseño = 1,69 y n efectivo ≈ 155. Los renglones de una misma nota no son independientes (AUD-007).
4. **Catálogo.** Hay 169 nombres de producto distintos y 6 grupos con variantes ortográficas, por ejemplo «Cola Sintetica / Cola sintetica / Cola sintética» e «Imprimante / Imprimantes». Esto da sustento cuantitativo a la mejora «catálogo estable», que los informes no usan.
5. **Tipos de dato.** Las hojas Datos de Lean y Seis Sigma guardan `fecha_emision` como texto ('2026-01-26 00:00:00'). En DMAIC es fecha. El contenido coincide celda por celda tras normalizarlo (AUD-015).

## ¿Evalúan los datos el proceso real?

**No.** Permiten evaluar **la calidad documental de un lote digitalizado retrospectivamente**: notas fotografiadas en agosto de 2026, con 62 % de fechas estimadas y 70 de 73 notas anteriores al inicio de actividades declarado.

**No miden el proceso de registro de HIDROCOM en operación.** No hay tiempos, ni registradores identificados, ni orden temporal real, ni sistema de captura observado. Los estados DISPONIBLE, REVISAR y EXCLUIR los asignó quien digitalizó el lote, no el proceso de la empresa. Cualquier DPMO es un indicador de **completitud del conjunto de datos**, no del desempeño empresarial.

## Unidades (no intercambiables)

| Unidad | Cantidad | Uso correcto |
|---|---|---|
| Nota de pedido | 73 (69 con detalle) | Denominador de fechas |
| Renglón | 262 | Denominador de estados y CTQ |
| Campo / oportunidad | 786 (3 por renglón) | Denominador del DPMO sintáctico |
| Defecto | 30 (vacíos) o 35/34 (con diferencias) | Solo bajo un CTQ declarado |
| Unidad defectuosa | 17 (vacíos) o 22 | Yield por unidad: 93,5 % o 91,6 % |
| Observación / incidencia | 151 | No usar como defectos (los informes lo respetan) |
| Registro excluido | 18 | Se conserva, no es defecto |
