# Propuestas de mejora para HIDROCOM KALLPA

Propuestas preliminares para la Unidad 3. Revisiones examinadas: `main` en `e3b5a60`, la rama de Claude en `4d1ec0d` y el árbol de la rama de Codex en `b9d921b`. La base documental permite validar indicadores y priorizar acciones. La eficacia de los controles requiere un piloto. Las iniciativas se mantienen dentro de sus respectivos trabajos de Lean, Seis Sigma y DMAIC.

## Con los archivos disponibles

### PM-01 · Separar y reproducir los indicadores de Seis Sigma

- **Evidencia y prioridad.** Alta. `02_Seis_Sigma/U3_Seis_Sigma_HIDROCOM.xlsx`, hoja `CTQ`, B8:B11, distingue completitud, coherencia y defecto operativo. El Excel oficial de DMAIC, `M2_LineaBase_Sigma!B8:B12`, usa una regla documental que incorpora ambos tipos de defecto. Intercambiar las cifras cambia la definición del indicador.
- **Cambio y archivos.** En el trabajo de Seis Sigma, presentar 30 campos vacíos entre 786 oportunidades (38 167,94 DPMO, 3,27 σ). En DMAIC, mantener el CTQ propuesto con 30 vacíos y 5 discrepancias adicionales entre las mismas 786 oportunidades (44 529,26 DPMO, 3,20 σ). Indicar el desplazamiento de 1,5 σ. Registrar por separado los 38 REVISAR entre 262 renglones (14,50 %). Alinear el Word, M2 y la diapositiva 5 con esa distinción.
- **Dependencia, aceptación y prueba.** Usar `03_DMAIC/U3_DMAIC_HIDROCOM.xlsx`, hoja `Datos`, como base de la reproducción documental. Recontar los vacíos por campo (5, 16 y 9), las cinco discrepancias de importes no vacíos y las tres oportunidades por renglón. Las fórmulas y las cifras visibles deben coincidir.
- **Impacto y esfuerzo.** Impacto alto sobre la interpretación. Esfuerzo bajo para alinear los textos y medio para mantener una comprobación automática reproducible.

### PM-02 · Conciliar fuentes y explicitar la unidad de las fechas

- **Evidencia y prioridad.** Alta. `03_DMAIC/U3_DMAIC_HIDROCOM.xlsx`, `Verificar!B8:B9`, documenta una categoría distinta entre Excel y CSV y una diferencia con el hash declarado del Excel. `Medir!A13:B15` usa notas. La diapositiva 5 de la presentación oficial usa renglones.
- **Cambio y archivos.** Crear un manifiesto de versiones con SHA-256 por archivo y una comparación tabular por identificador entre las versiones disponibles. Tratar las fechas en dos niveles: notas y renglones. Conservar originales y documentar las transformaciones con su revisión y conteo.
- **Dependencia, aceptación y prueba.** Registrar lo ya comprobable con los libros actuales. Ejecutar la conciliación entre archivos originales cuando estén disponibles por un canal autorizado. El control de `C1_Plan_Control!A8` debe verificar cada archivo contra su hash esperado y luego conciliar llaves, categorías y agregados. Los hashes de un XLSX y de un Data Mart en otro formato no tienen que ser iguales. Los porcentajes de fechas deben mostrar el numerador, denominador y tratamiento de discordancias.
- **Impacto y esfuerzo.** Impacto alto en trazabilidad. Esfuerzo medio para automatizar controles, con dependencia adicional para resolver discrepancias de origen.

### PM-03 · Reproducir Pareto, asociación e impacto simulado en DMAIC

- **Evidencia y prioridad.** Alta. `A1_Pareto!B5:B13` distribuye los 38 REVISAR en categorías exclusivas. `A2_Ishikawa_Verificacion!A22` describe otra agrupación por condiciones que se solapan. `I2_Plan_Accion!A13` propone un escenario retrospectivo.
- **Cambio y archivos.** Conservar la prioridad de clasificación de `Verificar!B14:B18`. Agregar una tabla que muestre 13 PEDIDO, 21 REVISAR con incidencia numérica y 9 que cumplen ambas condiciones, de modo que la unión sea 25. Vincular el escenario de 13 REVISAR restantes a reglas transparentes y mostrar el caso parcial cuando los documentos permitan resolver menos filas. Alinear I2, A2, Word y diapositivas 7 y 9.
- **Dependencia, aceptación y prueba.** Fijar las reglas sobre una copia de trabajo y comprobar que la suma exclusiva del Pareto da 38, la unión da 25 y 13/262 da 4,96 % únicamente bajo el escenario descrito. Conservar las hipótesis sobre el original y verificar la demostración operativa en el piloto.
- **Impacto y esfuerzo.** Impacto alto en la defensa del resultado. Esfuerzo medio para hacer trazable la reclasificación y sus excepciones.

### PM-04 · Hacer comprobables el Poka-Yoke y el plan de control

- **Evidencia y prioridad.** Alta. `01_Lean/U3_Lean_HIDROCOM.xlsx`, `PokaYoke!A3` y A17, delimita las alertas y la base de precio. `03_DMAIC/U3_DMAIC_HIDROCOM.xlsx`, `Validar!A17:A20`, define controles y tolerancia pendiente. El Excel oficial, `C1_Plan_Control!A5:B8`, contiene metas propuestas.
- **Cambio y archivos.** En Lean, incorporar un juego de pruebas para campos faltantes, importe incoherente, base de precio inválida y registro válido. En DMAIC, separar prevención de captura, revisión de la evidencia y liberación. Precisar para cada KPI la fórmula, fuente, frecuencia, rol propuesto, umbral y reacción. Mantener la aprobación del responsable diferenciada del estado del prototipo.
- **Dependencia, aceptación y prueba.** Las pruebas estructurales pueden ejecutarse con casos sintéticos identificados como tales. Probar la tolerancia monetaria cuando el equipo defina excepciones y criterio de aceptación. Verificar que un registro elegible pase y que una omisión o inconsistencia se detecte de forma reproducible.
- **Impacto y esfuerzo.** Reduce el riesgo de publicar un renglón incompleto. Esfuerzo medio. La activación en la empresa depende del dueño del proceso.

### PM-05 · Integrar el costo-beneficio como modelo de escenarios

- **Evidencia y prioridad.** Alta para el producto final. `C2_Beneficios_Lecciones!B5:B8` y A11 documentan el escenario de S/ 255. `03_DMAIC/U3_DMAIC_HIDROCOM.xlsx`, `Beneficios!A6:A14`, contempla el volumen, los tiempos, el costo recurrente y el factor realizable.
- **Cambio y archivos.** En el Excel de costo-beneficio, separar los supuestos editables de los cálculos. Mostrar horas liberadas y beneficio neto estimado. Someter a sensibilidad los renglones resueltos y los minutos por revisión con valores identificados como escenarios. Exponer el costo inicial, el recurrente y la proporción realizable como entradas diferenciadas. Mantener S/ 255 como el escenario base de C2, con sus supuestos.
- **Dependencia, aceptación y prueba.** Reproducir `(47,50 − 16,25) × 12 − 120 = 255` con los supuestos del Excel oficial. Comprobar que si el número de renglones resueltos baja a cero desaparece el beneficio bruto por retrabajo y que un costo recurrente mayor reduce el neto. El Word y la diapositiva 11 deben usar la misma etiqueta y alcance.
- **Impacto y esfuerzo.** Impacto alto para explicar de qué depende el resultado. Esfuerzo medio para desarrollar y probar el modelo.

## Con evidencia empresarial o piloto

### PM-06 · Medir en Lean el flujo actual y contrastar el flujo futuro

- **Evidencia y prioridad.** Alta si se pretende medir productividad. `VSM!A6:B11` del libro Lean identifica seis etapas. `VSM!A16:B20` deja pendientes tiempo de proceso, espera, lead time, valor agregado y eficiencia. `Desperdicios!A6:B13` distingue evidencias de hipótesis, y `5S!A2:B3` delimita el ejercicio al espacio académico.
- **Cambio y archivos.** Mantener el VSM documental como esquema. Preparar una ficha de observación por nota y etapa con hora de entrada y salida, espera, retrabajo, rol y evidencia. Tras la medición, construir el VSM actual y usar el futuro como diseño a contrastar. Mantener la 5S digital académica separada de cualquier futura intervención empresarial.
- **Dependencia, aceptación y prueba.** El dueño del proceso debe autorizar la observación y acordar el flujo, las clasificaciones y la unidad de tiempo. Una medición completa debe permitir reconstruir los tiempos desde las fichas sin convertir tiempos simulados en observados.
- **Impacto y esfuerzo.** Alto para evaluar esperas y retrabajo. El mayor esfuerzo está en observar un flujo representativo.

### PM-07 · Aprobar el CTQ y evaluar los controles con un lote nuevo

- **Evidencia y prioridad.** Alta para validar la mejora. `CTQ!A3` del libro Seis Sigma registra la VOC pendiente. `I2_Plan_Accion!A8` prevé un piloto real y `DECISIONES.md` mantiene abiertos el dueño del proceso, la meta, los plazos y los supuestos.
- **Cambio y archivos.** En Seis Sigma, validar con el responsable el CTQ, los campos aplicables, la base de precio y las excepciones. En DMAIC, definir antes del piloto cómo se cuenta REVISAR y cuándo se considera cerrada una observación. Aplicar al lote nuevo los controles ya acordados. Registrar el volumen, los defectos, el tiempo y los costos de revisión con las mismas unidades antes y después.
- **Dependencia, aceptación y prueba.** Requiere originales autorizados y trazables, aprobación del criterio y una captura prospectiva. Contrastar las causas documentales con el flujo observado. Informar el resultado del piloto junto con su alcance y comparar con el escenario retrospectivo sin sustituir uno por el otro.
- **Impacto y esfuerzo.** Alto para la adopción operativa. El esfuerzo depende de acceso y coordinación con la empresa.

## Orden de ejecución

1. Reproducir indicadores, aclarar sus bases y revisar trazabilidad en PM-01 y PM-02.
2. Documentar el Pareto y la simulación reproducible en PM-03. Probar el Poka-Yoke y precisar los controles en PM-04.
3. Modelar el costo-beneficio y sincronizar el Word, el Excel y la presentación en PM-05.
4. Ejecutar la observación y el piloto de PM-06 y PM-07 cuando se disponga de autorización y evidencia empresarial.
5. Conciliar estas propuestas con los hallazgos de la auditoría integral antes de modificar entregables compartidos.

## Decisiones del equipo y de la empresa

- ¿Se puede cotejar una copia autorizada de las notas originales y confirmar la procedencia y las fechas del lote?
- ¿Quién aprueba el CTQ, sus excepciones, la regla PEDIDO, el responsable del proceso y la meta de control?
- ¿Qué lote nuevo puede observarse y qué datos de tiempo, costo y volumen puede confirmar el dueño del proceso?

## Contraste con la auditoría integral publicada

Actualización posterior al commit `99df911` de Claude. Estas precisiones ajustan las propuestas preliminares. El cotejo se realizó con el informe de auditoría y el libro de base del repositorio.

- **PM-02 y PM-07.** Se recontaron 73 fechas de emisión en la hoja `Comprobantes`; 70 son anteriores al 9 de marzo de 2026, fecha de inicio de actividades indicada en la auditoría. Hasta confirmar la procedencia y la población, el objeto de análisis es la calidad documental de ese lote. La auditoría tampoco reprodujo las discrepancias de hash y categoría con la copia que examinó. Registrar ambas como discrepancias entre versiones por conciliar y retirarlas del argumento principal mientras no se reproduzcan.
- **PM-01.** El criterio D = 34, que excluye una diferencia atribuida a la etiqueta de base «millar», da 43 257,00 DPMO y 3,2141 σ. Este recálculo verifica la conversión para 34 defectos. La clasificación de la fila requiere aprobación. Mantener la distinción entre el conteo de vacíos y los conteos que incluyen discrepancias.
- **PM-03.** Los estados y criterios de clasificación intervienen en la construcción de REVISAR. La asociación identificada sirve para priorizar controles, con verificación operativa pendiente. Para proporciones supuestas de resolución del 100 %, 75 %, 50 % y 25 % de los 25 casos, se reproducen 4,96 %, 7,35 %, 9,73 % y 12,12 % de REVISAR. Son tasas esperadas en la simulación, con 262 renglones como denominador.
- **PM-05.** Incluir el escenario de S/ 255 con un lote mensual y un escenario de volumen bajo. Con el supuesto de distribuir un lote en aproximadamente 13,3 meses, el resultado se aproxima a −S/ 91,80 según el redondeo. Ese volumen no mide la cadencia real. Mostrar el punto de equilibrio en unidades de revisión por mes y solicitar al responsable una cadencia validada.

[Auditoría y plan de mejora en GitHub](https://github.com/Nunclear/hidrocom-mejora-procesos-u3/tree/99df911aa3b5f617e46ed65fe699c769d7266a3f/auditoria_integral)

## Correspondencia con las tareas de Claude

| Propuesta | Plan publicado de Claude | Punto que se debe conciliar |
|---|---|---|
| PM-01 | T07, T14, T15 y T23 | Definiciones comparables y criterio CTQ oficial |
| PM-02 | T01 a T06, T22 y T26 | Procedencia, población y versión de fuente, con denominadores explícitos |
| PM-03 | T08, T09 y T24 | Prioridad excluyente, comparación documental y supuestos de simulación |
| PM-04 | T23, T25 y T27 | Pruebas de captura, tolerancia y liberación |
| PM-05 | T10 y T19 | Sensibilidad al volumen y coherencia del Word con C2 |
| PM-06 | T13, T18 y T21 | VSM documental, diseño futuro y medición en campo |
| PM-07 | T11, T12, T17 y T27 | Aprobación del CTQ, responsables y piloto real |

El plan maestro condiciona T07 a una decisión del equipo. El prompt de implementación propone usar D = 34 como criterio oficial en ausencia de esa decisión. Conviene resolver la diferencia antes de propagar una cifra única. D = 34 puede presentarse como escenario analítico mientras el equipo documenta la regla aplicable a la base «millar» y aprueba el CTQ.

La comparación también debe conservar el alcance de las versiones: el libro completo de datos para pruebas locales y las hojas, indicadores o metadatos autorizados para publicación. Vincular el informe y el costo-beneficio a la regla acordada y al escenario de volumen declarado.

[Plan maestro de Claude](https://github.com/Nunclear/hidrocom-mejora-procesos-u3/blob/99df911aa3b5f617e46ed65fe699c769d7266a3f/auditoria_integral/10_PLAN_MAESTRO_MEJORA.md) · [Prompt de implementación](https://github.com/Nunclear/hidrocom-mejora-procesos-u3/blob/99df911aa3b5f617e46ed65fe699c769d7266a3f/auditoria_integral/13_PROMPT_IMPLEMENTACION.md)

## Revisión de las propuestas publicadas por Claude

- La propuesta PM-08 de Claude compara el registro original con el revisado y con el historial de correcciones. Aporta evidencia temporal independiente de la etiqueta REVISAR. El contraste sigue propuesto y requiere autorización de acceso. Puede describir omisiones y correcciones, con un alcance distinto del piloto y sin atribuir por sí solo una causa operativa.
- En el VSM documental de la propuesta PM-09 de Claude, rotular 206/262 = 78,63 % como proporción de renglones DISPONIBLE al corte. Un rendimiento de primera pasada requiere registrar el resultado antes de cualquier retrabajo. El estado DISPONIBLE al corte no identifica esa primera pasada.
- El intervalo de Wilson nominal para 38/262 REVISAR se reproduce en 10,75–19,28 %. Describir la hipótesis de independencia de ese cálculo. Para inferencia, considerar el agrupamiento de renglones dentro de cada nota y el diseño de muestreo. La incertidumbre estadística no resuelve la representatividad del lote.

[Propuestas de Claude en la revisión fc1216f](https://github.com/Nunclear/hidrocom-mejora-procesos-u3/blob/fc1216f9fd560ba367eb55dd56db741ca831de6c/auditoria_integral/16_PROPUESTAS_MEJORA_CLAUDE.md)

## Fuentes consultadas

- [Archivos de Lean en la revisión de base](https://github.com/Nunclear/hidrocom-mejora-procesos-u3/tree/e3b5a6004c89c504b60fe3deb77679f55b4e5a6d/01_Lean)
- [Archivos de Seis Sigma en la revisión de base](https://github.com/Nunclear/hidrocom-mejora-procesos-u3/tree/e3b5a6004c89c504b60fe3deb77679f55b4e5a6d/02_Seis_Sigma)
- [Archivos de DMAIC en la revisión de base](https://github.com/Nunclear/hidrocom-mejora-procesos-u3/tree/e3b5a6004c89c504b60fe3deb77679f55b4e5a6d/03_DMAIC)
- [Excel oficial, presentación y decisiones](https://github.com/Nunclear/hidrocom-mejora-procesos-u3/tree/4d1ec0dd0765202bce1fbf5e4195a52af6a2c8cb/04_Producto_Final)
