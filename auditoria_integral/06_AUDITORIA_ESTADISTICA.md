# 06 · Auditoría estadística

## Cálculos verificados independientemente

Todos se reproducen con `14_EVIDENCIAS_AUDITORIA/recalculo_independiente.py`:

| Cálculo | Publicado | Recalculado | Dictamen |
|---|---|---|---|
| p REVISAR | 14,50 % | 14,50 %; IC 95 % Wilson **nominal** 10,75–19,28 %, que supone renglones independientes; con agrupamiento por nota (deff 1,69) es más ancho. El IC no resuelve la representatividad del lote (AUD-001). | ✔ (falta comunicar el intervalo y su supuesto) |
| DPMO / sigma (D = 30) | 38 167,94 / 3,2724 | idénticos | ✔ |
| DPMO / sigma (D = 35) | 44 529 / 3,20 | 44 529,26 / 3,2004 | ✔ (criterio distinto, AUD-002) |
| DPMO / sigma (D = 34, sin el artefacto millar) | — | 43 257,0 / 3,2141 | Propuesta |
| Sin EXCLUIR (D = 27) | 36 885,25 / 3,288 | idénticos | ✔ |
| Pareto acumulado | 34,21–100 % | idéntico | ✔ |
| 45/73 fechas | 61,64 % | idéntico | ✔ |
| Beneficio (escenario base de 04) | S/ 255 | S/ 255 con sus supuestos; **−S/ 91,80** con el volumen implícito en el rango de fechas | ◐ (AUD-005) |

El desplazamiento de 1,5 σ está declarado en Seis Sigma, en DMAIC 03 («si el curso exige») y en 04 («bajo la regla propuesta»). ✔

## Dependencia entre renglones de una misma nota

- 262 renglones en 69 notas: media de 3,8 por nota, máximo 14.
- ICC del indicador REVISAR dentro de la nota = **0,246**. Efecto de diseño ≈ **1,69**. Tamaño efectivo ≈ **155**.
- **Consecuencias:**
  - Los intervalos y pruebas a nivel de renglón subestiman la incertidumbre.
  - Un Fisher o chi-cuadrado sobre renglones viola el supuesto de independencia.
  - Cualquier comparación futura antes/después debe hacerse **por nota** o con métodos para conglomerados.

## Pertinencia de herramientas

| Herramienta | Aplicable actualmente | Justificación | Datos adicionales necesarios | Beneficio |
|---|---|---|---|---|
| Estadística descriptiva | Sí | Conteos y proporciones sobre la población del lote | — | Alto |
| Distribuciones de frecuencia | Sí | Estados, condiciones, productos, renglones por nota | — | Medio |
| Intervalos de confianza | Sí, con cautela | Wilson para p; ajustar por conglomerado (deff 1,69). Si el lote se trata como población, el IC solo tiene sentido para inferir a lotes futuros. | — | Medio |
| Análisis de datos faltantes | **Sí (falta hacerlo)** | 30 vacíos: ¿aleatorios o concentrados en PEDIDO, notas tachadas o un archivo de origen? Tabla vacío × estado y vacío × archivo_origen. | — | Alto |
| Análisis de sensibilidad | **Sí (falta)** | D = 30/34/35, con o sin EXCLUIR, eficacia de la simulación, supuestos del beneficio | — | Alto |
| Estratificación | Sí | Por estado de nota, tipo de fecha, archivo de origen (lote de imágenes) | — | Alto |
| Pareto | Sí (hecho) | Excluyente y reproducible | — | Alto |
| Histogramas | Parcial | Importe por renglón y renglones por nota. Son descriptivos, no del proceso. | — | Bajo |
| Diagramas de caja | Parcial | Importe por estado de uso | — | Bajo |
| Pruebas de normalidad | No | No hay variable continua del proceso que modelar | Tiempos de registro | — |
| Pruebas de hipótesis | No para causas | Las asociaciones PEDIDO/numéricas → REVISAR son definicionales. Probarlas sería circular. | Lote nuevo con estado asignado por un criterio independiente | — |
| Chi-cuadrado | No recomendable | Celdas esperadas pequeñas (1,9) y dependencia intra-nota | — | — |
| Prueba exacta de Fisher | Solo descriptiva | Fecha estimada: p = 0,47, sin poder; no permite «descartar» | — | Bajo |
| Gráficos de dispersión / correlación / regresión | No | Sin variables continuas del proceso; el importe no es un CTQ | Tiempos, volumen | — |
| Gráfico p | **No ahora** | No hay orden temporal real (fechas estimadas o discordantes) ni subgrupos definidos. Ordenar por correlativo sería inventar el orden. | Lotes de piloto con fecha real de registro | Alto a futuro |
| Gráfico np | No | Igual; además, subgrupos de tamaño variable | Ídem | — |
| Gráficos c / u | No ahora | Defectos por nota sin orden temporal válido | Ídem | Medio a futuro (u por lote) |
| I-MR / X̄-R | No | No hay variable continua medida | Tiempo por renglón | Alto a futuro |
| Cp / Cpk / Pp / Ppk | **No** | Variable categórica, sin límites de especificación ni estabilidad demostrada | Tiempo de ciclo con especificación | — |
| MSA por atributos (kappa) | **Sí, recomendable** | La clasificación REVISAR depende de juicio humano | Segundo revisor y originales | Alto |

## Riesgos de sobreinterpretación detectados

1. **«Causa respaldada» por asociaciones definicionales** (04, A2 y lámina 7). Ver AUD-003.
2. **«Descartada» con p = 0,47 y poco poder.** Ya se corrigió a «no respaldada (descriptivo)» en `4d1ec0d`. Mantener.
3. **Simulación presentada con un solo valor.** Debe presentarse como rango (AUD-004).
4. **Sigma como desempeño de la empresa.** Los tres trabajos ya lo niegan. Mantener.
