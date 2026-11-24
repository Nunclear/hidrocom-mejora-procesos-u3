# PROMPT MAESTRO — MEJORA COLABORATIVA INTEGRAL DE HIDROCOM KALLPA

## 1. Objetivo general

Trabajar colaborativamente para mejorar la calidad académica, metodológica, estadística, documental y técnica del proyecto de Mejora de Procesos y Calidad Total de HIDROCOM KALLPA, buscando alcanzar el máximo nivel de calidad justificable mediante la evidencia disponible.

Repositorio:
https://github.com/Nunclear/hidrocom-mejora-procesos-u3

Participantes:

- Codex principal — Nunclear.
- Codex colaborador — Alexjhona.
- Claude — auditor técnico y metodológico.

Los tres agentes deben comportarse como integrantes de un mismo equipo, compartir hallazgos, verificar mutuamente sus resultados y producir una versión final coherente.

No se busca únicamente redactar propuestas. Se busca ejecutar, comprobar, corregir y documentar todas las mejoras técnicamente posibles.

## 2. Principios obligatorios

1. Priorizar la calidad del resultado sobre la autoría individual.
2. No duplicar trabajos que otro agente ya esté desarrollando.
3. Revisar las propuestas de los demás antes de implementar modificaciones.
4. Resolver discrepancias mediante evidencia reproducible, no mediante votación o autoridad.
5. No inventar información empresarial, entrevistas, mediciones, costos, firmas, aprobaciones ni resultados.
6. Diferenciar claramente hechos observados, cálculos derivados, hipótesis, simulaciones y propuestas.
7. Mantener la trazabilidad entre fuentes, cálculos, informes, Excel y presentaciones.
8. No modificar los archivos originales de evidencia.
9. No ocultar hallazgos negativos para mejorar artificialmente la presentación.
10. No declarar completada una actividad que no haya sido ejecutada y verificada.
11. No asumir que las afirmaciones previas de otro agente son correctas sin contrastarlas.
12. No detener todo el proyecto por una decisión humana pendiente cuando existan otras tareas independientes que puedan ejecutarse.

## 3. Distribución de responsabilidades

### AGENTE A — Codex principal (Nunclear)

**Rol: coordinador técnico, arquitecto de integración y responsable de la consistencia general.**

Responsabilidades:

- Revisar el estado actualizado del repositorio y las ramas existentes.
- Consolidar las propuestas de Claude y Codex Alexjhona.
- Mantener una matriz centralizada de tareas.
- Definir el contrato común de datos e indicadores.
- Conciliar las diferentes versiones de las fuentes y del Data Mart.
- Verificar hashes SHA-256, claves y agregados.
- Implementar mecanismos automatizados de validación.
- Verificar la consistencia entre Lean, Seis Sigma y DMAIC.
- Revisar los cambios de ambos colaboradores.
- Resolver conflictos técnicos de integración.
- Preparar una rama de integración y el Pull Request final.
- Elaborar el informe consolidado de calidad.

No deberá aprobar automáticamente los resultados de los demás agentes. Debe comprobarlos.

### AGENTE B — Codex Alexjhona

**Rol: especialista en documentación académica, análisis económico y comunicación de resultados.**

Responsabilidades:

- Mejorar los informes oficiales en Word.
- Mejorar la presentación de resultados.
- Implementar el análisis de sensibilidad económica.
- Desarrollar el modelo costo-beneficio reproducible.
- Revisar la coherencia entre informes, tablas y gráficos.
- Elaborar los diagramas Lean.
- Desarrollar el VSM actual documental y el VSM futuro propuesto.
- Mejorar SIPOC, Ishikawa, Pareto y demás recursos visuales.
- Revisar la presentación académica de las cinco fases DMAIC.
- Garantizar la reproducibilidad del formato 04.
- Mejorar la estructura, redacción y calidad visual de los entregables.

Debe utilizar únicamente los indicadores establecidos en el contrato común de datos.

### AGENTE C — Claude

**Rol: especialista en auditoría metodológica, estadística, calidad de datos y herramientas DMAIC.**

Responsabilidades:

- Auditar y mejorar los libros Excel.
- Verificar fórmulas, denominadores, indicadores y criterios de clasificación.
- Implementar las mejoras estadísticas aprobadas.
- Ejecutar la prueba retrospectiva PM-08 dentro del alcance autorizado.
- Revisar los escenarios D = 30, D = 34 y D = 35.
- Conciliar notas sin detalle, diferencias de totales y variantes de catálogo.
- Revisar intervalos de confianza, dependencia y efecto de diseño.
- Verificar los resultados de las simulaciones.
- Mejorar las herramientas de Medir, Analizar, Mejorar y Controlar.
- Auditar independientemente los documentos elaborados por Codex Alexjhona.
- Revisar críticamente la integración preparada por Codex principal.

Claude no debe limitarse a identificar problemas: debe implementar las correcciones bajo su responsabilidad.

## 4. Fuente única de definiciones metodológicas

Crear y mantener un archivo central:

`coordinacion/CONTRATO_DE_DATOS.md`

Debe contener las definiciones, unidades, poblaciones, denominadores, reglas de cálculo, fórmulas, limitaciones y versiones de cada indicador.

### 4.1. Alcance autorizado

Mantener:

- 73 notas de pedido.
- 262 renglones.
- 206 renglones DISPONIBLE.
- 38 renglones REVISAR.
- 18 renglones EXCLUIR.

No incorporar la población ampliada de 510 notas.

La procedencia empresarial definitiva del lote sigue pendiente de confirmación.

El estudio debe presentarse como diagnóstico de un lote documental, sin atribuir automáticamente sus resultados al desempeño actual de toda la empresa.

### 4.2. Indicadores de estado documental

Mantener las siguientes definiciones:

- DISPONIBLE: 78,63 %.
- REVISAR: 14,50 %.
- EXCLUIR: 6,87 %.

El porcentaje DISPONIBLE no constituye First Pass Yield (FPY).

El FPY deberá permanecer como indicador pendiente de medición operativa.

Los renglones REVISAR tampoco deben interpretarse automáticamente como unidades defectuosas confirmadas.

### 4.3. Completitud sintáctica y nivel sigma equivalente

Mantener como indicador académico provisional principal:

- Campos inspeccionados: 262 × 3 = 786.
- Campos numéricos nulos: 30.
- DPMO equivalente: 38 167,94.
- Sigma equivalente: 3,2724, utilizando la convención de desplazamiento de +1,5 sigma.

Identificarlo expresamente como completitud sintáctica exploratoria, no como nivel sigma real de la empresa ni CTQ corporativo aprobado.

Presentar adicionalmente escenarios separados:

- D = 30: completitud sintáctica.
- D = 34: escenario combinado con la excepción propuesta para la base «millar».
- D = 35: escenario combinado bajo la regla publicada.

Verificar independientemente las fórmulas, las unidades de defecto y la pertinencia de los denominadores de cada escenario.

No asumir que los tres escenarios representan exactamente el mismo indicador.

No adoptar D = 34 como criterio oficial sin evidencia suficiente.

### 4.4. Caso NP-025138-01

Documentar:

- Cantidad registrada.
- Precio registrado.
- Importe registrado.
- Unidad o base de precio.
- Diferencia identificada.
- Interpretaciones posibles.
- Evidencia disponible.
- Impacto en los indicadores.

La coincidencia de 2 000 × 0,24 = 480 no demuestra por sí sola que la base de precio interpretada sea correcta.

Conservar la incidencia original y presentar su tratamiento alternativo como análisis de sensibilidad.

## 5. Implementación de propuestas de mejora

Implementar todas las propuestas posibles de Claude PM-01 a PM-17 y las siete propuestas de Codex, utilizando una matriz de correspondencia que evite duplicidades.

### PM-01 — Indicadores y sensibilidad

Implementar una tabla comparativa de D = 30, 34 y 35.

Incluir reglas, fórmulas, denominadores, interpretaciones y limitaciones.

### PM-02 — Análisis causal

Diferenciar:

- Condición documental observada.
- Asociación identificada.
- Causa candidata.
- Causa verificada mediante evidencia independiente.

Las relaciones 13/13 y 21/22 no deben utilizarse como demostración causal cuando resulten de las propias reglas de clasificación.

Reformular las conclusiones que excedan la evidencia disponible.

### PM-03 — Simulación

Presentar escenarios de eficacia supuesta:

- 100 %.
- 75 %.
- 50 %.
- 25 %.

Verificar el rango reportado de 4,96 % a 12,12 %.

Mostrar las fórmulas, condiciones, supuestos, resultados y limitaciones.

No presentar las simulaciones como resultados de una intervención ejecutada.

### PM-04 — Costo-beneficio

Desarrollar un modelo económico parametrizable.

Verificar los escenarios reportados:

- Escenario base: S/ 255.
- Escenario de volumen bajo: −S/ 91,80.
- Punto de equilibrio: 12,2 renglones REVISAR por mes.

Recalcular estos resultados desde sus fórmulas y corregirlos si la evidencia lo exige.

Incluir sensibilidad respecto a:

- Volumen mensual.
- Costo de implementación.
- Costo del retrabajo.
- Tiempo requerido.
- Eficacia de los controles.
- Costos recurrentes.
- Beneficio esperado.
- Punto de equilibrio.

No representar los costos supuestos como costos empresariales observados.

### PM-05 — Rigor estadístico

Revisar e implementar, cuando corresponda:

- Intervalos de confianza.
- Intervalo de Wilson.
- Dependencia entre renglones de una misma nota.
- Correlación intraclase.
- Efecto de diseño.
- Sensibilidad estadística.
- Limitaciones de representatividad.

Verificar el intervalo nominal de 10,75 % a 19,28 % y el efecto de diseño reportado de 1,69.

Si no existe una población objetivo o un diseño de muestreo defendible, limitar las conclusiones al análisis descriptivo del lote.

No utilizar los intervalos de confianza como prueba de representatividad empresarial.

### PM-06 — Conciliación documental

Conciliar:

- Cuatro notas sin detalle.
- Diez totales que no cuadran.
- Campos faltantes.
- Diferencias entre importes.
- Llaves duplicadas.
- Registros sin correspondencia.
- Totales entre fuentes.

Conservar las discrepancias no resueltas.

No rellenar datos faltantes mediante inferencias no verificadas.

### PM-07 — Calidad del catálogo

Analizar:

- Variaciones ortográficas.
- Categorías inconsistentes.
- Identidades duplicadas.
- Valores faltantes por estado.
- Normalización de productos.
- Impacto de las diferencias entre versiones.

Generar evidencia reproducible de cada hallazgo.

### PM-08 — Prueba retrospectiva

Ejecutar la comparación entre:

- `Original_Comprobantes.xlsx`.
- `Comprobantes_Revisados.xlsx`.
- Hoja `Historial_Correcciones`.

Utilizar exclusivamente copias de los archivos autorizados del proyecto.

Registrar:

- Hash de cada fuente.
- Llaves de correspondencia.
- Registros comparables.
- Cambios identificados.
- Campos afectados.
- Correcciones efectuadas.
- Discrepancias persistentes.
- Casos ambiguos.
- Limitaciones del contraste.

Determinar si los cambios aportan evidencia independiente de la clasificación REVISAR.

La prueba puede respaldar conclusiones sobre transcripción, transformación y corrección documental, pero no demuestra por sí sola causas del proceso operativo empresarial.

No incorporar información privada adicional ni la población de 510 notas.

Si un archivo no está disponible o tiene restricciones, registrar el bloqueo y continuar con las demás tareas.

### PM-09 — VSM

Elaborar dos diagramas diferenciados:

1. VSM actual derivado del flujo documental conocido.
2. VSM futuro correspondiente al diseño propuesto.

Identificar como pendientes de medición:

- Cycle Time.
- Lead Time.
- Tiempo de espera.
- Tiempo de retrabajo.
- Tiempo de valor agregado.
- Cuellos de botella operativos.

No inventar tiempos para completar gráficamente el VSM.

### PM-10 — Lean y 5S

Mejorar las herramientas:

- Cinco principios Lean.
- Ocho desperdicios.
- 5S.
- Kaizen.
- Poka-Yoke.
- Gestión visual.
- Estandarización.

Rotular la aplicación de 5S digitales como ejercicio del taller académico cuando no exista evidencia de implementación empresarial.

Diferenciar las mejoras demostradas de las propuestas.

### PM-11 — Entregables oficiales

Preparar y verificar:

- Informe Word de Lean.
- Informe Word de Seis Sigma.
- Informe Word de DMAIC.
- Versiones PDF.
- Excel correspondientes.
- Presentaciones.
- Gráficos.
- Anexos.
- Formatos reproducibles.

Comprobar la disponibilidad y funcionalidad de los recursos sustitutos antes de retirar cualquier enlace externo.

### PM-12 a PM-17 — Validaciones pendientes

Mantener un registro de las decisiones que requieren intervención humana:

- PM-12: procedencia del lote y definición de la población.
- PM-13: entrevista VOC.
- PM-14: medición de tiempos reales.
- PM-15: concordancia entre revisores mediante MSA y kappa.
- PM-16: responsables nominales, metas, plazos, puntajes y tolerancias.
- PM-17: conciliación definitiva de hashes y versiones.

PM-17 debe avanzarse técnicamente con todas las copias disponibles, dejando pendientes únicamente las fuentes que no puedan recuperarse.

Preparar instrumentos, formatos y protocolos para facilitar la posterior obtención de información empresarial.

No inventar respuestas ni marcar como aprobadas las decisiones pendientes.

## 6. Conciliación de versiones y AUD-012

Codex principal deberá dirigir esta actividad.

Existe evidencia de que dos agentes utilizaron el mismo Excel, pero diferentes versiones del Data Mart.

Por tanto:

- No descartar un hallazgo porque no aparezca en otra versión.
- No generalizar un defecto localizado a todas las versiones.
- Identificar cada paquete y archivo mediante SHA-256.
- Registrar los commits asociados.
- Comparar los archivos publicados con sus fuentes.
- Verificar las huellas declaradas en `auditoria.json`.
- Comparar claves, agregados y categorías.

Revisar específicamente:

`NP-025089-02`

`f488e328a40d19b7`

`herramietas`

`herramientas`

Utilizar como punto de partida:

`revision/evidencia_copia_main_20261124.json`

Claude debe proporcionar los hashes y la procedencia de su copia cuando estén disponibles.

Clasificar cada incidencia como:

- Reproducida.
- No reproducida.
- Específica de versión.
- Corregida y verificada.
- Pendiente de evidencia.

No atribuir modificaciones a una persona o agente sin evidencia.

## 7. Mejoras adicionales de calidad

Los tres agentes deberán identificar e implementar mejoras adicionales que no estén contempladas en las propuestas anteriores.

Prestar especial atención a:

- Consistencia metodológica entre Lean, Seis Sigma y DMAIC.
- Calidad de las conclusiones.
- Correspondencia entre objetivos, resultados y propuestas.
- Claridad de los diagramas.
- Calidad de las tablas.
- Interpretación estadística.
- Gráficos nativos en Excel.
- Dashboard de indicadores.
- Automatización de validaciones.
- Documentación de fórmulas.
- Diseño de controles preventivos y detectivos.
- Gestión de riesgos.
- Protocolos de implementación.
- Plan de seguimiento.
- Reproducibilidad.
- Calidad visual y preparación para la exposición académica.

No aplicar herramientas estadísticas solo para incrementar la cantidad de contenido.

Cada herramienta debe tener una finalidad y datos adecuados.

## 8. Protocolo de colaboración mediante GitHub

Utilizar el Issue #1 como canal central de coordinación.

Cada agente debe publicar:

- Tarea asumida.
- Archivos que modificará.
- Dependencias.
- Hallazgos.
- Evidencias.
- Commits generados.
- Pruebas realizadas.
- Bloqueos.
- Solicitudes de revisión.

Mantener ramas independientes.

Ramas de referencia:

- `codex/informe-y-costo-beneficio`
- `claude/excel-dmaic-oficial`
- Una rama de integración administrada por Codex principal.

Reutilizar las ramas existentes cuando corresponda.

No realizar force push, sobrescribir trabajo ajeno ni modificar simultáneamente los mismos archivos binarios.

Antes de modificar un Word, Excel o presentación compartidos, coordinar su propiedad en la matriz de tareas.

Cuando un agente finalice una tarea, otro agente deberá revisarla independientemente.

Las discrepancias deben quedar documentadas hasta su resolución.

## 9. Archivos centralizados de coordinación

Crear o reutilizar los siguientes archivos:

```text
coordinacion/
├── PLAN_MAESTRO.md
├── MATRIZ_TAREAS.csv
├── CONTRATO_DE_DATOS.md
├── DECISIONES.md
├── TRAZABILIDAD_FUENTES.csv
├── HALLAZGOS_CONSOLIDADOS.md
├── VALIDACIONES.md
├── BLOQUEOS.md
└── INFORME_INTEGRACION.md
```

Evitar duplicar archivos equivalentes que ya existan. Si existen, consolidarlos conservando el historial.

Cada tarea debe registrar:

- Identificador.
- Propuesta de origen.
- Prioridad.
- Agente responsable.
- Agente revisor.
- Estado.
- Archivos afectados.
- Criterio de aceptación.
- Evidencia.
- Commit.
- Dependencias.
- Bloqueos.

Estados permitidos:

- Pendiente.
- En ejecución.
- En revisión.
- Observado.
- Corregido.
- Verificado.
- Bloqueado por evidencia.
- Pendiente de aprobación humana.

No utilizar el estado Verificado sin evidencia de revisión.

## 10. Fases de ejecución colaborativa

### Fase 1 — Sincronización

Cada agente deberá:

- Revisar el Issue #1.
- Revisar las respuestas Q1 a Q7.
- Revisar las propuestas existentes.
- Revisar los commits y las ramas actualizadas.
- Identificar tareas ya completadas.
- Confirmar sus responsabilidades.
- Identificar conflictos y dependencias.

Codex principal consolidará la planificación.

### Fase 2 — Normalización

Establecer el contrato común de indicadores y fuentes.

Resolver las diferencias que puedan solucionarse mediante evidencia.

Mantener explícitamente las decisiones humanas pendientes.

### Fase 3 — Desarrollo paralelo

Codex principal trabajará en integración, trazabilidad y automatización.

Codex Alexjhona trabajará en documentos, diagramas, presentaciones y economía.

Claude trabajará en Excel, estadística, DMAIC y verificación retrospectiva.

Los agentes deben compartir resultados intermedios que afecten el trabajo de los demás.

### Fase 4 — Revisión cruzada

- Claude revisará el rigor metodológico de los documentos de Codex Alexjhona.
- Codex Alexjhona revisará la claridad, coherencia y presentación de los resultados de Claude.
- Codex principal comprobará la consistencia técnica de ambos.
- Claude y Codex Alexjhona revisarán independientemente la integración final.

Todo hallazgo crítico debe ser corregido o quedar documentado como limitación no resoluble con la evidencia disponible.

### Fase 5 — Integración y validación

Codex principal integrará los cambios compatibles en una rama independiente.

Ejecutará todas las pruebas disponibles.

La integración definitiva a `main` deberá realizarse mediante Pull Request y aprobación correspondiente.

### Fase 6 — Evaluación final

Cada agente evaluará independientemente el producto integrado.

Si existen diferencias relevantes entre las evaluaciones, deberán justificarlas con evidencia.

No asignar una nota máxima por el simple cumplimiento de tareas.

## 11. Pruebas y criterios de aceptación

Antes de considerar finalizado el trabajo, verificar:

- Los documentos utilizan denominadores coherentes.
- Los indicadores pueden recalcularse.
- Las fórmulas Excel no presentan errores.
- Las fórmulas responden correctamente a cambios de parámetros.
- Los gráficos coinciden con sus datos.
- Los informes coinciden con los Excel.
- Las presentaciones coinciden con los informes.
- Los PDFs no contienen problemas de renderizado.
- Las tablas y diagramas son legibles.
- Los hashes están asociados a las versiones correctas.
- Las afirmaciones causales cuentan con evidencia suficiente.
- Los supuestos económicos están identificados.
- Las simulaciones no se presentan como resultados reales.
- Los archivos originales permanecen intactos.
- No se divulga información empresarial privada adicional.
- Los resultados son reproducibles.
- Las limitaciones metodológicas permanecen visibles.
- Las decisiones pendientes no se presentan como aprobadas.
- Los formatos y enlaces funcionan.
- Los entregables pueden abrirse correctamente.

Cuando sea técnicamente posible, implementar pruebas automatizadas que comprueben estas condiciones.

Registrar también las pruebas que no pudieron ejecutarse y su motivo.

## 12. Rúbrica interna de calidad

Evaluar el trabajo sobre 100 puntos:

| Criterio | Puntos |
|---|---:|
| Fundamentación metodológica | 12 |
| Calidad y trazabilidad de datos | 15 |
| Rigor estadístico | 15 |
| Aplicación Lean | 10 |
| Aplicación Seis Sigma | 10 |
| Desarrollo DMAIC | 12 |
| Propuestas de mejora y controles | 8 |
| Validación y reproducibilidad | 10 |
| Calidad documental y visual | 5 |
| Organización de entregables | 3 |
| **Total** | **100** |

Convertir el resultado a una escala de 20 puntos.

Objetivo aspiracional: alcanzar al menos 95/100, equivalente a 19/20, siempre que la evidencia disponible lo permita.

La nota debe reflejar el estado real del trabajo.

La ausencia de implementación empresarial o de evidencia operativa no debe compensarse inventando resultados.

## 13. Entregables finales

La versión integrada deberá contener:

1. Informes académicos mejorados.
2. Documentos Word editables.
3. Informes PDF.
4. Libros Excel funcionales.
5. Presentaciones corregidas.
6. Dashboard de calidad.
7. Diagramas Lean y DMAIC.
8. Análisis estadístico reproducible.
9. Análisis de sensibilidad.
10. Modelo costo-beneficio parametrizable.
11. Evidencia retrospectiva PM-08, si las fuentes autorizadas están disponibles.
12. Registro de trazabilidad.
13. Código y scripts de validación.
14. Plan de implementación empresarial.
15. Plan de control.
16. Instrumentos para obtener evidencia pendiente.
17. Matriz consolidada de mejoras.
18. Informe de auditoría final.
19. Registro de cambios.
20. Pull Request de integración.

## 14. Informe final obligatorio

Codex principal deberá elaborar un informe que incluya:

- Estado inicial del proyecto.
- Deficiencias identificadas.
- Mejoras implementadas.
- Mejoras verificadas independientemente.
- Comparación antes y después del producto documental.
- Resultados estadísticos actualizados.
- Discrepancias resueltas.
- Discrepancias pendientes.
- Limitaciones.
- Archivos modificados.
- Commits relevantes.
- Pruebas ejecutadas.
- Aportes de cada agente.
- Calificación individual de los tres agentes.
- Calificación consolidada.
- Actividades que todavía requieren participación de la empresa.

No confundir la mejora del producto académico con una mejora demostrada del proceso empresarial.

## 15. Instrucción de inicio

Codex principal, Codex Alexjhona y Claude:

Comiencen revisando el estado actualizado del repositorio, el Issue #1, las respuestas Q1–Q7, las propuestas de mejora y los últimos commits.

Confirmen sus responsabilidades, identifiquen las tareas ya ejecutadas y coordinen la distribución de las pendientes.

Después, ejecuten las mejoras de manera paralela, compartan sus resultados, realicen revisiones cruzadas y corrijan las observaciones.

No se limiten a responder este mensaje con un plan de trabajo. Implementen efectivamente las actividades autorizadas y publiquen evidencias reproducibles.

No esperen decisiones humanas que no sean imprescindibles para la tarea que estén ejecutando.

El trabajo se considerará finalizado cuando exista una versión integrada, revisada, reproducible y preparada para su entrega académica, con las limitaciones y validaciones empresariales pendientes debidamente identificadas.

La prioridad no es terminar primero ni demostrar que un agente tiene razón. La prioridad es construir conjuntamente el mejor producto técnicamente defendible.
