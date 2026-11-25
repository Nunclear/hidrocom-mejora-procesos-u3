# Dashboard de calidad documental

[Libro editable](Dashboard_Calidad_HIDROCOM.xlsx) con indicadores del lote, gráfico nativo de condiciones vinculado a sus celdas, tabla de porcentajes acumulados y escenarios separados. Contiene 73 notas y 262 renglones ya públicos; no incorpora la población ampliada.

- Dashboard: estados, proporción REVISAR, vacíos, sigma equivalente S30 y condiciones del Pareto.
- Escenarios: S30/S34/S35 y cuatro eficacias hipotéticas. Las unidades fraccionarias son expectativas del modelo, no resoluciones observadas.
- Corte y Notas: copias del corte congelado. Los cambios de población exigen una versión nueva del contrato.

FPY, origen empresarial, tiempos, VOC y MSA siguen pendientes. Los gráficos no acreditan mejora de la operación.

Generación: `herramientas/crear_dashboard.mjs`, usando `@oai/artifact-tool` del runtime empaquetado. `HIDROCOM_NODE_MODULES` permite indicar la ruta de sus módulos. Pruebas: `validacion/dashboard_pruebas.json`. Se ejecutaron cambios temporales de prueba y se restauraron antes de exportar. La evidencia de render se revisa aparte de los cálculos.
