# Registro de validaciones

## Ejecutadas por A antes de la integración

- Lectura binaria del ZIP exterior e interior: cuatro archivos extraídos coinciden byte por byte con la copia local. Evidencia: EVIDENCIA_COPIA_MAIN.json. Los nueve CSV coinciden con su auditoria.json; la huella del Excel declarada en ese JSON difiere del Excel real. NP-025089-02 conserva la categoría antigua en el CSV del ZIP v3.
- Extracción congelada de valores de las tres hojas fuente ya publicadas en el corte e3b5a60. Sin ampliar población.

## A ejecutar y registrar

`python herramientas/validar_integracion.py` recalcula métricas desde el corte congelado y contrasta los libros, enlaces y entregables. `python -m unittest discover -s herramientas -p "test_*.py"` verifica casos límite del modelo y de los controles. Las salidas identifican versión/commit y hashes.

Una lectura de caché Excel no equivale a recálculo de fórmulas. El revisor debe indicar qué motor ejecutó, qué entradas cambió y qué pruebas restauró. Los PDF/Word/PPTX requieren revisión visual, además de integridad estructural. Mantener una lista explícita de comprobaciones no ejecutadas.
