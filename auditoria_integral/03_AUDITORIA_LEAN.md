# 03 · Auditoría del trabajo Lean

Objeto: `01_Lean/U3_Lean_HIDROCOM.pdf` (7 págs.), `U3_Lean_HIDROCOM.xlsx` (7 hojas, 25 fórmulas) y `Evidencia_5S.csv`.

El trabajo es **honesto y bien delimitado**: separa con disciplina lo observado de lo hipotético. Su debilidad es la contracara: **casi ninguna herramienta Lean llega a aplicarse con datos del proceso**. Se queda en un protocolo.

## Evaluación por herramienta

Escala: ✔ sí · ◐ parcial · ✘ no.

| Herramienta | Conceptualmente correcta | Pertinente | Respaldada por datos | Evidencia de ejecución | Documentada | Acción |
|---|---|---|---|---|---|---|
| 5 principios (valor, cadena, flujo, pull, perfección) | ✔ | ✔ | ◐ (valor sin VOC) | ✘ | ✔ | Ampliar: validar el «valor» con el usuario del reporte |
| Identificación de valor | ◐ | ✔ | ✘ (sin entrevista) | ✘ | ✔ | Requiere la entrevista (12_DATOS_PENDIENTES) |
| VSM actual | ◐ (6 etapas, sin tiempos ni WIP) | ✔ | ✘ | ✘ | ✔ (declara el límite) | **Corregir:** levantar tiempos con el protocolo; dibujar el VSM gráfico con iconografía (AUD-010) |
| VSM futuro | ✘ (no existe) | ✔ | — | — | — | **Ampliar:** VSM futuro con los controles propuestos, marcado como diseño |
| Lead time / CT / VA / NVA / PCE | ✔ (fórmulas correctas en VSM!B16:B20, validadas) | ✔ | ✘ (celdas vacías) | ✘ | ✔ | Recolectar tiempos; no inventarlos |
| 8 desperdicios (DOWNTIME) | ✔ | ✔ | ◐ (defectos e inventario con datos; 6 hipótesis) | ✘ | ✔ | Ampliar: cuantificar «defectos» (35 en 22 renglones) e «inventario» (38 en cola, 22 notas) |
| Muda / Mura / Muri | ✘ (ausente) | ◐ | — | — | — | Opcional: Mura = variación de formato y base de precio; Muri requiere observar |
| 5S | ◐ | ✘ para la empresa (se aplicó a la carpeta académica) | ◐ (CSV 1/5 → 4/5) | ✔ (sobre el repositorio) | ✔ | Reorientar a las carpetas reales de notas e imágenes de la empresa, o declararlo explícitamente como ejercicio del taller U3-S1/2 (AUD-011) |
| Kaizen | ✔ (8 ideas K01–K08) | ✔ | ◐ | ✘ | ✔ | Puntuar impacto y esfuerzo con el equipo; hoy la matriz dice «SIN EVALUAR» |
| Poka-Yoke | ✔ (prevención y detección) | ✔ | ✔ (vacíos y diferencias reales) | ◐ (prototipo en Excel; no impide editar) | ✔ | Probar el prototipo sobre los 262 renglones como prueba retrospectiva declarada |
| Estandarización | ◐ (procedimiento descrito en DMAIC) | ✔ | — | ✘ | ◐ | Redactar la hoja de trabajo estándar de 1 página |
| Gestión visual | ✘ | ✔ | — | ✘ | ✘ | Proponer un tablero de la cola REVISAR por motivo y antigüedad |
| Flujo continuo / Pull | ◐ (pull aplicado a la publicación) | ◐ | ✘ | ✘ | ✔ | Suficiente para el nivel; mantener como diseño |

## Puntos de atención específicos

- **VSM sin tiempos.** Es correcto no inventar tiempos. Falta el **instrumento**: hoja de observación, tamaño de muestra y criterio de inicio y fin. Ver la propuesta en `12_DATOS_PENDIENTES.md`.
- **VSM defendible.** El estado actual se puede dibujar con lo que **sí** se sabe:
  - etapas reconstruidas de los archivos;
  - WIP = 38 renglones REVISAR repartidos en 22 notas;
  - proporción de renglones DISPONIBLE al corte = 206/262 = 78,63 % (no es un rendimiento de primera pasada: el FPY exige registrar el resultado antes de cualquier retrabajo y queda por medir en el piloto);
  - en el lugar de los tiempos, «t = ? (por medir)».

  El VSM futuro marca dónde actúan los controles. Ambos deben rotular cada dato como **observado**, **derivado de los archivos** o **hipotético**.
- **5S.** La ficha del taller U3-S1/2 pedía expresamente aplicar 5S «a un espacio digital del equipo», así que el ejercicio **cumple el taller**. En un informe sobre HIDROCOM, en cambio, se puede leer como una intervención en la empresa. Hay que declararlo en el título de la sección.
- **Desperdicios sin observación directa.** El informe los presenta correctamente como hipótesis. Dos de ellos sí son cuantificables con los datos y no se cuantificaron: defectos e inventario en cola.
- **Prototipos frente a controles implementados.** La distinción está bien hecha («no impide editar»). Se mantiene.
- **Viabilidad de Kaizen.** Sin puntajes ni responsables no se puede evaluar. En `04_Producto_Final` hay puntajes como propuesta que no se trasladaron aquí (AUD-006).

## Dictamen

Es un diagnóstico Lean metodológicamente prudente, con aplicación incompleta: VSM sin tiempos ni estado futuro, 5S fuera del proceso empresarial y Kaizen sin priorizar. Calificación: ver `11_CALIFICACION.md`.
