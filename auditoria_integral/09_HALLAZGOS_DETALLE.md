# 09 · Hallazgos en detalle

Generado por `14_EVIDENCIAS_AUDITORIA/generar_hallazgos.py`; la matriz tabular está en `09_MATRIZ_HALLAZGOS.csv`.

**Total: 24** · P0 = 1 · P1 = 9 · P2 = 9 · P3 = 5


### Hallazgo AUD-001

- **Título:** Procedencia y cronología del lote no confirmadas: 70 de 73 notas son anteriores al inicio de actividades declarado
- **Prioridad:** P0
- **Trabajo afectado:** Lean, Seis Sigma, DMAIC, 04
- **Archivo:** Comprobantes (Excel DMAIC); README; informes
- **Ruta:** 03_DMAIC/U3_DMAIC_HIDROCOM.xlsx
- **Página/hoja/celda/línea:** Comprobantes!D6:D78; README §Fechas; DMAIC pág. 2
- **Evidencia encontrada:** Fechas del 27/01/2025 al 09/03/2026; solo 3 notas en o después del 09/03/2026; 39 estimadas y 6 discordantes
- **Resultado esperado:** Muestra de la empresa con período verificable
- **Resultado observado:** Lote digitalizado retrospectivamente, de pertenencia no confirmada
- **Explicación técnica:** Si las notas no son de HIDROCOM o de su operación actual, el proyecto no mide su proceso
- **Impacto académico:** Compromete la validez externa de los tres trabajos
- **Impacto estadístico:** Ningún indicador puede generalizarse a la empresa
- **Impacto empresarial:** Decisiones basadas en otra realidad
- **Causa probable:** Recuperación histórica de notas de un negocio anterior o familiar (hipótesis)
- **Corrección propuesta:** Obtener una declaración del dueño sobre el origen de las notas; reformular el objeto de estudio como 'calidad documental del lote digitalizado' hasta confirmarlo; en 04, retirar 'único proceso de HIDROCOM con registros reproducibles' sin esa salvedad
- **Datos adicionales necesarios:** Confirmación escrita del dueño; explicación de la fecha de inicio
- **Dependencias:** —
- **Criterio de aceptación:** Cada informe declara la procedencia confirmada o la limitación en su resumen
- **Método para verificar:** Revisión textual de los resúmenes y de la lámina 2
- **Tipo de corrección:** Requiere información adicional de la empresa

### Hallazgo AUD-002

- **Título:** Dos criterios de defecto (D = 30 y D = 35) sin conciliar; una diferencia es un artefacto de la base millar y la regla kg no está documentada
- **Prioridad:** P1
- **Trabajo afectado:** Seis Sigma, 04
- **Archivo:** U3_Seis_Sigma_HIDROCOM.pdf; U3_Formato_DMAIC_HIDROCOM.xlsx; PPTX
- **Ruta:** 02_Seis_Sigma; 04_Producto_Final
- **Página/hoja/celda/línea:** Seis Sigma pág. 5; Formato M2!B8:B12; lámina 5
- **Evidencia encontrada:** 3,2724 σ (30/786) frente a 3,2004 σ (35/786); NP-025138-01: 2000 × 0,24 = 480 = subtotal, pero la base 'millar' produce una diferencia de 479,52; NP-025066-04/06 (kg) calculados como 375 sin regla escrita
- **Resultado esperado:** Un único CTQ y D en todos los documentos
- **Resultado observado:** Dos líneas base sin explicación
- **Explicación técnica:** D depende de la regla; la base del precio altera la coherencia
- **Impacto académico:** Confunde al jurado ('¿cuál es el sigma?')
- **Impacto estadístico:** La línea base cambia 0,07 σ según el criterio
- **Impacto empresarial:** Ninguno directo
- **Causa probable:** Trabajo en paralelo de dos agentes
- **Corrección propuesta:** Adoptar un criterio oficial (recomendado: D = 34, sin el artefacto millar, o D = 30 con nota) y publicar la tabla de sensibilidad de 4 filas en los tres trabajos; documentar la regla para kg y millar
- **Datos adicionales necesarios:** Aprobación del CTQ por el equipo
- **Dependencias:** AUD-013
- **Criterio de aceptación:** La misma cifra de sigma en Seis Sigma, Formato, PPTX e informe; existe la tabla de sensibilidad
- **Método para verificar:** grep de '3,2' en los documentos; recálculo con recalculo_independiente.py
- **Tipo de corrección:** Ejecutable mediante cálculos

### Hallazgo AUD-003

- **Título:** La verificación de la causa raíz en 04 usa asociaciones definicionales (circulares)
- **Prioridad:** P1
- **Trabajo afectado:** 04 (DMAIC producto final)
- **Archivo:** U3_Formato_DMAIC_HIDROCOM.xlsx; PPTX
- **Ruta:** 04_Producto_Final
- **Página/hoja/celda/línea:** A2!A15:D18, A22; láminas 2 y 7
- **Evidencia encontrada:** 13/13 PEDIDO y 21/22 numéricas están en REVISAR porque quien digitalizó asignó REVISAR por esas condiciones
- **Resultado esperado:** Causa verificada con un dato independiente de la clasificación
- **Resultado observado:** Se presenta la regla de clasificación como evidencia causal
- **Explicación técnica:** Una tasa del 100 % producida por la propia regla no prueba causalidad; Fisher p≈0 es trivial
- **Impacto académico:** Error clásico que el jurado busca
- **Impacto estadístico:** Inferencia inválida
- **Impacto empresarial:** Se podrían atacar síntomas de la digitalización y no del proceso de la empresa
- **Causa probable:** Presión de la plantilla por 'causa confirmada'
- **Corrección propuesta:** Reformular: 'condiciones documentales asociadas por construcción a REVISAR'; causa raíz candidata = ausencia de reglas de captura, a verificar observando la herramienta y el procedimiento reales (o revisando Original_Comprobantes frente a Revisados)
- **Datos adicionales necesarios:** Observación del registro; entrevista; comparación Original vs Revisado
- **Dependencias:** —
- **Criterio de aceptación:** A2 y lámina 7 distinguen condición, causa candidata y causa verificada; ninguna dice 'confirmada' sin un dato independiente
- **Método para verificar:** Revisión textual
- **Tipo de corrección:** Ejecutable inmediatamente (redacción); verificación real requiere información de la empresa

### Hallazgo AUD-004

- **Título:** La simulación 14,50 % → 4,96 % es circular y se presenta con un solo valor
- **Prioridad:** P1
- **Trabajo afectado:** 04
- **Archivo:** Formato I2!A13; PPTX lámina 9
- **Ruta:** 04_Producto_Final
- **Página/hoja/celda/línea:** I2!A13; lámina 9
- **Evidencia encontrada:** Se eliminan por construcción los 25 renglones de las categorías atacadas y se supone un 100 % de corrección
- **Resultado esperado:** Escenario con supuestos y rango
- **Resultado observado:** Un único valor optimista
- **Explicación técnica:** Es el máximo teórico; con 75/50/25 % de eficacia resultan 7,35/9,73/12,12 %
- **Impacto académico:** Sobreestima el efecto
- **Impacto estadístico:** Sin incertidumbre
- **Impacto empresarial:** Expectativas irreales
- **Causa probable:** Simplificación
- **Corrección propuesta:** Presentar la tabla de escenarios (100/75/50/25 %) y rotular 'máximo teórico de la simulación retrospectiva'; mantener 'no es piloto'
- **Datos adicionales necesarios:** —
- **Dependencias:** AUD-003
- **Criterio de aceptación:** Lámina 9 e I2 muestran el rango y el rótulo
- **Método para verificar:** Revisión de la lámina y la celda
- **Tipo de corrección:** Ejecutable mediante simulaciones declaradas

### Hallazgo AUD-005

- **Título:** El beneficio de S/ 255 depende de un supuesto de volumen incompatible con la cronología del lote
- **Prioridad:** P1
- **Trabajo afectado:** 04
- **Archivo:** Formato C2!B5:B8, A11; PPTX lámina 11
- **Ruta:** 04_Producto_Final
- **Página/hoja/celda/línea:** C2
- **Evidencia encontrada:** Supone 38 REVISAR/mes; el lote abarca 13,3 meses, lo que implica 2,86 REVISAR/mes → beneficio −S/ 91,80; equilibrio = 12,2 REVISAR/mes
- **Resultado esperado:** Beneficio con supuestos coherentes y análisis de sensibilidad
- **Resultado observado:** Un solo escenario favorable
- **Explicación técnica:** Volumen, minutos y costo hora sin evidencia
- **Impacto académico:** El rol de finanzas (U3-S3) lo refutaría
- **Impacto estadístico:** Resultado inestable ante el supuesto principal
- **Impacto empresarial:** Podría justificar una inversión sin retorno
- **Causa probable:** Falta de datos de volumen
- **Corrección propuesta:** Mostrar 3 escenarios (volumen según rango de fechas, 1 lote/mes, equilibrio) y aclarar que con el volumen observado el beneficio es negativo o nulo; justificar la mejora por calidad de la información (beneficio cualitativo)
- **Datos adicionales necesarios:** Volumen mensual real de notas; minutos medidos
- **Dependencias:** AUD-001
- **Criterio de aceptación:** C2 y lámina 11 muestran la sensibilidad y el escenario negativo
- **Método para verificar:** recalculo_independiente.py sección K
- **Tipo de corrección:** Ejecutable mediante cálculos; el valor real requiere información de la empresa

### Hallazgo AUD-006

- **Título:** Roles, meta y puntajes figuran como 'pendientes' en main y como 'propuesta' asignada por el agente en 04
- **Prioridad:** P1
- **Trabajo afectado:** Transversal
- **Archivo:** PDF de main; Formato 0, D1, I1; PPTX láminas 1 y 3; DECISIONES.md
- **Ruta:** raíz y 04
- **Página/hoja/celda/línea:** Lean pág. 1; Seis Sigma pág. 3; DMAIC pág. 3; Formato B9:B12
- **Evidencia encontrada:** Los PDF dicen 'No hay asignación nominal aprobada de roles'; 04 nombra Champion, BB y GB
- **Resultado esperado:** Decisiones del equipo aprobadas y consistentes
- **Resultado observado:** Dos versiones contradictorias; decisiones tomadas por un agente
- **Explicación técnica:** La plantilla exige roles, meta y matriz puntuada
- **Impacto académico:** Contradicción entre entregables
- **Impacto estadístico:** —
- **Impacto empresarial:** Responsabilidades indefinidas
- **Causa probable:** Falta de reunión de decisión
- **Corrección propuesta:** El equipo aprueba DECISIONES.md y la decisión se propaga a los tres trabajos y a 04; se retiran las marcas [PROPUESTA]
- **Datos adicionales necesarios:** Decisión del equipo
- **Dependencias:** —
- **Criterio de aceptación:** DECISIONES.md con todas las casillas marcadas; sin contradicciones en grep
- **Método para verificar:** grep 'Pendiente de designación' frente a los roles de 04
- **Tipo de corrección:** Ejecutable inmediatamente (decisión humana)

### Hallazgo AUD-007

- **Título:** Sin intervalos de confianza y sin considerar la dependencia de renglones dentro de una nota
- **Prioridad:** P2
- **Trabajo afectado:** Seis Sigma, DMAIC, 04
- **Archivo:** Informes y Excel
- **Ruta:** —
- **Página/hoja/celda/línea:** Medir / M2
- **Evidencia encontrada:** ICC 0,246; efecto de diseño 1,69; n efectivo ≈155; IC Wilson 10,8–19,3 %
- **Resultado esperado:** La línea base con incertidumbre
- **Resultado observado:** Valor puntual
- **Explicación técnica:** Los renglones de una nota comparten registrador, fecha y legibilidad
- **Impacto académico:** Rigor estadístico
- **Impacto estadístico:** Subestima la varianza
- **Impacto empresarial:** Metas mal calibradas
- **Causa probable:** Omisión
- **Corrección propuesta:** Reportar el IC y una nota sobre el conglomerado; comparar antes/después por nota
- **Datos adicionales necesarios:** —
- **Dependencias:** —
- **Criterio de aceptación:** La línea base muestra el IC
- **Método para verificar:** Cálculo en el script
- **Tipo de corrección:** Ejecutable mediante cálculos

### Hallazgo AUD-008

- **Título:** Los totales de nota no cuadran con los renglones y las hojas fuente discrepan entre sí
- **Prioridad:** P2
- **Trabajo afectado:** Datos (todos)
- **Archivo:** Comprobantes y Datos
- **Ruta:** 03_DMAIC xlsx
- **Página/hoja/celda/línea:** Comprobantes!diferencia_total
- **Evidencia encontrada:** 10 notas con diferencia en la fuente y 10 por recálculo, con conjuntos distintos (NP-025126: 430 frente a 1 130 sin marca; NP-025068 y NP-025084 con suma legible ≠ detalle); 23 notas sin total
- **Resultado esperado:** Totales conciliados o marcados
- **Resultado observado:** Inconsistencia no reportada
- **Explicación técnica:** Integridad entre la cabecera y el detalle
- **Impacto académico:** Hallazgo de datos no aprovechado
- **Impacto estadístico:** Posible defecto adicional del CTQ a nivel de nota
- **Impacto empresarial:** Reportes con totales errados
- **Causa probable:** Digitación en dos capas
- **Corrección propuesta:** Añadir el CTQ 'total de nota coherente' o al menos reportar la tabla; investigar las 3 discrepancias
- **Datos adicionales necesarios:** Originales de NP-025068, -084 y -126
- **Dependencias:** —
- **Criterio de aceptación:** Tabla de conciliación en el anexo
- **Método para verificar:** recalculo_independiente.py sección E
- **Tipo de corrección:** Ejecutable mediante cálculos

### Hallazgo AUD-009

- **Título:** 73 notas como denominador, pero solo 69 tienen renglones; 4 notas sin detalle no explicadas
- **Prioridad:** P2
- **Trabajo afectado:** DMAIC, Lean
- **Archivo:** Comprobantes frente a Datos
- **Ruta:** 03_DMAIC xlsx
- **Página/hoja/celda/línea:** NP-025111, -127, -137, -140
- **Evidencia encontrada:** 3 notas en estado PEDIDO y 1 dudosa sin renglones
- **Resultado esperado:** Explicar el denominador de notas
- **Resultado observado:** No se menciona
- **Explicación técnica:** Mezcla de poblaciones
- **Impacto académico:** Menor
- **Impacto estadístico:** Denominadores
- **Impacto empresarial:** —
- **Causa probable:** Notas sin detalle legible
- **Corrección propuesta:** Añadir una nota metodológica: 73 notas, 69 con detalle
- **Datos adicionales necesarios:** —
- **Dependencias:** —
- **Criterio de aceptación:** La nota aparece en Medir
- **Método para verificar:** Revisión textual
- **Tipo de corrección:** Ejecutable inmediatamente

### Hallazgo AUD-010

- **Título:** Lean: VSM sin tiempos ni estado futuro; PCE no calculable; sin instrumento de recolección
- **Prioridad:** P1
- **Trabajo afectado:** Lean
- **Archivo:** U3_Lean_HIDROCOM.pdf/xlsx
- **Ruta:** 01_Lean
- **Página/hoja/celda/línea:** Pág. 3; VSM!E6:G11
- **Evidencia encontrada:** Celdas de tiempo vacías; no hay VSM futuro ni dibujo con iconografía
- **Resultado esperado:** VSM actual y futuro con datos o con su protocolo
- **Resultado observado:** Tabla de etapas
- **Explicación técnica:** El VSM es la herramienta central de Lean
- **Impacto académico:** Nota de Lean limitada
- **Impacto estadístico:** —
- **Impacto empresarial:** No se ven esperas ni retrabajo
- **Causa probable:** Sin acceso a la operación
- **Corrección propuesta:** Dibujar el VSM actual con los datos derivados (WIP 38, FPY 78,6 %, t = por medir) y el VSM futuro como diseño; anexar la hoja de cronometraje
- **Datos adicionales necesarios:** Tiempos medidos (12_DATOS_PENDIENTES)
- **Dependencias:** AUD-001
- **Criterio de aceptación:** Dos figuras VSM rotuladas como observado, derivado o hipotético
- **Método para verificar:** Inspección visual
- **Tipo de corrección:** Ejecutable inmediatamente (diseño); tiempos requieren la empresa

### Hallazgo AUD-011

- **Título:** 5S aplicada a la carpeta académica, no al proceso de la empresa
- **Prioridad:** P2
- **Trabajo afectado:** Lean
- **Archivo:** Evidencia_5S.csv; PDF pág. 5
- **Ruta:** 01_Lean
- **Página/hoja/celda/línea:** pág. 5
- **Evidencia encontrada:** La intervención se hizo en el repositorio de entrega
- **Resultado esperado:** 5S en el área del proceso o declarada como ejercicio del taller
- **Resultado observado:** Se puede leer como intervención en la empresa
- **Explicación técnica:** Cumple el taller U3-S1/2, que pedía un espacio digital del equipo
- **Impacto académico:** Riesgo de malinterpretación
- **Impacto estadístico:** —
- **Impacto empresarial:** Sin efecto en la empresa
- **Causa probable:** Sin acceso a la empresa
- **Corrección propuesta:** Titular 'ejercicio 5S del taller (espacio digital del equipo)' y proponer una 5S para las carpetas de notas e imágenes de la empresa
- **Datos adicionales necesarios:** —
- **Dependencias:** —
- **Criterio de aceptación:** El título y el texto lo aclaran
- **Método para verificar:** Revisión textual
- **Tipo de corrección:** Ejecutable inmediatamente

### Hallazgo AUD-012

- **Título:** Las 'evidencias verificadas' de hash distinto y categoría 'herramietas' no se reproducen con la copia local del paquete
- **Prioridad:** P1
- **Trabajo afectado:** Lean, Seis Sigma, DMAIC, README
- **Archivo:** README; DMAIC pág. 8; Lean pág. 3; Verificar!B8:B9
- **Ruta:** raíz, 01, 03
- **Página/hoja/celda/línea:** DMAIC pág. 8 filas 3-4
- **Evidencia encontrada:** SHA-256 local del Excel fuente = ac6ab323… = auditoria.json; los 9 CSV coinciden; 'herramietas' no aparece; NP-025089-02 = herramientas
- **Resultado esperado:** Evidencias reproducibles por terceros
- **Resultado observado:** Evidencias no reproducibles
- **Explicación técnica:** Probablemente otra copia del paquete o una edición local del compañero
- **Impacto académico:** Las evidencias 'verificadas' pierden credibilidad
- **Impacto estadístico:** —
- **Impacto empresarial:** —
- **Causa probable:** Versiones distintas del paquete entre los integrantes
- **Corrección propuesta:** Que el autor publique el hash y la ruta de su copia; si no se reproduce, retirar o recalificar como 'observado en la copia X'
- **Datos adicionales necesarios:** Copia del paquete usada por el compañero
- **Dependencias:** AUD-019
- **Criterio de aceptación:** Ambas evidencias se reproducen con un paquete versionado o se retiran
- **Método para verificar:** sha256sum y grep (14_EVIDENCIAS/verificacion_hashes_paquete_local.txt)
- **Tipo de corrección:** Requiere información adicional (del equipo)

### Hallazgo AUD-013

- **Título:** Sin voz del cliente; CTQ propuesto sin validar con el usuario del reporte
- **Prioridad:** P2
- **Trabajo afectado:** Seis Sigma, DMAIC
- **Archivo:** Seis Sigma pág. 4; CTQ
- **Ruta:** 02_Seis_Sigma
- **Página/hoja/celda/línea:** Hoja CTQ
- **Evidencia encontrada:** 'Necesidad por validar'; no hay entrevista
- **Resultado esperado:** VOC → CTQ trazable
- **Resultado observado:** CTQ deducido de los datos
- **Explicación técnica:** Sin VOC el CTQ es una conjetura
- **Impacto académico:** Requisito metodológico
- **Impacto estadístico:** Las oportunidades no están validadas
- **Impacto empresarial:** El reporte podría no servir al usuario
- **Causa probable:** Sin acceso
- **Corrección propuesta:** Entrevista breve (guion en 12_DATOS_PENDIENTES) a quien usa el reporte; actualizar el árbol CTQ
- **Datos adicionales necesarios:** Entrevista
- **Dependencias:** —
- **Criterio de aceptación:** Acta de VOC con citas y árbol actualizado
- **Método para verificar:** Revisión
- **Tipo de corrección:** Requiere información adicional de la empresa

### Hallazgo AUD-014

- **Título:** Falta el informe Word con la plantilla oficial; la presentación de main es un enlace externo
- **Prioridad:** P1
- **Trabajo afectado:** DMAIC (producto final)
- **Archivo:** Plantilla del ZIP; README raíz
- **Ruta:** —
- **Página/hoja/celda/línea:** README línea 'Presentación editable DMAIC'
- **Evidencia encontrada:** No hay .docx en ninguna rama; enlace a chatgpt.com
- **Resultado esperado:** Word de 12–18 págs. con la plantilla + PPTX en el repositorio
- **Resultado observado:** PDF propio + enlace
- **Explicación técnica:** Incumple la entrega formal
- **Impacto académico:** Riesgo directo en la nota
- **Impacto estadístico:** —
- **Impacto empresarial:** —
- **Causa probable:** Trabajo asignado a Codex, aún en curso
- **Corrección propuesta:** Publicar U3_Informe_HIDROCOM.docx con la plantilla, usando las cifras del Formato 04 corregido; retirar el enlace externo y apuntar al PPTX de 04
- **Datos adicionales necesarios:** —
- **Dependencias:** AUD-002 a AUD-006
- **Criterio de aceptación:** .docx presente, 12–18 págs., sin recuadros [EQUIPO]
- **Método para verificar:** Abrir en Word y contar páginas
- **Tipo de corrección:** Ejecutable inmediatamente

### Hallazgo AUD-015

- **Título:** Fechas guardadas como texto en las hojas Datos de Lean y Seis Sigma
- **Prioridad:** P3
- **Trabajo afectado:** Lean, Seis Sigma
- **Archivo:** Hojas Datos
- **Ruta:** 01_Lean, 02_Seis_Sigma
- **Página/hoja/celda/línea:** Datos!C6:C267
- **Evidencia encontrada:** '2026-01-26 00:00:00' es str
- **Resultado esperado:** Tipo fecha
- **Resultado observado:** Texto
- **Explicación técnica:** Impide calcular con fechas
- **Impacto académico:** Menor
- **Impacto estadístico:** —
- **Impacto empresarial:** —
- **Causa probable:** Exportación
- **Corrección propuesta:** Convertir a fecha conservando el día
- **Datos adicionales necesarios:** —
- **Dependencias:** —
- **Criterio de aceptación:** ISNUMBER(C6)=VERDADERO
- **Método para verificar:** openpyxl data_type
- **Tipo de corrección:** Ejecutable inmediatamente

### Hallazgo AUD-016

- **Título:** El Pareto del DMAIC depende de una clasificación tecleada (Pendientes!H), no derivada por fórmula
- **Prioridad:** P3
- **Trabajo afectado:** DMAIC
- **Archivo:** U3_DMAIC_HIDROCOM.xlsx
- **Ruta:** 03_DMAIC
- **Página/hoja/celda/línea:** Pendientes!H6:H43; Analizar!B6:B10
- **Evidencia encontrada:** Valores; 0 discrepancias con el recálculo
- **Resultado esperado:** Derivación dinámica
- **Resultado observado:** Estática
- **Explicación técnica:** Si cambian los datos, el Pareto no se actualiza
- **Impacto académico:** Reproducibilidad
- **Impacto estadístico:** —
- **Impacto empresarial:** —
- **Causa probable:** Clasificación hecha en Python
- **Corrección propuesta:** Fórmula IFS que replique la regla de prioridad
- **Datos adicionales necesarios:** —
- **Dependencias:** —
- **Criterio de aceptación:** Al cambiar un estado en Datos, el Pareto cambia
- **Método para verificar:** Prueba manual en una copia
- **Tipo de corrección:** Ejecutable inmediatamente

### Hallazgo AUD-017

- **Título:** El Formato oficial (04) tiene U, D, O y el Pareto tecleados por script, sin hoja de datos vinculada
- **Prioridad:** P2
- **Trabajo afectado:** 04
- **Archivo:** U3_Formato_DMAIC_HIDROCOM.xlsx
- **Ruta:** 04_Producto_Final
- **Página/hoja/celda/línea:** M2!B8:B10; A1!B5:B9
- **Evidencia encontrada:** Valores constantes
- **Resultado esperado:** Cálculos trazables dentro del libro
- **Resultado observado:** Trazables solo por llenar.py
- **Explicación técnica:** Un revisor no ve de dónde salen los números
- **Impacto académico:** Reproducibilidad
- **Impacto estadístico:** —
- **Impacto empresarial:** —
- **Causa probable:** La plantilla no tiene hoja de datos
- **Corrección propuesta:** Añadir una hoja Datos (copia de 03) y fórmulas COUNTIFS
- **Datos adicionales necesarios:** —
- **Dependencias:** AUD-002
- **Criterio de aceptación:** M2 y A1 son fórmulas
- **Método para verificar:** Inspección de fórmulas
- **Tipo de corrección:** Ejecutable inmediatamente

### Hallazgo AUD-018

- **Título:** Existe una versión ampliada de los datos (510 comprobantes, 1 846 renglones, 2021–2026) no considerada al definir la población
- **Prioridad:** P1
- **Trabajo afectado:** Transversal
- **Archivo:** auditoria.json de la entrega 'DataCompleta' (equipo del usuario)
- **Ruta:** fuera del repositorio
- **Página/hoja/celda/línea:** —
- **Evidencia encontrada:** Totales agregados declarados por su auditoria.json
- **Resultado esperado:** Justificar por qué se estudia el lote de 73 notas
- **Resultado observado:** No se menciona
- **Explicación técnica:** La elección de la población determina todos los indicadores
- **Impacto académico:** Posible sesgo de selección
- **Impacto estadístico:** Un n mayor permitiría series y gráficos de control
- **Impacto empresarial:** Diagnóstico parcial
- **Causa probable:** Desconocimiento o decisión no documentada
- **Corrección propuesta:** El equipo decide: (a) mantener el lote de 73 y justificarlo, o (b) extender el análisis con las mismas reglas y comparar
- **Datos adicionales necesarios:** Confirmar la procedencia y el permiso de uso de la versión ampliada (hay un archivo marcado PRIVADO)
- **Dependencias:** AUD-001
- **Criterio de aceptación:** Decisión documentada en DECISIONES.md y en los tres informes
- **Método para verificar:** Revisión
- **Tipo de corrección:** Requiere información adicional (decisión del equipo)

### Hallazgo AUD-019

- **Título:** Reproducibilidad: fuentes, plantillas e imágenes no versionadas; los scripts dependen de rutas externas
- **Prioridad:** P2
- **Trabajo afectado:** Transversal
- **Archivo:** Repositorio
- **Ruta:** —
- **Página/hoja/celda/línea:** —
- **Evidencia encontrada:** Sin Comprobantes_Revisados.xlsx, Data Mart ni plantillas del ZIP en el repositorio
- **Resultado esperado:** Paquete reproducible (o hashes y ruta documentados)
- **Resultado observado:** Dependencia de copias personales
- **Explicación técnica:** Un tercero no puede reproducir
- **Impacto académico:** Reproducibilidad (1 punto)
- **Impacto estadístico:** —
- **Impacto empresarial:** —
- **Causa probable:** Tamaño y privacidad
- **Corrección propuesta:** Versionar las plantillas del curso y el Data Mart publicado (no el PRIVADO) o documentar los hashes; README de reproducción
- **Datos adicionales necesarios:** Permiso del equipo
- **Dependencias:** —
- **Criterio de aceptación:** Un clon limpio reproduce el Excel y el PPTX con un comando
- **Método para verificar:** Prueba en una carpeta limpia
- **Tipo de corrección:** Ejecutable inmediatamente

### Hallazgo AUD-020

- **Título:** Variantes de catálogo cuantificables no aprovechadas para sustentar la mejora 'catálogo'
- **Prioridad:** P3
- **Trabajo afectado:** Lean, DMAIC
- **Archivo:** Datos.producto_normalizado
- **Ruta:** —
- **Página/hoja/celda/línea:** —
- **Evidencia encontrada:** 169 nombres; 6 grupos con variantes (Cola sintética ×3, Imprimante/s…)
- **Resultado esperado:** Usar el dato
- **Resultado observado:** Mejora sin cuantificar
- **Explicación técnica:** Refuerza la propuesta con evidencia
- **Impacto académico:** Menor
- **Impacto estadístico:** —
- **Impacto empresarial:** —
- **Causa probable:** —
- **Corrección propuesta:** Añadir la tabla de variantes
- **Datos adicionales necesarios:** —
- **Dependencias:** —
- **Criterio de aceptación:** La tabla aparece
- **Método para verificar:** Script, sección J
- **Tipo de corrección:** Ejecutable mediante cálculos

### Hallazgo AUD-021

- **Título:** '62 % de fechas estimadas' mezcla unidades en el Formato 04
- **Prioridad:** P3
- **Trabajo afectado:** 04
- **Archivo:** U3_Formato_DMAIC_HIDROCOM.xlsx
- **Ruta:** 04
- **Página/hoja/celda/línea:** 0!E24; D1!A25; D2!C8; A2!C9
- **Evidencia encontrada:** 61,64 % = notas estimadas o discordantes; 61,83 % = renglones estimados
- **Resultado esperado:** Unidad explícita
- **Resultado observado:** Ambiguo
- **Explicación técnica:** —
- **Impacto académico:** Menor
- **Impacto estadístico:** —
- **Impacto empresarial:** —
- **Causa probable:** Redacción
- **Corrección propuesta:** Especificar la unidad en cada mención (la lámina 5 ya corregida en 4d1ec0d)
- **Datos adicionales necesarios:** —
- **Dependencias:** —
- **Criterio de aceptación:** Cada mención dice 'notas' o 'renglones'
- **Método para verificar:** grep '62 %'
- **Tipo de corrección:** Ejecutable inmediatamente

### Hallazgo AUD-022

- **Título:** Informes sin portada, índice, bibliografía formal ni figuras clave (VSM, flujo en 03, árbol CTQ)
- **Prioridad:** P2
- **Trabajo afectado:** Lean, Seis Sigma, DMAIC
- **Archivo:** PDF
- **Ruta:** 01–03
- **Página/hoja/celda/línea:** Todas
- **Evidencia encontrada:** Solo hay tablas; una figura en DMAIC pág. 5
- **Resultado esperado:** Formato académico completo
- **Resultado observado:** Formato de reporte técnico mínimo
- **Explicación técnica:** Presentación documental (2 puntos)
- **Impacto académico:** —
- **Impacto estadístico:** —
- **Impacto empresarial:** —
- **Causa probable:** Generación automática con ReportLab
- **Corrección propuesta:** Portada, índice, bibliografía en APA y figuras (ver 08)
- **Datos adicionales necesarios:** —
- **Dependencias:** AUD-014
- **Criterio de aceptación:** Las figuras listadas en 08 están presentes
- **Método para verificar:** Inspección visual
- **Tipo de corrección:** Ejecutable inmediatamente

### Hallazgo AUD-023

- **Título:** Sin análisis del sistema de medición (MSA por atributos) de la clasificación DISPONIBLE/REVISAR/EXCLUIR
- **Prioridad:** P2
- **Trabajo afectado:** Seis Sigma, DMAIC
- **Archivo:** —
- **Ruta:** —
- **Página/hoja/celda/línea:** Medir
- **Evidencia encontrada:** Una sola persona asignó los estados
- **Resultado esperado:** Kappa entre revisores
- **Resultado observado:** No evaluado
- **Explicación técnica:** La línea base depende de un juicio no calibrado
- **Impacto académico:** Rigor de Medir
- **Impacto estadístico:** Sesgo de medición desconocido
- **Impacto empresarial:** —
- **Causa probable:** Omisión
- **Corrección propuesta:** Dos revisores reclasifican 40 renglones con los originales; calcular kappa ≥ 0,7
- **Datos adicionales necesarios:** Originales; segundo revisor
- **Dependencias:** AUD-001
- **Criterio de aceptación:** Kappa reportado
- **Método para verificar:** Cálculo
- **Tipo de corrección:** Ejecutable mediante pruebas retrospectivas

### Hallazgo AUD-024

- **Título:** Formularios Poka-Yoke sin tolerancia aprobada y libros sin protección
- **Prioridad:** P3
- **Trabajo afectado:** Lean, DMAIC
- **Archivo:** PokaYoke!B5; Validar!B4
- **Ruta:** 01, 03
- **Página/hoja/celda/línea:** B4/B5 vacías
- **Evidencia encontrada:** No pueden emitir VALIDADO
- **Resultado esperado:** Tolerancia definida y fórmulas protegidas
- **Resultado observado:** Prototipo inerte
- **Explicación técnica:** Prueba incompleta
- **Impacto académico:** —
- **Impacto estadístico:** —
- **Impacto empresarial:** Control inoperante
- **Causa probable:** Decisión pendiente
- **Corrección propuesta:** Definir la tolerancia (p. ej. S/ 0,05) y proteger las hojas
- **Datos adicionales necesarios:** Aprobación del dueño
- **Dependencias:** AUD-006
- **Criterio de aceptación:** Prueba con 5 casos tipo
- **Método para verificar:** Pruebas en una copia
- **Tipo de corrección:** Ejecutable inmediatamente
