# 04 · Auditoría del trabajo Seis Sigma

Objeto: `02_Seis_Sigma/U3_Seis_Sigma_HIDROCOM.pdf` (7 págs.) y `U3_Seis_Sigma_HIDROCOM.xlsx` (6 hojas, 1 328 fórmulas, todas recalculadas sin diferencias).

## Evaluación

| Elemento | Dictamen | Evidencia |
|---|---|---|
| Selección del proceso crítico | ◐ Correcta, pero **cualitativa** | Se eligió por disponibilidad de datos (pág. 2). No hay matriz de selección puntuada (el taller U3-S3 la tenía). La razón es válida, pero no compara impacto. |
| VOC | ✘ Ausente | «Necesidad por validar» sin entrevista. Es la base del CTQ (AUD-013). |
| Árbol CTQ | ◐ Bien construido, propuesto | Tres CTQ (completitud, coherencia, trazabilidad) y defecto operativo «todavía no definido». |
| Definición operacional de defecto | ◐ | Existe una regla sintáctica (celda nula). Falta tratar las excepciones: ¿un precio vacío en una nota PEDIDO es defecto? |
| RACI | ✔ | Una sola A por actividad, verificado en la pág. 3. |
| Responsabilidades | ◐ | Roles definidos; nombres pendientes. En 04 se asignan como propuesta (AUD-006). |
| Unidad de análisis | ✔ | Renglón (`id_detalle`), declarado. |
| Número de oportunidades | ◐ | O = 3 es homogéneo, pero son **campos inspeccionados**, no oportunidades de defecto validadas con el cliente. |
| DPU / DPO / DPMO | ✔ Cálculo correcto | 30/262 = 0,1145; 30/786 = 0,03817; 38 167,94 (recalculado). DPU y yield no se reportan; se recomienda añadirlos (yield por unidad 93,5 %). |
| Yield / RTY | ✘ No reportados | Con una sola etapa, el RTY no aplica. El FPY documental (206/262 = 78,6 %) sería un indicador alternativo útil. |
| Nivel sigma | ✔ Correcto y bien rotulado | 3,2724 con desplazamiento de 1,5 **declarado** («equivalente exploratorio»). |
| Estabilidad | ✔ Correctamente **excluida** | No hay orden temporal fiable. |
| Capacidad | ✔ Correctamente excluida | No hay variable continua con especificación. |

## Preguntas obligatorias del encargo

- **¿Los 30 vacíos son defectos?** Solo bajo la regla sintáctica «campo nulo = defecto». No hay una definición operacional aprobada ni tratamiento de excepciones: notas PEDIDO sin precio, renglones EXCLUIR, unidad de medida. **Dictamen:** se pueden reportar como «defectos de completitud bajo regla analítica», no como defectos del proceso.
- **¿Las 786 oportunidades son válidas?** Son **campos evaluados**, homogéneos y contables. Para llamarlas oportunidades de defecto en sentido Seis Sigma falta que el cliente valide que cada campo es crítico. **Dictamen:** «oportunidades sintácticas».
- **¿3,27 σ representa a la empresa?** **No.** Mide la completitud de un lote digitalizado retrospectivamente, del que 70 de 73 notas son anteriores al inicio de actividades declarado (AUD-001). El informe ya lo advierte. Se mantiene.

## Inconsistencia con el producto final

`04_Producto_Final` usa D = 35 (vacíos + 5 diferencias de importe), DPMO 44 529 y 3,20 σ. Seis Sigma usa D = 30, DPMO 38 168 y 3,27 σ. Ambos son reproducibles, pero ningún documento explica por qué difieren (AUD-002). Además, una de las 5 diferencias (NP-025138-01) es un artefacto de la base «millar»: el criterio ampliado defendible es D = 34, DPMO 43 257 y ≈ 3,21 σ (recalculado).

**Propuesta:** publicar ambos criterios en una tabla de sensibilidad. La tabla debe tener 4 filas: solo vacíos / con diferencias × todo el lote / sin EXCLUIR. Hay que elegir **uno** como línea base oficial y aplicarlo igual en los tres trabajos.

## Alternativas válidas si no se puede calcular un sigma empresarial

1. **Proporción de renglones listos para publicar (FPY documental)**: 206/262 = 78,6 %. Es un indicador por unidad, sin supuestos sobre oportunidades.
2. **p de REVISAR** con intervalo de confianza que considere la agrupación por nota (efecto de diseño 1,69).
3. Un DPMO formal **solo** después de aprobar el CTQ con el dueño del proceso y medir un lote nuevo con orden temporal. En ese momento sí aplicaría una gráfica p por lote.
