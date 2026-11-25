# Registro de validaciones

A comparó bytes del ZIP v3, congeló solo 73 notas/262 renglones y contrastó las fuentes de los libros con ese congelado. Las huellas de C se identifican como reportadas cuando no hubo bytes disponibles a A.

Ejecutar `python herramientas/ejecutar_pruebas.py` y `python herramientas/validar_integracion.py --final --revision REVISION`. Las salidas de validacion/ registran métricas, escenarios, fórmulas en caché, integridad y enlaces. Leer cachés no equivale a recálculo Excel. Los archivos temporales Office ~$ se excluyen.

El dashboard pasó 18 comprobaciones Artifact Tool, incluida mutación restaurada 30→31→30. Las cadenas vacías esperadas se contrastan con estado fuente y fórmula antes de considerarlas vacíos conocidos.

Los Word se exportaron en Microsoft Word; A revisó las 31 páginas PDF y las 35 láminas únicas. Los PPTX pasaron integridad, geometría, fuentes de referencia e importación. Los reportes públicos contienen huellas; las imágenes privadas de QA se conservan en .qa/ y pueden regenerarse.

No ejecutado por A: recálculo nativo Excel de todos los libros, prueba PowerPoint/Google Slides, reproducción con bytes de primera captura PM08 o Data Mart posterior C, entrevistas, MSA de campo y piloto. Los recálculos nativos reportados por B/C se atribuyen expresamente.

La revisión y calificación final B/C siguen solicitadas. La ejecución de GitHub Actions debe comprobarse en el PR: crear el flujo no demuestra que pasó.
