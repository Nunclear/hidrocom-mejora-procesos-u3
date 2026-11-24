# 16 · Propuestas de mejora de Claude (priorizadas)

Respuesta al comentario 7146568385 del issue #1. Las propuestas (PM-xx) **se derivan de los hallazgos AUD-xxx** de esta auditoría. Remiten al plan `10_PLAN_MAESTRO_MEJORA.md` (tareas T-xx) y al prompt ejecutable `13_PROMPT_IMPLEMENTACION.md`, sin duplicarlos.

**Naturaleza de cada cifra:**
- **[H]** hecho verificado en archivos
- **[C]** resultado calculado (reproducible con `14_EVIDENCIAS_AUDITORIA/recalculo_independiente.py`)
- **[Hi]** hipótesis
- **[P]** propuesta
- **[E]** escenario

**Ninguna** cifra es un resultado operativo real.

**Prioridad.** La primera se justifica por el riesgo para la validez o la nota (P0 > P1 > P2 > P3); a igual nivel, va primero la que desbloquea a otras. No se asignan puntajes, costos ni plazos inventados.

---

## A. Ejecutables con los archivos existentes

### PM-01 · Un único CTQ y nivel sigma en todos los entregables
- **Evidencia:**
  - [H] Seis Sigma PDF pág. 5 y `Metricas!I6:J6`: 38 167,94 / 3,2724.
  - [H] `04 Formato M2!B8:B12` y lámina 5: 44 529 / 3,20.
  - [C] NP-025138-01: 2 000 × 0,24 = 480 = subtotal. La «diferencia» de 479,52 se debe solo a la etiqueta «millar».
- **Hallazgo:** AUD-002 (P1).
- **Prioridad:** P1. Es la pregunta más probable del jurado («¿cuál es su sigma?») y desbloquea PM-02, PM-03 y el informe Word.
- **Cambio:**
  - Adoptar un criterio oficial. Propongo D = 34 [C]: DPMO 43 257,0 y σ 3,2141. Alternativa: D = 30, solo vacíos.
  - Publicar la tabla de sensibilidad de 4 filas en Seis Sigma, M2, lámina 5 e informe.
  - Documentar la regla de las bases kg y millar.
- **Archivos:** `02_Seis_Sigma/*.pdf|xlsx`; `04_Producto_Final/U3_Formato_DMAIC_HIDROCOM.xlsx` (M2), `.pptx` (lámina 5), `scripts/llenar.py` y `deck.py`; informe Word (Codex).
- **Dependencias:** decisión del equipo sobre el criterio (pregunta Q4).
- **Aceptación:** un único valor de σ en todos los documentos; la tabla existe.
- **Comprobación:** `grep -r "3,2"` en el texto extraído; ejecutar el script (sección C).

### PM-02 · Reformular la «causa raíz» como condición documental + causa candidata por verificar
- **Evidencia:** [H] `Formato A2!D15:D16` («RESPALDADA»), `A2!A22`, láminas 2 y 7. [C] 13/13 y 21/22 son asociaciones **por construcción**: el estado REVISAR se asignó por esas condiciones.
- **Hallazgo:** AUD-003 (P1).
- **Prioridad:** P1. Es el «error clásico» que, según la plantilla, el jurado busca.
- **Cambio:** veredictos «Condición documental confirmada [H]» y «Causa candidata [Hi], verificación pendiente».
  - Conclusión: «Los datos del lote no permiten verificar la causa raíz. La causa candidata, ausencia de reglas de captura y clasificación, se verificará observando el registro real (PM-13) o comparando `Original_Comprobantes` con `Revisados` (PM-08)».
- **Archivos:** Formato A2; láminas 2 y 7; `figuras.py` (leyenda del Ishikawa); capítulo 3 del Word.
- **Dependencias:** ninguna.
- **Aceptación:** ningún «confirmada/respaldada» como veredicto causal.
- **Comprobación:** lectura de A2 y de las láminas.

### PM-03 · Simulación como rango de escenarios
- **Evidencia:** [H] `Formato I2!A13`, lámina 9: un único valor de 4,96 %. [C] Con una eficacia del 100/75/50/25 % resultan 4,96/7,35/9,73/12,12 %.
- **Hallazgo:** AUD-004 (P1).
- **Prioridad:** P1. Hoy el valor único es el máximo teórico.
- **Cambio:** tabla de escenarios [E] rotulada «simulación retrospectiva declarada; no es piloto».
- **Archivos:** Formato I2; lámina 9; capítulo 4 del Word.
- **Dependencias:** PM-02.
- **Aceptación:** rango visible.
- **Comprobación:** fórmula 38 − 25·e.

### PM-04 · Beneficio con sensibilidad y escenario negativo
- **Evidencia:** [H] `Formato C2!B5:B8` = S/ 255 con «1 lote/mes». [C] El lote abarca 13,3 meses, lo que da 2,86 REVISAR/mes y −S/ 91,80. El punto de equilibrio está en 12,2 REVISAR/mes.
- **Hallazgo:** AUD-005 (P1).
- **Prioridad:** P1. El rol de finanzas (U3-S3) lo refutaría.
- **Cambio:** tres escenarios [E] con supuestos visibles. La mejora se justifica también por la calidad de la información, como beneficio cualitativo. Hay que coordinarlo con el costo-beneficio de Codex.
- **Archivos:** Formato C2; lámina 11; Excel costo-beneficio (Codex).
- **Dependencias:** PM-12 (volumen real) para el valor definitivo.
- **Aceptación:** el escenario negativo es visible.
- **Comprobación:** script, sección K.

### PM-05 · Línea base con incertidumbre y dependencia intra-nota
- **Evidencia:** [C] IC Wilson 10,75–19,28 %; ICC 0,246; efecto de diseño 1,69; n efectivo ≈ 155.
- **Hallazgo:** AUD-007 (P2).
- **Cambio:** reportar el IC y una nota de que el piloto debe compararse por nota.
- **Archivos:** DMAIC Medir, M2, Seis Sigma.
- **Aceptación:** IC presente.
- **Comprobación:** script, sección H.

### PM-06 · Notas sin detalle y conciliación de totales
- **Evidencia:** [C]
  - 4 notas sin renglones (NP-025111, -127, -137, -140).
  - 10 notas cuyo total ≠ suma de renglones; el conjunto difiere del que marca la fuente (NP-025126 sin marca; NP-025068 y NP-025084 discrepan entre hojas).
  - 23 notas sin total.
- **Hallazgos:** AUD-008 y AUD-009 (P2).
- **Cambio:** nota metodológica (73 notas; 69 con detalle) y tabla de conciliación en el anexo.
- **Archivos:** DMAIC 03 (Medir y anexo), Formato M2.
- **Aceptación:** tabla presente.
- **Comprobación:** script, secciones A y E.

### PM-07 · Cuantificar lo que hoy son mejoras sin dato
- **Evidencia:** [C] 6 grupos de variantes de producto («Cola sintética» ×3, «Imprimante/s»…); análisis de vacíos por estado.
- **Hallazgos:** AUD-020 (P3) y análisis de faltantes (06).
- **Cambio:**
  - tabla de variantes como sustento de la mejora «catálogo»;
  - tabla vacío × estado;
  - en Lean, cuantificar los desperdicios «defectos» (35) e «inventario» (38 en 22 notas).
- **Archivos:** Lean (desperdicios), DMAIC Analizar y Mejorar.
- **Aceptación:** tablas presentes.
- **Comprobación:** script, sección J.

### PM-08 · Prueba retrospectiva de la causa candidata con `Original_Comprobantes.xlsx`
- **Evidencia:**
  - [H] En la copia local del paquete existen `Original_Comprobantes.xlsx` (SHA-256 `e29a8d6a…`, coincide con `auditoria.json`) y `Historial_Correcciones` dentro de `Comprobantes_Revisados.xlsx`.
  - [Hi] Comparar la captura original con la revisada mostraría qué campos se omitieron al capturar y cuáles se corrigieron después. Esa evidencia es **independiente** del estado REVISAR.
- **Hallazgo:** AUD-003.
- **Prioridad:** P1. Es la única vía, sin ir a la empresa, para acercarse a verificar la causa.
- **Cambio:** script que cruza Original con Revisado por id. Salida: tasa de campos vacíos en la captura original frente a la versión revisada, y tipo de corrección.
- **Archivos:** nuevo script en `14_EVIDENCIAS_AUDITORIA`; DMAIC Analizar.
- **Dependencias:** autorización del usuario para usar esos archivos (Q3).
- **Aceptación:** tabla «original → revisado» por tipo de campo.
- **Comprobación:** recuento reproducible.
- **Nota:** **no se ejecutó** en esta auditoría. Es una propuesta.

### PM-09 · Lean: VSM actual derivado y VSM futuro de diseño
- **Evidencia:** [H] Lean pág. 3 y `VSM!E6:G11` vacíos; no hay estado futuro.
- **Hallazgo:** AUD-010 (P1 para Lean).
- **Cambio:** dos figuras con iconografía VSM. El actual lleva WIP 38 en 22 notas, FPY 78,6 % y «t = por medir». El futuro muestra los Poka-Yoke en Registrar y Validar. Leyenda: observado / derivado / hipotético.
- **Archivos:** Lean PDF y xlsx.
- **Aceptación:** dos figuras rotuladas.
- **Comprobación:** inspección visual.

### PM-10 · Lean: 5S rotulada como ejercicio del taller y 5S propuesta para las carpetas de la empresa
- **Evidencia:** [H] Lean pág. 5 y `Evidencia_5S.csv`.
- **Hallazgo:** AUD-011 (P2).
- **Archivos:** Lean.
- **Aceptación:** título explícito.
- **Comprobación:** lectura.

### PM-11 · Entregables oficiales completos y coherentes
- **Evidencia:** [H] No hay `.docx` en ninguna rama. El README raíz enlaza una presentación de ChatGPT. Los PDF no tienen portada, índice, bibliografía APA ni figuras clave.
- **Hallazgos:** AUD-014 (P1) y AUD-022 (P2).
- **Cambio:**
  - Word oficial (Codex), con las cifras de PM-01 a PM-06;
  - retirar el enlace externo;
  - portada, índice, APA y figuras (Pareto combinado, Ishikawa, flujo, VSM, árbol CTQ).
  - Además, hacer reproducible el Formato 04: hoja Datos y COUNTIFS (AUD-017); fechas como fecha (AUD-015); Pareto con IFS (AUD-016); protección de hojas (AUD-024); plantillas versionadas y `REPRODUCIR.md` (AUD-019).
- **Dependencias:** PM-01 a PM-04 antes del Word.
- **Aceptación:** checklist 15, ítems 19 a 26.

## B. Requieren información de la empresa o del equipo

| ID | Propuesta | Hallazgo | Por qué no se puede hacer ahora | Aceptación |
|---|---|---|---|---|
| PM-12 | Confirmar el origen y la cronología del lote; decidir la población (73 notas frente a la versión ampliada de 510) | AUD-001 (P0), AUD-018 | Requiere declaración del dueño y decisión del equipo | Declaración + DECISIONES.md |
| PM-13 | VOC (guion de 15 min) y árbol CTQ validado | AUD-013 | Requiere al usuario del reporte | Acta |
| PM-14 | Tiempos del registro (hoja de cronometraje, 30 notas) para VSM, PCE, beneficio e I-MR | AUD-010, AUD-005 | No hay tiempos; no se inventan | Datos medidos |
| PM-15 | MSA por atributos (kappa, 40 renglones, 2 revisores) | AUD-023 | Requiere originales y un segundo revisor | Kappa ≥ 0,70 |
| PM-16 | Aprobar roles, meta, puntajes y tolerancia, y propagarlos | AUD-006, AUD-024 | Son decisiones humanas | DECISIONES.md marcado |
| PM-17 | Reproducir o retirar las evidencias de hash y «herramietas» | AUD-012 | Requiere la copia del paquete del autor de `main` | Hash publicado o evidencias retiradas |

## C. Requieren implementación o piloto real

| ID | Propuesta | Condición previa | Aceptación |
|---|---|---|---|
| PM-18 | Piloto con un lote nuevo (4 semanas) usando la plantilla validada; % REVISAR por lote **y por nota** con IC; gráfico p **solo** con orden real de registro | PM-12, PM-16, PM-15 | Criterio de éxito acordado **antes** del piloto |

## Orden sugerido

1. PM-12, PM-16 y PM-17 (decisiones; se pueden pedir hoy).
2. PM-01, luego PM-02, PM-03, PM-04, PM-05 y PM-06.
3. PM-07 y PM-08 (si se autoriza).
4. PM-09 y PM-10.
5. PM-11 (Word final y reproducibilidad).
6. PM-13, PM-14 y PM-15 cuando haya acceso a la empresa.
7. PM-18.

## Coincidencias y discrepancias con Codex

Codex aún **no publicó** `propuestas_mejora/PROPUESTAS_MEJORA_CODEX.md` (su rama sigue en `b9d921b`). La comparación se hace contra su comentario 7146072315.

| Tema | Codex | Claude | Estado |
|---|---|---|---|
| Línea base: 262, 38, 14,50 %, 35 defectos en 22 renglones, 44 529 / 3,20 σ, unión de 25 | Verificado | Verificado [C] | **Coinciden** |
| CTQ «propuesto» y desplazamiento de 1,5 declarado | Sí | Sí | **Coinciden** |
| Valor de D | 35 | 34 recomendado (artefacto millar) o 30 | **Discutir** (PM-01) |
| Causa | «La evidencia respalda priorizar… se asocian con 25 de 38» | Asociación **por construcción**: no respalda causa, solo prioriza condiciones | **Discutir** (PM-02). Su formulación de «priorizar» es aceptable; la mía elimina «respaldada» como veredicto. |
| Simulación | 4,96 % como valor único | Rango 4,96–12,12 % | **Discutir** (PM-03) |
| Beneficio | S/ 255 «escenario base», con sensibilidad anunciada | Escenario base + −S/ 91,80 con el volumen del rango | **Coinciden en la sensibilidad**; discutir cuál es el escenario base (PM-04) |
| Fechas | 16,0 % frente a 12,0 % descriptivo | Ídem; Fisher p = 0,47 | **Coinciden** |

## Preguntas pendientes para el usuario y el equipo

1. **Q1.** ¿De dónde provienen las 73 notas y qué significa el inicio de actividades del 09/03/2026? (PM-12)
2. **Q2.** ¿Se usa solo el lote de 73 notas o la versión ampliada (510 notas)? ¿Hay permiso para usarla? Uno de los archivos dice PRIVADO. (PM-12)
3. **Q3.** ¿Autorizan usar `Original_Comprobantes.xlsx` e `Historial_Correcciones` para la prueba retrospectiva PM-08?
4. **Q4.** ¿Qué criterio de D se adopta: 30, 34 o 35? (PM-01)
5. **Q5.** ¿Quiénes son Champion, BB, GB y dueño del proceso? ¿Qué meta, plazo y puntajes aprueban? (PM-16)
6. **Q6.** ¿Puede el autor de `main` compartir el hash y la ruta de su copia del paquete? (PM-17)
7. **Q7.** ¿Aplico ya en 04 las propuestas PM-01 a PM-06 y PM-11 que me corresponden, o esperamos a coordinar con Codex?

## Limitaciones

- PM-08 no se ejecutó.
- No se revisaron las imágenes originales, el manual ni los antecedentes.
- La versión ampliada solo se conoce por sus totales.
- El auditor es coautor de 04: esas propuestas son autocríticas, pero deben revisarlas otros.
