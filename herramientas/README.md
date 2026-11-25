# Reproducir las comprobaciones

Con Python y `requirements-validacion.txt`:

```powershell
python herramientas/ejecutar_pruebas.py
python herramientas/validar_integracion.py --final --revision revision-examinada
```

El corte congelado permite comprobar valores, indicadores, sensibilidad, cachés y formatos sin datos privados adicionales. Las salidas se escriben en validacion/. GitHub Actions usa los mismos comandos. Leer cachés no equivale a recalcular Excel.

`crear_informes_independientes.py` usa python-docx, reportlab y pypdfium2. `comprobar_pdf_word.py` exige exportar antes los Word desde Microsoft Word a `.qa/word/` con sus mismos nombres; renderiza y contrasta tokens, sin sustituir la inspección visual. `inspeccionar_documentos.py` extrae estructura y medios.

`crear_dashboard.mjs` usa `@oai/artifact-tool`, recalcula y restaura entradas temporales antes de exportar. Definir `HIDROCOM_NODE_MODULES` con el directorio del runtime suministrado.

`crear_presentaciones.mjs` contiene las especificaciones y callback usados en la sesión. `exportar_presentaciones.mjs` fue la vía local tras fallar la exportación de Artifact Session. Definir `HIDROCOM_NODE_MODULES`, `RUNTIME_NODE_MODULES`, `HIDROCOM_PYTHON` y `HIDROCOM_PRESENTATIONS_SKILL` con las rutas instaladas. Usa la referencia inmutable de `documentacion/plantillas/`. Para repetir la finalización, usar una nueva carpeta privada porque el finalizador no sobrescribe finales previos. Inspeccionar cada render además de ejecutar los controles.

`cerrar_documentacion.py` registra la migración de esta revisión y exige sus PDF de QA; no forma parte del validador ni del CI. Los scripts históricos de 04 corresponden a versiones anteriores: no regenerar encima de la entrega actual con sus reglas antiguas. No modificar datos para hacer pasar las pruebas.
