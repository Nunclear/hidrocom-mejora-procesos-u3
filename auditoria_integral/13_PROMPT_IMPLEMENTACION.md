# 13 · Prompt de implementación (para Codex u otro agente)

> Copia este documento completo como instrucción. Es autónomo: no depende de ninguna conversación previa.

## Contexto

Repositorio: `https://github.com/Nunclear/hidrocom-mejora-procesos-u3`.

- **Curso:** Mejora de Procesos y Calidad Total (UPeU, 2026-2).
- **Empresa:** GRUPO HIDROCOM KALLPA E.I.R.L.
- **Proceso:** registro y validación de notas de pedido.
- **Tres trabajos independientes:** `01_Lean`, `02_Seis_Sigma`, `03_DMAIC`.
- **Producto final del curso** en `04_Producto_Final` (rama `claude/excel-dmaic-oficial`):
  - Excel con el formato oficial;
  - presentación de 13 láminas;
  - scripts `llenar.py`, `deck.py`, `flujo.py` y `figuras.py`.
- **Plantillas oficiales:** ZIP del curso, carpeta «Proyecto final - Sesión 7».
- **Entrega:** 26-11-2026.

## Estado inicial (auditado el 24-11-2026)

| Rama | Commit |
|---|---|
| `main` | `e3b5a60` |
| `claude/excel-dmaic-oficial` | `4d1ec0d` (más la auditoría) |
| `codex/informe-y-costo-beneficio` | `b9d921b` |

- **Datos:** 73 notas (69 con detalle), 262 renglones (206 DISPONIBLE / 38 REVISAR / 18 EXCLUIR).
- **Fuente versionada:** `03_DMAIC/U3_DMAIC_HIDROCOM.xlsx` › Datos, Comprobantes, Fechas.
- **Verificación:** coinciden celda por celda con `Comprobantes_Revisados.xlsx` (SHA-256 `ac6ab323…`, igual al de `auditoria.json`).
- **Hallazgos:** 24 (1 P0, 9 P1, 9 P2, 5 P3). Ver `auditoria_integral/09_MATRIZ_HALLAZGOS.csv` y `09_HALLAZGOS_DETALLE.md`.

## Restricciones (obligatorias)

1. **No inventes** datos, tiempos, costos, entrevistas, roles aprobados ni resultados. Lo que dependa del equipo o de la empresa (T01, T02, T03, T11, T12, T17, T27) se deja **marcado como pendiente** y no se rellena.
2. No modifiques las hojas Datos, Comprobantes ni Fechas. Las correcciones de datos se documentan, no se sobrescriben.
3. Mantén los tres trabajos separados. No los fusiones en un solo informe.
4. Toda simulación se rotula como «simulación retrospectiva declarada» y se presenta como rango.
5. **Propaga cada corrección a todos los documentos, datos, gráficos y hojas afectados:** PDF o Word, Excel de cada trabajo, Formato 04, PPTX, README.
6. Trabaja en tu rama, con `pull --rebase` antes de `push`, y coordina en el issue #1.

## Orden de ejecución

| Paso | Tarea (ID del plan 10) | Instrucción concreta | Fórmula o regla | Prueba |
|---|---|---|---|---|
| 1 | T05, T06 | Añadir en Medir (03 y M2 de 04): «73 notas; 69 con renglones; 4 sin detalle (NP-025111, -127, -137, -140)». Convertir `Datos!C6:C267` de Lean y Seis Sigma a fecha. | — | `ISNUMBER(C6)` = VERDADERO |
| 2 | T07 | CTQ oficial. Si el equipo no decidió, usar D = 34 = 30 vacíos + 4 diferencias (se excluye NP-025138-01 por el artefacto «millar»). Añadir la tabla de sensibilidad. | DPMO = D/(U·3)·10⁶; σ = NORM.S.INV(1−DPMO/10⁶)+1,5. Filas: (30, 262) → 38 167,94 / 3,2724; (34, 262) → 43 257,0 / 3,2141; (35, 262) → 44 529,26 / 3,2004; (27, 244) → 36 885,25 / 3,2880 | Mismo sigma en Seis Sigma, M2, lámina 5 e informe |
| 3 | T08 | En A2 (04), lámina 7 y capítulo 3: «PEDIDO y las incidencias numéricas son condiciones que la clasificación del lote asocia **por construcción** a REVISAR (25 de 38). La causa candidata es la ausencia de reglas de captura y clasificación; su verificación requiere observar el registro real.» Eliminar «RESPALDADA» como veredicto de causa. Usar: «Condición documental confirmada / Causa por verificar». | — | `grep -i "confirmada\|respaldada"` solo en contextos de condición documental |
| 4 | T09 | Simulación como rango en I2 y lámina 9: eficacia 100/75/50/25 % → 4,96/7,35/9,73/12,12 %. | REVISAR_después = 38 − 25·e; % = /262 | Tabla visible |
| 5 | T10 | En C2, lámina 11 y el costo-beneficio de Codex: tres escenarios. | Beneficio = (R·(1−13/38)·10/60·7,5)·12 − 120. R = 38 → 255; R = 2,86 → −91,80; equilibrio R = 12,16 | Escenario negativo visible |
| 6 | T14, T15, T16 | Añadir: IC Wilson 10,75–19,28 % y efecto de diseño 1,69; tabla de vacíos por estado; tabla de 6 grupos de variantes de producto. | Script: `auditoria_integral/14_EVIDENCIAS_AUDITORIA/recalculo_independiente.py` (secciones B, H, J) | Valores idénticos al JSON |
| 7 | T13, T18 | Lean: retitular la 5S como «ejercicio del taller U3-S1/2 (espacio digital del equipo)». Dibujar el VSM actual (WIP 38 en 22 notas; FPY 78,6 %; t = «por medir») y el VSM futuro (controles en «Registrar» y «Validar»), con la leyenda observado / derivado / hipotético. | — | 2 figuras en el informe Lean |
| 8 | T23, T24 | Formato 04: añadir la hoja Datos (copia de 03) y reemplazar M2!B8:B10 y A1!B5:B9 por COUNTIFS. DMAIC 03: Pendientes!H con fórmula IFS de prioridad. | Prioridad: PEDIDO > vacío > diferencia ≠ 0 > observación o DUDOSA > resto | Cambiar un estado en una copia y ver que el Pareto se actualiza |
| 9 | T22, T25 | Unidades explícitas en cada «62 %». Proteger las hojas (celdas amarillas desbloqueadas). La tolerancia queda **pendiente** si no hay decisión. | 61,64 % notas; 61,83 % renglones | grep |
| 10 | T19, T20, T21 | Informe Word con `U3_Producto_Plantilla_Informe_UPeU.docx` (12–18 págs.), con las cifras ya corregidas. Retirar el enlace a ChatGPT del README. Portada, índice, bibliografía APA y figuras (Pareto combinado, Ishikawa, flujo, VSM, árbol CTQ). | — | Sin recuadros [EQUIPO]; páginas 12–18 |
| 11 | T26 | Versionar `plantillas/` (las 4 del curso) y un `REPRODUCIR.md` con los comandos para regenerar Excel, PPTX y figuras desde un clon limpio. No subir archivos marcados PRIVADO. | — | Regenerar en una carpeta limpia |
| 12 | T28 | Ejecutar `recalculo_independiente.py`, `auditoria_formulas.py` y `generar_hallazgos.py`, y completar `15_CHECKLIST_VALIDACION_FINAL.md`. | — | Checklist en verde |

## Estructura final esperada

```
01_Lean/ 02_Seis_Sigma/ 03_DMAIC/          (corregidos, independientes)
04_Producto_Final/
  U3_Formato_DMAIC_HIDROCOM.xlsx            (con hoja Datos y fórmulas vivas)
  U3_Presentacion_HIDROCOM.pptx
  U3_Informe_HIDROCOM.docx                  (plantilla oficial)
  Costo_Beneficio_HIDROCOM.xlsx             (Codex, con sensibilidad)
  DECISIONES.md                             (aprobado por el equipo)
  scripts/  plantillas/  REPRODUCIR.md
auditoria_integral/                         (esta auditoría + checklist completado)
```

## Condiciones para dar por terminado

- Todos los ítems E1 a E4 del checklist 15 están en ✔.
- Los ítems R1 y R2 están en ✔ o en «pendiente declarado» en los tres informes.
- No hay contradicciones de cifras entre documentos (el grep de las cifras clave da un único valor).
- Comentario en el issue #1 con el commit final.
