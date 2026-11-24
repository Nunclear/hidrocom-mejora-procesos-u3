# Contrato común de datos e indicadores

Versión 1.0 · 24/11/2026 · fijado por la instrucción expresa del usuario en PROMPT_MEJORA_COLABORATIVA.md. Los roles de agentes no son cargos ni certificaciones de integrantes de la empresa.

## Fuentes, alcance y unidad

Se estudia un lote documental de **73 notas y 262 renglones**. La procedencia empresarial y la cronología siguen pendientes. No se incorpora la población ampliada de 510. Las fechas estimadas/discordantes no constituyen una cadencia operativa observada.

El Excel original tiene SHA-256 `ac6ab323264518a0f2eb7dfe61a43960b8992fdc5453e25cda9073fac6318682`. No se modifica. La copia congelada de los valores ya publicados está en `../datos_control/corte_documental_73_262.json` (SHA-256 `e575d3a81ffc1ff894b8d6b0cd5b47bf7c01d28db6978458500c206e0844f56c`). Las hojas fuente de los Excel actualizados deben seguir siendo trazables a ella.

| Unidad | Identificación | Uso |
|---|---|---|
| Nota | id_comprobante | 73 documentos; incluye notas sin detalle |
| Renglón | id_detalle | 262, agrupados en notas; no presumir independencia |
| Campo inspeccionado | cantidad, precio_unitario, subtotal_producto | 3 por renglón, 786 en total |
| Vacío sintáctico | celda nula en esos tres campos | no implica incumplimiento operativo aprobado |
| Estado documental | uso_importe | no equivale a defecto ni a primera pasada |

## Indicadores de estado

| Indicador | Numerador | Denominador | Resultado |
|---|---:|---:|---:|
| DISPONIBLE | 206 | 262 | 78,63 % |
| REVISAR | 38 | 262 | 14,50 % |
| EXCLUIR | 18 | 262 | 6,87 % |

DISPONIBLE **no es FPY**. FPY y RTY operativos quedan pendientes; REVISAR no prueba una unidad defectuosa. No usar las 151 entradas heterogéneas de incidencias como D.

## Indicador principal: completitud sintáctica exploratoria

Cantidad: 5 nulos; precio: 16; importe: 9. D = 30 campos nulos. U = 262 renglones. O = 3 campos por renglón. DPO equivalente = 30/786; DPU sintáctico = 30/262. DPMO equivalente = 30/786 × 10^6 = 38 167,94. Sigma equivalente = Φ⁻¹(1−30/786)+1,5 = 3,2724. La convención +1,5 es explícita; no demuestra estabilidad o capacidad real ni CTQ aprobado.

La proporción de renglones completos y el complemento de la fracción de campos vacíos son medidas distintas; ninguna es FPY operativo. Los campos llenos pueden contener valores incorrectos. Un vacío puede ser una excepción válida; esto requiere acordar obligatoriedad.

## Escenarios separados

| Escenario | Regla | D | Denominador académico | DPMO equiv. | Sigma equiv. |
|---|---|---:|---:|---:|---:|
| S30 (principal) | solo campos nulos | 30 | 786 campos | 38 167,94 | 3,2724 |
| S34 (sensibilidad) | regla combinada con excepción propuesta de base de precio | 34 | 786 bajo regla publicada, por validar | 43 257,00 | 3,2141 |
| S35 (sensibilidad) | nulos + 5 diferencias consignadas | 35 | 786 bajo regla publicada, por validar | 44 529,26 | 3,2004 |

S34/S35 mezclan comprobaciones de completitud y coherencia y no son el mismo indicador de S30. Su denominador es una convención del ejercicio publicado, no oportunidades empresariales validadas. No convertir esas cifras en un único sigma oficial ni imputar correcciones. Conservar la incidencia NP-025138-01 y documentar cantidad, precio, importe, unidad_del_precio, importe_calculado y diferencia_importe sin resolver la base por simple coincidencia aritmética.

## Pareto y análisis causal

Para los 38 REVISAR usar la primera regla que corresponda: (1) PEDIDO en nota o renglón; (2) alguno de los tres campos nulo; (3) diferencia consignada no cero; (4) observación o DUDOSA; (5) motivo no explicitado en el detalle. Categorías excluyentes: 13, 7, 5, 7 y 6. Para el Pareto visual ordenar por frecuencia y mostrar acumulado, conservando esta prioridad de asignación.

La unión de PEDIDO y condiciones numéricas puede describirse; no demuestra causa raíz porque interviene en la asignación del estado. Separar condición observada, asociación, causa candidata y causa verificada independientemente. PM-08 permite comprobar transformaciones documentales, no prueba por sí sola causalidad operativa.

## Simulación y economía

Si el conjunto hipotéticamente resoluble es 25, REVISAR esperado = 38−25×e; tasa = (38−25×e)/262 para e = 100/75/50/25 %. Los valores fraccionarios son expectativas del modelo, no renglones realmente resueltos. Rango aproximado 4,96–12,12 %. El 100 % es un máximo condicionado; los casos deben cotejarse antes de cerrar.

Beneficio anual neto del modelo = volumen REVISAR/mes × fracción resuelta × minutos ahorrados/60 × costo/hora × factor realizable × 12 − costo inicial − costo recurrente anual. Todos los parámetros empresariales permanecen sin medición; los ejemplos se identifican como escenarios. Conservar resultados negativos, distinguir horas liberadas de flujo de caja y probar sensibilidad y equilibrio. El rango de fechas no mide frecuencia mensual real.

## Estadística, tiempos y aprobación

38/262 es descriptivo del lote completo. Wilson nominal supone independencia; ICC/efecto de diseño dependen de un modelo de agrupamiento, no acreditan muestreo ni representatividad. No inferir desempeño poblacional sin población objetivo y diseño defendibles. No usar fechas inciertas para cartas de control ni Cp/Cpk sin variables y especificaciones válidas.

VSM actual = flujo documental derivado; futuro = diseño. TC, LT, espera, retrabajo y VA quedan sin medir. 5S digital = taller académico. Roles nominales, metas, plazos, puntajes, tolerancias, VOC y MSA permanecen pendientes. Una aprobación metodológica del usuario no es firma empresarial ni certificación Belt.

## Conciliación de versiones

AUD-012 es **específico de versión**. El ZIP v3 de main conserva una huella declarada distinta y «herramietas»; la copia reportada por Claude presenta otros CSV. Ver EVIDENCIA_COPIA_MAIN.json y TRAZABILIDAD_FUENTES.csv. Cada archivo se compara con su propia huella esperada; no se exige igualdad entre formatos diferentes. No atribuir autor o fecha de transformación sin evidencia.

El esquema legible por máquina está en contrato_datos.json. Los resultados independientes y los controles están en ../validacion/; cada revisión debe citar el commit y las pruebas efectivamente ejecutadas.
