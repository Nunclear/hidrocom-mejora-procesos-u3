# 12 · Datos pendientes e instrumentos de recolección

No se inventa ningún dato. Para cada pendiente se indica quién lo da, el instrumento y cómo se usa.

| # | Dato | A quién pedirlo | Instrumento | Uso | Hallazgo |
|---|---|---|---|---|---|
| 1 | Origen de las 73 notas y explicación de las fechas anteriores al 09/03/2026 | Dueño / gerencia | Declaración escrita de 1 párrafo (modelo abajo) | Validez del objeto de estudio | AUD-001 |
| 2 | Decisión sobre la población (lote de 73 frente a versión ampliada) y permiso de uso | Equipo + dueño | Acta en DECISIONES.md | Definir U | AUD-018 |
| 3 | Copia del paquete usada para las evidencias de hash y categoría | Integrante que redactó `main` | Ruta + SHA-256 del Excel y de Productos.csv | Reproducir AUD-012 | AUD-012 |
| 4 | Necesidades del usuario del reporte (VOC) | Quien usa el reporte (gerencia o compras) | Guion de entrevista de 15 min (abajo) | Árbol CTQ validado | AUD-013 |
| 5 | Tiempos del registro y la revisión | Persona que registra | Hoja de cronometraje (abajo) | VSM, PCE, beneficio | AUD-010, -005 |
| 6 | Volumen mensual de notas y renglones | Administración | Conteo de un mes completo | Beneficio, meta | AUD-005 |
| 7 | Costo hora del rol que revisa | Administración | Planilla o remuneración documentada | Beneficio | AUD-005 |
| 8 | Originales de NP-025068, NP-025084, NP-025126 y de una muestra de 40 renglones | Custodio documental | Fotos autorizadas | Conciliación y MSA | AUD-008, -023 |
| 9 | Roles, meta, plazo y puntajes | Equipo | Reunión + DECISIONES.md | Charter y matriz | AUD-006 |
| 10 | Tolerancia monetaria y regla para PEDIDO, kg y millar | Dueño del proceso | Acta de criterios | CTQ y Poka-Yoke | AUD-002, -024 |

## 1. Modelo de declaración de origen

> «Yo, ____ (cargo) de GRUPO HIDROCOM KALLPA E.I.R.L., declaro que las notas de pedido NP-025059 a NP-025144 corresponden a ____ (operación de la empresa / negocio anterior / otro: ____) y que la fecha de inicio de actividades del 09/03/2026 se refiere a ____. Autorizo su uso académico. Fecha y firma.»

## 4. Guion de VOC (15 minutos)

1. ¿Para qué decisiones usa el reporte de ventas o pedidos? (compras, reposición, cobranza…)
2. ¿Qué dato de una nota necesita sí o sí? Ordénelos: producto, cantidad, precio, importe, fecha, cliente, estado.
3. ¿Qué pasa cuando falta un dato o no cuadra? ¿Cuánto tarda en resolverlo?
4. ¿Una nota «PEDIDO» (aún no vendida) debe aparecer en el reporte? ¿Dónde?
5. ¿Qué diferencia de importe es tolerable? (S/ 0,10; S/ 1; ninguna)
6. ¿Cada cuánto necesita el reporte actualizado?

Salida: tabla «necesidad → requisito → CTQ medible → límite», firmada por el entrevistado.

## 5. Hoja de cronometraje (registro de notas)

| Campo | Descripción |
|---|---|
| ID nota | NP-xxxxxx |
| N.º renglones | conteo |
| Inicio de captura (hh:mm:ss) | al tomar la nota |
| Fin de captura | al guardar el último renglón |
| ¿Faltó algún dato? (S/N) y cuál | |
| Inicio y fin de la revisión | si pasó a revisión |
| Espera entre captura y revisión (min) | |
| ¿Retrabajo? (consulta al original) | S/N, minutos |
| Observador | iniciales |

**Muestra mínima:** 30 notas consecutivas, o todas las de 2 semanas si son menos, con el mismo observador.

**Salidas:**
- tiempo de ciclo por renglón (media e IQR);
- espera;
- % de retrabajo;
- PCE = tiempo de valor agregado / lead time;
- un gráfico I-MR del tiempo por nota **en orden real de registro**.

## 8. Protocolo de MSA por atributos

1. Seleccionar 40 renglones al azar estratificado (20 DISPONIBLE, 15 REVISAR, 5 EXCLUIR).
2. Dos revisores clasifican cada renglón de forma ciega con el original y la regla escrita.
3. Calcular el kappa de Cohen.
   - Aceptable: ≥ 0,70.
   - Si es menor, reescribir la regla y repetir.

## Protocolo de piloto (T27)

- **Lote:** notas nuevas de 4 semanas, registradas con la plantilla validada.
- **Indicador:** % REVISAR por lote **y por nota**, con IC.
- **Comparación:** contra la línea base reclasificada con la misma regla.
- **Registro:** tiempos (hoja 5) y motivos de REVISAR (lista cerrada).
- **Criterio de éxito:** se acuerda **antes** de empezar (p. ej. ≤ 5 % con el límite superior del IC < 10 %).
