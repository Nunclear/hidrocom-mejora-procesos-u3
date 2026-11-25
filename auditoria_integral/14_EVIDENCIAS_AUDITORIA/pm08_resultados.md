# PM-08 · Captura original frente a versión revisada (solo lectura)

Script: `pm08_original_vs_revisado.py` · Resultados completos: `pm08_resultados.json`.

**Autorización:** comentario 7146745531 del issue #1, Q3. La comparación se hizo sobre la copia del paquete del usuario, sin modificar ningún archivo.

**Archivos comparados:**
- `Original_Comprobantes.xlsx`: SHA-256 `e29a8d6a…`, coincide con `auditoria.json`.
- `Comprobantes_Revisados.xlsx`: SHA-256 `ac6ab323…`.

Solo se publican agregados.

## Resultados

| Medición | Resultado | Tipo |
|---|---|---|
| Renglones | Original 285 · Revisado 262 · Comunes 262 · Solo en el original **23** (retirados en la revisión) | [C] |
| Notas | 73 en ambos | [C] |
| Cantidad (262 comunes) | igual 256 · vacío→vacío 5 · vacío→completado 1 | [C] |
| Precio unitario | igual 232 · vacío→vacío 16 · vacío→completado **11** · valor cambiado 3 | [C] |
| Importe | igual 252 · vacío→vacío 9 · vacío→completado 1 | [C] |
| **Los 30 vacíos del revisado** | **30 de 30 ya estaban vacíos en la captura original** | [C] |
| Estado PEDIDO | 13 en el original = 13 en el revisado | [C] |
| Los 38 REVISAR del revisado | 38 presentes en el original; **37 ya eran REVISAR** y 1 era DISPONIBLE | [C] |
| Historial_Correcciones | 471 registros, del **17-11-2026 al 18-11-2026**. Por hoja: Detalle 401, Revisión 49, Comprobantes 21. Campos más corregidos: Clasificación 158, Categoría completada 105, Estado de revisión 41, nombre de producto 32 + 32, Registro 23, precio 15 | [C] |

## Interpretación y límites

**[Inferencia]** Lo que se puede concluir:
- Los campos vacíos **no se originaron en la revisión**. Ya estaban en la primera transcripción: la revisión completó 13 y no creó ninguno.
- El estado REVISAR se asignó **en la primera transcripción** (37 de 38). Esto confirma que la asociación «PEDIDO/vacío → REVISAR» es una regla de clasificación de quien digitalizó, no un efecto observado del proceso de la empresa (AUD-003).
- El historial fecha la digitalización y la revisión el 17 y 18 de noviembre de 2026. El conjunto de datos es una **reconstrucción documental hecha para el proyecto**, no un registro operativo de la empresa (refuerza AUD-001).
- **No se puede distinguir** si un vacío proviene de una nota física incompleta, ilegible o de una omisión al transcribir. Para eso hacen falta las imágenes originales.

**Límites:**
- Esto no prueba una causa operativa, no es una intervención en la empresa y no verifica cada dato frente al papel.
- Los 23 renglones retirados se contaron, pero no se clasificó su motivo (el historial registra 23 cambios en «Registro»).

## Consecuencia para los entregables

- En **Analizar**, la causa candidata debe reformularse con este dato: los vacíos existen desde la primera transcripción del documento. No hay base para atribuirlos a un sistema de captura de HIDROCOM, porque no se observó ninguno.
- Las mejoras de «validación en la captura» se convierten en una **propuesta para la digitalización y el registro futuros**, a confirmar en el Gemba.
