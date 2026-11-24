# Plan maestro de ejecución

La instrucción íntegra del usuario está en PROMPT_MEJORA_COLABORATIVA.md. Este plan consolida las 18 propuestas de Claude (PM-18 exige piloto), las siete de Codex y las tareas de coordinación; la correspondencia está en MATRIZ_TAREAS.csv.

## Propiedad y ramas

| Agente | Rama | Propiedad inicial | Revisor |
|---|---|---|---|
| A, Codex principal | codex/integracion-calidad | coordinacion/, datos_control/, herramientas/, validacion/, instrumentos/, PR | B y C |
| B, Codex Alexjhona | codex/informe-y-costo-beneficio | Word, PDF, PPTX, diagramas; código del modelo económico | C; A coteja resultados |
| C, Claude | claude/excel-dmaic-oficial | XLSX de 01/02/03/04, dashboard; estadística, PM-08 | A; B revisa claridad |

B define el modelo económico; C produce su libro coordinadamente. No editar el mismo binario en paralelo. Cada agente anuncia archivos y commits en Issue #1. Todos leen el contrato antes de propagar cifras. A integra archivos compatibles y preserva historia; nadie hace force push ni fusiona main sin la aprobación correspondiente.

## Secuencia

1. Congelar el corte ya publicado, establecer contrato y conciliar paquetes.
2. C corrige Excel, escenarios y estadísticas; B prepara documentos/diagramas/economía; A desarrolla verificadores e instrumentos.
3. C revisa documentos de B; B revisa claridad de C; A recalcula y contrasta ambos.
4. A incorpora commits exactos en integración, ejecuta checks y publica evidencia. Documenta cualquier tarea bloqueada por falta de originales o datos reales.
5. B y C revisan el commit integrado. A prepara PR y evaluación consolidada. La aprobación del PR es un paso distinto de la comprobación técnica.

Los originales externos permanecen inmutables. Una limitación empresarial explícita no se disfraza de tarea ejecutada ni impide corregir las tareas independientes.
