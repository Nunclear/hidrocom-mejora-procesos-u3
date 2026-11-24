# 10 · Plan maestro de mejora

Las tareas están ordenadas por nivel y dependencia.

**Tipo de corrección:**
- **E1**: ejecutable inmediatamente con los archivos existentes
- **E2**: mediante cálculos o reconstrucciones
- **E3**: mediante pruebas retrospectivas
- **E4**: mediante simulaciones declaradas
- **R1**: requiere información adicional de la empresa o del equipo
- **R2**: requiere implementación empresarial real

## Nivel 1 — Integridad de datos

| ID | Corrección | Prioridad | Archivos afectados | Dependencias | Procedimiento | Criterio de aceptación | Tipo |
|---|---|---|---|---|---|---|---|
| T01 | Confirmar el origen y la cronología del lote | P0 (AUD-001) | Los 3 informes, 04, README | — | Pedir al dueño una declaración escrita. Mientras no llegue, rotular el objeto de estudio como «calidad documental del lote digitalizado». | Cada resumen declara el origen confirmado o la limitación | R1 + E1 |
| T02 | Decidir la población: lote de 73 o versión ampliada | P1 (AUD-018) | DECISIONES.md, los 3 informes | T01 | Reunión del equipo. Si se amplía, aplicar las mismas reglas con `recalculo_independiente.py` adaptado. | Decisión documentada y justificada | R1 |
| T03 | Reproducir o retirar las evidencias de hash y «herramietas» | P1 (AUD-012) | README, Lean pág. 3, DMAIC pág. 8, Verificar | — | El autor publica el hash y la ruta de su copia. Si no se reproduce, retirar o recalificar la evidencia. | Ambas son reproducibles con un paquete versionado, o se retiran | R1 |
| T04 | Conciliar los totales de nota con los renglones | P2 (AUD-008) | Excel DMAIC (anexo), informe | — | Tabla de las 10 + 3 notas. Consultar originales de NP-025068, NP-025084 y NP-025126. | Tabla en el anexo | E2 |
| T05 | Documentar el denominador de 69 notas con detalle | P2 (AUD-009) | Medir (03 y 04) | — | Nota metodológica | Texto presente | E1 |
| T06 | Convertir las fechas de texto a fecha | P3 (AUD-015) | Lean y Seis Sigma › Datos | — | Conversión conservando el día | ISNUMBER verdadero | E1 |

## Nivel 2 — Rigor metodológico

| ID | Corrección | Prioridad | Archivos afectados | Dependencias | Procedimiento | Criterio de aceptación | Tipo |
|---|---|---|---|---|---|---|---|
| T07 | Un solo CTQ y D en los tres trabajos, con tabla de sensibilidad | P1 (AUD-002) | Seis Sigma (PDF y xlsx), Formato M2, PPTX lámina 5, informe | Decisión del equipo | Elegir D = 34 (recomendado) o D = 30. Añadir la tabla de 4 filas. Documentar las reglas de kg y millar. | Misma cifra de sigma en todos los documentos | E2 |
| T08 | Reformular la causa raíz | P1 (AUD-003) | Formato A2, láminas 2 y 7, informe cap. 3 | — | Separar condición documental, causa candidata y verificación pendiente. Retirar «respaldada» para las asociaciones definicionales. | Ningún documento afirma una causa verificada sin un dato independiente | E1 |
| T09 | Presentar la simulación como rango | P1 (AUD-004) | Formato I2, lámina 9, informe cap. 4 | T08 | Tabla con 100/75/50/25 % → 4,96/7,35/9,73/12,12 % | Rango y rótulo visibles | E4 |
| T10 | Sensibilidad del beneficio con escenario negativo | P1 (AUD-005) | Formato C2, lámina 11, costo-beneficio de Codex | T02 | 3 escenarios: −S/ 91,80 (volumen del rango), S/ 255 (1 lote/mes), equilibrio en 12,2 REVISAR/mes | Escenario negativo visible; la mejora también se justifica por la calidad de la información | E2 |
| T11 | Aprobar roles, meta y puntajes y propagarlos | P1 (AUD-006) | DECISIONES.md → los 3 trabajos y 04 | — | Reunión del equipo; actualizar todos los documentos | Sin contradicciones | R1 |
| T12 | Instrumento de VOC y árbol CTQ validado | P2 (AUD-013) | Seis Sigma, DMAIC Definir | — | Guion en 12_DATOS_PENDIENTES | Acta de la entrevista | R1 |
| T13 | Declarar la 5S como ejercicio del taller | P2 (AUD-011) | Lean pág. 5 | — | Cambiar título y texto | Texto claro | E1 |

## Nivel 3 — Fortalecimiento analítico

| ID | Corrección | Prioridad | Archivos afectados | Dependencias | Procedimiento | Criterio de aceptación | Tipo |
|---|---|---|---|---|---|---|---|
| T14 | Intervalo de confianza y efecto de diseño de la línea base | P2 (AUD-007) | Medir y M2 | — | Wilson + ICC (script, sección H) | IC reportado | E2 |
| T15 | Análisis de datos faltantes por estrato | P2 | Seis Sigma, DMAIC Analizar | — | Tablas de vacío × estado y vacío × archivo de origen | Tabla e interpretación | E2 |
| T16 | Variantes de catálogo como evidencia de la mejora «catálogo» | P3 (AUD-020) | Lean, DMAIC Mejorar | — | Tabla de 6 grupos | Tabla presente | E2 |
| T17 | MSA por atributos (kappa) | P2 (AUD-023) | DMAIC Medir | Originales | 40 renglones, 2 revisores | Kappa reportado | E3 / R1 |
| T18 | VSM actual (derivado) y VSM futuro (diseño) | P1 (AUD-010) | Lean | — | Figuras con rótulos observado / derivado / hipotético; t = por medir | 2 figuras | E1 |

## Nivel 4 — Calidad documental y visual

| ID | Corrección | Prioridad | Archivos afectados | Dependencias | Procedimiento | Criterio de aceptación | Tipo |
|---|---|---|---|---|---|---|---|
| T19 | Informe Word con la plantilla oficial | P1 (AUD-014) | Nuevo `04_Producto_Final/U3_Informe_HIDROCOM.docx` | T07–T11 | Codex lo redacta con las cifras de 04 ya corregidas | 12–18 págs., sin [EQUIPO] | E1 |
| T20 | Retirar el enlace a ChatGPT del README | P1 (AUD-014) | README raíz y 03/README | — | Apuntar al PPTX de 04 | Sin enlaces externos de autoría | E1 |
| T21 | Portada, índice, bibliografía APA y figuras | P2 (AUD-022) | Los 3 PDF | T18 | Ver la tabla de 08 | Figuras presentes | E1 |
| T22 | Unidades explícitas para el «62 %» | P3 (AUD-021) | Formato 04 | — | Editar `llenar.py` | grep limpio | E1 |

## Nivel 5 — Validación y reproducibilidad

| ID | Corrección | Prioridad | Archivos afectados | Dependencias | Procedimiento | Criterio de aceptación | Tipo |
|---|---|---|---|---|---|---|---|
| T23 | Hoja Datos y fórmulas vivas en el Formato 04 | P2 (AUD-017) | `llenar.py`, Formato | T07 | Copiar Datos y usar COUNTIFS en M2 y A1 | M2 y A1 son fórmulas | E1 |
| T24 | Pareto con fórmula IFS en DMAIC 03 | P3 (AUD-016) | Pendientes!H | — | Fórmula de prioridad | Pareto dinámico | E1 |
| T25 | Tolerancia y protección de los formularios | P3 (AUD-024) | Validar, PokaYoke | T11 | Definir la tolerancia; proteger las hojas | 5 casos de prueba pasan | E1 / R1 |
| T26 | Paquete reproducible | P2 (AUD-019) | Repositorio | T03 | Versionar las plantillas del curso y el Data Mart publicado (no el PRIVADO) o los hashes; README de reproducción | Un clon limpio regenera Excel y PPTX | E1 |
| T27 | Piloto real con un lote nuevo | — | Todos | T01, T11, T25 | Protocolo de 12_DATOS_PENDIENTES | % REVISAR medido con IC | R2 |
| T28 | Volver a correr esta auditoría (scripts de 14_) | — | — | T01–T26 | Ejecutar los 3 scripts y el checklist 15 | Checklist en verde | E1 |
