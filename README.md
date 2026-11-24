# HIDROCOM KALLPA

## Registro y validación de notas de pedido

Proyecto académico de Lean Seis Sigma para el curso Mejora de Procesos y Calidad Total de la Universidad Peruana Unión. Incluye un diagnóstico documental y una propuesta de mejora para el registro, revisión y publicación de información comercial.

Fecha de revisión: 24 de noviembre de 2026.

## Entregables

- [Informe del proyecto en PDF](U3_Informe_HIDROCOM.pdf): 15 páginas con contexto, alcance, charter, 5W2H, SIPOC, medición, Pareto descriptivo, verificación documental, propuestas de mejora, plan PDCA, control y anexo de pendientes.
- [Excel DMAIC](U3_Formato_DMAIC_HIDROCOM.xlsx): 13 hojas con datos fuente preservados, cálculos, seguimiento de 38 renglones pendientes y un prototipo de validación de nuevos registros.
- [Presentación editable](https://chatgpt.com/space/page_ca61c7120d948191aaa3a90517d367db): 15 diapositivas. El enlace conserva los permisos propios del documento en ChatGPT y permite exportarlo desde su visor.

## Diagnóstico del corte documental

La muestra contiene 73 notas y 262 renglones. La fuente clasifica 206 renglones como DISPONIBLE, 38 como REVISAR y 18 como EXCLUIR. La proporción por revisar es 14,50 % de los renglones de la muestra completa.

REVISAR expresa un estado documental y no equivale a un defecto confirmado. Los registros excluidos se conservan y no se reclasifican automáticamente como errores.

## Uso del Excel

1. Consultar Resumen y Medir para entender los conteos y sus denominadores.
2. Mantener las hojas fuente Datos, Comprobantes y Fechas como copia del corte examinado.
3. Completar las decisiones pendientes en Definir y los parámetros de control aprobados en Control.
4. Documentar cada revisión en Pendientes con responsable, evidencia y fecha. Cambiar una etiqueta sin evidencia no demuestra corrección.
5. Utilizar Validar como prototipo de control de captura. La tolerancia monetaria y las reglas aplicables deben acordarse antes de liberar registros.
6. Completar Beneficios únicamente cuando existan costos, tiempos y volumen medidos. Los campos pendientes no deben sustituirse por ceros supuestos.

## Información pendiente

- Confirmar la pertenencia de las notas a HIDROCOM y aclarar sus fechas respecto del inicio de actividades reportado.
- Aprobar campos obligatorios, base de precio, tratamiento de estados y definición de defecto CTQ.
- Definir meta, plazo y responsables nominales.
- Ejecutar y medir el piloto antes de afirmar resultados de mejora.
- Obtener tiempos y costos con evidencia antes de calcular beneficios económicos.

El informe y la presentación distinguen los hallazgos documentales de las hipótesis y las propuestas. No se declara una mejora ya lograda, un ahorro económico ni una certificación del sistema de gestión.

## Contexto del proyecto

### Organización y actividad descrita

El manual identifica a GRUPO HIDROCOM KALLPA E.I.R.L. como una organización dedicada a la comercialización, distribución y abastecimiento de productos ferreteros para instalaciones de agua y desagüe, almacenamiento de agua y riego. Entre sus productos menciona tuberías y conexiones PVC y CPVC, tanques, biodigestores, mangueras, termas solares y complementos del rubro.

La operación descrita atiende principalmente a micro y pequeñas empresas de la región de Puno, mediante un almacén principal y transporte de reparto. Esta descripción proviene del manual suministrado y no constituye una verificación independiente de la operación actual.

El Sistema de Gestión de la Calidad del manual es una propuesta académica. Sus políticas, metas y planes no se utilizan como evidencia de resultados alcanzados.

### Curso y equipo

- Curso: Mejora de Procesos y Calidad Total.
- Universidad: Universidad Peruana Unión.
- Programa: Ingeniería de Sistemas.
- Periodo académico: 2026-2.
- Docente indicado en el material: Mg. Esteban Tocto Cano.
- Integrantes registrados en el manual: Gutierrez Morales Jhon Alex, Mullisaca Condori Carlos Augusto y Mamani Mamani Ciro Wagner.

Los nombres identifican al equipo académico. La asignación de Champion, líder, analistas, revisor y dueño del proceso sigue pendiente y no se deduce de otros trabajos.

### Propósito y selección del proceso

El proyecto desarrolla el proceso de registro y validación de notas de pedido para generar información comercial confiable. Se eligió este alcance porque existen registros documentales que permiten reproducir conteos y contrastar versiones. El material no contiene mediciones suficientes de tiempos de reparto, exactitud física de inventario o errores de entrega para sustentar un proyecto sobre esos resultados.

El objetivo de diseño es establecer controles de captura, revisión, aprobación y publicación que permitan reducir pendientes con evidencia. El valor numérico de la meta y la fecha de cumplimiento requieren acuerdo con el dueño del proceso.

## Alcance y flujo propuesto

El alcance comprende la recepción de una nota o su evidencia, el registro de sus datos, la validación, la resolución documentada de observaciones, la aprobación de una versión y su publicación en reportes comerciales.

1. **Recibir e identificar:** asignar o comprobar un identificador estable y conservar el original.
2. **Registrar:** transcribir los campos preservando la diferencia entre un valor confirmado, un dato dudoso y un dato ausente.
3. **Validar:** revisar los campos aplicables, el estado comercial y la base de precio antes de comparar cantidades, precios e importes.
4. **Resolver o justificar:** documentar el motivo de revisión o exclusión y la evidencia necesaria para decidir.
5. **Aprobar la versión:** registrar quién revisó y aprobó el dato y qué evidencia utilizó.
6. **Publicar y conciliar:** comprobar que la fuente y el conjunto publicado correspondan a la misma versión.

Este flujo es una propuesta por validar en campo. Los archivos permiten observar capas de registro y publicación, pero no acreditan una observación completa del proceso operativo ni sus tiempos.

Quedan fuera del alcance la evaluación de trabajadores, la exactitud del inventario físico, el desempeño de entregas y la afirmación de mejoras no medidas.

## Material utilizado y trazabilidad

| Fuente del paquete suministrado | Uso en el proyecto |
| --- | --- |
| `SEM2_Esquema_Manual_HIDROCOM_COMPLETADO.docx` | Contexto organizacional, procesos propuestos e identificación del equipo. |
| `Antecedentes_y_alcance.md` | Antecedentes históricos y limitaciones de la recopilación. |
| `Comprobantes_Revisados.xlsx` | Registros de notas, detalle, estados de fecha, revisión de campos e incidencias. |
| `Detalle.csv` y `Productos.csv` del Data Mart | Contraste de registros y categorías con la fuente Excel. |
| `auditoria.json` | Contraste de las huellas de fuente y archivos publicados. |

Las hojas Datos, Comprobantes y Fechas del Excel entregable preservan 8 916 celdas fuente verificadas. Las fechas se representan como fechas de hoja de cálculo conservando el día registrado. Los identificadores se mantienen como texto. Los originales del paquete no se modificaron.

## Interpretación de los datos

### Unidades de análisis

- **Nota:** documento identificado en la hoja Comprobantes. Hay 73 en la muestra.
- **Renglón:** detalle identificado por `id_detalle`. Hay 262 en la muestra.
- **Incidencia registrada:** entrada de un registro que mezcla observaciones, estados y condiciones documentales. Hay 151 entradas, pero no se interpretan como 151 defectos.

Estas unidades no son intercambiables. Ninguna tasa de defectos se obtiene dividiendo automáticamente las incidencias entre notas o renglones.

### Estados de uso del importe

| Estado de la fuente | Renglones | Proporción de los 262 renglones |
| --- | ---: | ---: |
| DISPONIBLE | 206 | 78,63 % |
| REVISAR | 38 | 14,50 % |
| EXCLUIR | 18 | 6,87 % |
| Total | 262 | 100,00 % |

DISPONIBLE es una etiqueta de uso en la fuente, no una certificación de que todos los campos estén verificados. REVISAR indica una revisión pendiente y no confirma un error. EXCLUIR requiere conservar la justificación y no se convierte automáticamente en defecto.

La suma de importes de renglones DISPONIBLE es S/ 26 509,70. Es un importe documental del corte y no se utiliza como ventas auditadas, utilidad, costo de mala calidad ni beneficio del proyecto.

### Fechas y origen de la muestra

| Estado de fecha | Notas | Proporción de 73 notas |
| --- | ---: | ---: |
| Estimada | 39 | 53,42 % |
| Real sin etiqueta de discordancia | 28 | 38,36 % |
| Año discordante | 6 | 8,22 % |

Las fechas registradas abarcan del 27/01/2025 al 09/03/2026. El antecedente reporta inicio de actividades el 09/03/2026. Falta explicar la relación entre esa fecha y los documentos anteriores, así como confirmar la pertenencia del lote a la empresa.

Por esta razón, el análisis utiliza un corte documental revisado el 24/11/2026. No se atribuye a un periodo comercial confirmado ni se presenta como serie mensual de ventas.

## Desarrollo DMAIC

### Definir

El charter delimita el registro y validación documental. El 5W2H diferencia lo observado de lo pendiente. El SIPOC propone proveedores, entradas, seis pasos, salidas y clientes internos que requieren validación con la organización.

La meta SMART, el plazo y los responsables nominales permanecen pendientes. No se reutilizan metas de otros procesos del manual.

### Medir

La línea descriptiva cuenta los estados existentes de las notas y renglones. El denominador de la proporción REVISAR es la muestra completa de 262 renglones.

Para medir conformidad se necesita aprobar primero el defecto CTQ, su evidencia, la unidad y las oportunidades homogéneas. El Excel incorpora los campos U, D y O y las fórmulas condicionadas para DPMO y nivel sigma. Permanecen pendientes hasta completar esos requisitos.

No se construye una gráfica de control ni se afirma capacidad del proceso sin una secuencia operativa y subgrupos comparables.

### Analizar

Los 38 renglones REVISAR se agrupan mediante una regla descriptiva exclusiva. Cada renglón entra en el primer criterio que cumple, en este orden:

1. Estado PEDIDO en la nota o el renglón.
2. Cantidad, precio unitario o subtotal vacío.
3. Diferencia de importe consignada en la fuente distinta de cero.
4. Observación no vacía o estado de renglón DUDOSA.
5. Ningún criterio anterior: motivo no explicitado en el detalle, por consultar en otras hojas y el original.

Esta prioridad evita doble conteo. No representa gravedad ni demuestra causa raíz.

| Condición principal | Renglones | Porcentaje de los 38 pendientes | Acumulado |
| --- | ---: | ---: | ---: |
| Estado PEDIDO en nota o renglón | 13 | 34,21 % | 34,21 % |
| Campos numéricos incompletos | 7 | 18,42 % | 52,63 % |
| Observación o lectura dudosa documentada | 7 | 18,42 % | 71,05 % |
| Motivo no explicitado en el detalle | 6 | 15,79 % | 86,84 % |
| Diferencia de importe consignada en la fuente | 5 | 13,16 % | 100,00 % |

Las cuatro primeras condiciones reúnen 33 de 38 pendientes. El estado PEDIDO puede ser válido; hace falta aclarar su regla de inclusión comercial. Los cinco casos con diferencia de importe incluyen una fila con base de precio por millar. Una diferencia numérica no se declara error aritmético confirmado sin revisar la base y el documento.

### Evidencias documentales verificadas

| Condición | Evidencia | Límite de la conclusión |
| --- | --- | --- |
| Campo numérico incompleto | `NP-025059-03` tiene cantidad 100 e importe 25, pero precio unitario vacío. | Se confirma el vacío. No se infiere un precio dividiendo importe entre cantidad. |
| Diferencia de importe consignada | `NP-025072-04` tiene cantidad 2, precio 5, subtotal 100 y diferencia 90. | El registro contiene la diferencia. El original debe sustentar qué dato corresponde corregir. |
| Categoría distinta entre capas | `NP-025089-02`, Tarrajas: herramientas en Excel y herramietas en `CategoriaOriginal` del CSV. | Se confirma la diferencia entre archivos, no su autor o fecha de origen. |
| Desalineación de versión | El hash del Excel actual difiere del declarado en `auditoria.json`; los nueve CSV coinciden con sus huellas registradas. | Se confirma la desalineación documental, no su causa operativa. |

El Ishikawa del informe propone preguntas sobre personas, método, sistema, material, medición y entorno. Son hipótesis por verificar, no causas humanas u operativas demostradas.

### Mejorar

Las ocho ideas de mejora son:

1. Campos obligatorios según tipo de nota.
2. Base de precio explícita.
3. Catálogo estable de productos y categorías.
4. Motivo obligatorio para REVISAR y EXCLUIR.
5. Evidencia y aprobación al resolver una observación.
6. Conciliación de versión antes de publicar.
7. Organización documental con 5S digital.
8. Revisión Kaizen de problemas repetidos.

Las puntuaciones de impacto y esfuerzo están vacías para evaluación del equipo. No se fabricó una prioridad numérica.

El formulario Validar es un prototipo de Poka Yoke. Comprueba presencia de datos, base de precio positiva, coherencia numérica y evidencia de aprobación. Requiere definir la tolerancia monetaria. No modifica las notas originales y no acredita por sí solo la verdad documental.

El plan PDCA propone aprobar criterios, probar controles, comparar mediciones equivalentes y ajustar el procedimiento según resultados. El piloto de la operación todavía no se ha ejecutado.

### Controlar

| Indicador propuesto | Situación inicial o disponibilidad |
| --- | --- |
| Renglones REVISAR / renglones del lote | 38 / 262 = 14,50 %. |
| Fechas estimadas o discordantes / notas | 45 / 73 = 61,64 %. Mide estado documental, no errores confirmados. |
| Cierres con evidencia y responsable / cierres declarados | Sin resoluciones de intervención registradas. Si no hay cierres, el resultado es no aplicable. |
| Publicaciones conciliadas / publicaciones realizadas | No existe una serie de publicaciones verificable. |

Las metas, umbrales, frecuencias y responsables deben acordarse. Una integración posterior con el flujo de publicación o Power BI es una propuesta, no una automatización ya implementada.

## Evaluación económica

No se dispone de tiempos medidos antes y después, costo horario validado, inversión ni costos recurrentes de la intervención. Por ello, no se declara un ahorro.

Cuando existan datos, el cálculo propuesto será:

```text
Ahorro mensual realizable =
  (minutos antes - minutos después) / 60
  × volumen mensual comparable
  × costo por hora
  × factor de realización sustentado

Beneficio anual neto =
  ahorro mensual realizable × 12
  - costo inicial
  - costo recurrente anual
```

Un resultado negativo debe conservarse. Un dato no disponible no equivale a cero.

## Verificación de entregables

- Informe PDF de 15 páginas, renderizado y revisado visualmente.
- Presentación editable de 15 diapositivas, revisada visualmente.
- Excel de 13 hojas, con 18 comprobaciones de cálculos y controles.
- Contraste de 8 916 celdas de las hojas fuente con el material extraído.
- Comprobación de que no quedaron datos temporales de prueba en las entradas del formulario y de evaluación económica.

Estas comprobaciones validan el desarrollo documental y las fórmulas probadas. No equivalen a una prueba de la operación real ni a resultados de un piloto empresarial.

## Próximos pasos

1. Confirmar el origen de las notas y resolver la cronología con evidencia.
2. Acordar el CTQ, los campos obligatorios y las reglas para cada estado.
3. Aprobar meta, plazo, equipo y dueño del proceso.
4. Acceder a originales o evidencias autorizadas para resolver observaciones.
5. Ejecutar un piloto con reglas estables y registrar tiempos y resultados.
6. Actualizar informe, Excel y presentación con los resultados efectivamente medidos.

El proyecto conserva exclusivamente el alcance de HIDROCOM KALLPA y los datos sustentados en su material suministrado.
