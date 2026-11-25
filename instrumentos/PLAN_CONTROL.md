# Plan de control propuesto

Todavía no está operando en la empresa. Las frecuencias y funciones de esta tabla son recomendaciones para aprobación; nombres, umbrales y metas siguen pendientes.

| Indicador o control | Definición | Fuente / unidad | Frecuencia propuesta | Función / reacción propuesta |
|---|---|---|---|---|
| Estado REVISAR | REVISAR / renglones del mismo lote | Registro del lote; 38/262 al corte | Por lote | Dueño/revisor; investigar motivos sin declarar todos como defectos |
| Completitud sintáctica | Nulos en tres campos / campos inspeccionados | Detalle; 30/786 al corte | Por lote | Analista; verificar excepciones sin imputación |
| Cierres trazables | Cierres con evidencia, revisor y fecha / cierres declarados | Seguimiento; sin cierre real aún | Por cierre/lote | Revisor; reabrir cierres sin fundamento; sin cierres = no aplicable |
| Publicación conciliada | Archivos que pasan conciliación / publicaciones realizadas | Manifiesto y cotejo de claves/agregados | Antes de publicar | Responsable de publicación; detener versión incoherente |
| ID único | Duplicados de id_detalle identificados | Claves del registro | En captura/importación | Sistema propuesto; alertar duplicado, no borrarlo automáticamente |
| Base e importe | Importe vs cantidad × precio/base con tolerancia aprobada | Registro y original autorizado | En captura/revisión | Revisor; conservar ambigüedad y evidencia |
| Tiempos reales | Variables definidas en PROTOCOLO_TIEMPOS.md | Observación; sin línea base real | Por diseño de medición | Observador; verificar comparabilidad y eventos extremos |
| FPY operativo | Unidades conformes en primera pasada / unidades procesadas | Registro temporal sin retrabajo; pendiente | A definir | Dueño; no sustituir por DISPONIBLE al corte |

La reacción y aceptación del control requieren reglas aprobadas. Los prototipos actuales alertan; no impiden por sí solos editar Excel ni prueban que el dato sea verdadero. Registrar excepción, evidencia, decisión y versión del procedimiento para cada liberación.
