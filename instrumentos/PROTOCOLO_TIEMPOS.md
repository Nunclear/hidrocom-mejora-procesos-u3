# Protocolo propuesto de observación de tiempos

## Diseño

Confirmar primero el flujo y la unidad con el dueño del proceso. El VSM documental propone seis etapas; no prueba que sean el recorrido real. Medir un recorrido completo de la misma unidad, identificando excepciones y retrabajos.

Registrar instantes ISO 8601 con zona (por ejemplo, fecha real y desfase -05:00 en America/Lima); no escribir fechas de ejemplo como observaciones. Mantener entrada a cola, inicio de actividad, fin de actividad y salida. Medir en segundos y convertir de manera uniforme a minutos para el mapa.

## Variables y fórmulas

- Espera de una etapa = inicio de actividad − entrada a cola.
- Proceso de una etapa = fin − inicio. Las interrupciones se registran separadamente para evitar dobles conteos.
- Retrabajo = tiempo adicional identificado como repetición, con motivo y vínculo a la unidad.
- Lead time de un recorrido = salida final − entrada inicial, con el mismo alcance y reloj. Conciliarlo con tiempos de actividad, esperas y periodos no observados.
- Tiempo VA = suma de intervalos calificados por el destinatario como valor añadido. Esa clasificación debe validarse; no todo el procesamiento es VA.
- PCE = VA / lead time, únicamente si LT es positivo y los intervalos son comparables.

El TC por etapa se definirá operacionalmente con el equipo (duración de actividad por unidad). Si se mide tiempo entre salidas, registrarlo como cadencia en una variable distinta, no sustituirlo automáticamente por tiempo de procesamiento.

## Controles

Validar orden cronológico, reloj común, exclusividad de intervalos y unidad. No eliminar demoras para mejorar el promedio. Anotar datos incompletos y no calcular una duración a partir de una marca ausente. No rellenar VSM con tiempos supuestos. Acordar antes la cobertura temporal y la selección de casos; no afirmar representatividad sin diseño.

## Comparación de piloto

Usar idénticas definiciones y población comparable antes/después, separar tipo de nota y condiciones de excepción. Examinar la agrupación por nota y conservar evidencia de que el control se utilizó realmente. Un ensayo sintético de formulario no es una observación de tiempos ni un piloto empresarial.
