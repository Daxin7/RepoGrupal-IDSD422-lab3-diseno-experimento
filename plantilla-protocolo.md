# Plantilla de protocolo — Experimento de ubicación de producto

**Equipo:** ___ · **Integrantes:** ___ · **Fecha:** 27/10/2026

Completa cada sección. Usa commits por sección; la historia del repositorio se revisa.

## 1. Pregunta e hipótesis

El producto en el pasillo principal vende más en promedio que en su ubicación habitual en ventas semanales duratne 4 semanas?

## 2. Unidad experimental

*¿Quién recibe el tratamiento? ¿Cuántas unidades se incluyen?*
**Semana-Tienda** (el numero de tiendas que van a estar aplicandose en el experimento en una cantidad de tiempo) (**# de tiendas x # de semanas**)

- **Unidad:**
  - 10 tiendas x 4 Semanas = 40 unidades 
- **Número de unidades y justificación:**
  - voy a experimentar en 10 tiendas y en cada tienda voy a observar 4 semanas.


## 3. Factor, niveles y tratamiento

- **Factor** (variable manipulada): Ubicacion del producto principal
- **Niveles** (valores del factor): pasillo y la ubicación habitual.
- **Tratamiento** (combinación asignada): pasillo durante una semana y ubicación habitual durante otra (grupo de control)

## 4. Grupo de control

*¿Cuál es la referencia sin tratamiento y qué rol cumple?*

Sera la misma tienda pero con el producto expuesto en la ubicación habitual.

## 5. Aleatorización

*¿Cómo se asignan las unidades a los grupos? ¿Por qué es necesaria?*

Sorteo de 20 tiendas a cada grupo en paralelo (todas van a estar experimentandose al mismo tiempo)

TODO: HACER EL CODIGO DE ESTO
- **Línea de código de la asignación (Python o R):** escribe el comando que asigna al azar tus N unidades a los dos grupos (tratamiento y control) y ejecútalo con semilla. Incluye el resultado de una corrida y explica por qué el sorteo reparte los factores desconocidos entre los grupos.

## 6. Respuesta y medición

- **Variable respuesta:**
  -  Ventas semanales en USD
- **Período de medición:**
  -  4 semanas
- **Quién registra y cómo (¿ciego?(persona que administra este proceso)):**
  -  Mediante el POS(PUNTO DE VENTA), ciego (porque el vendedor no sabría si el producto esta en el pasillo principal o habitual)

## 7. Factores a controlar (mínimo 4)

| Factor a controlar | Cómo se controla o registra |
|---|---|
| 1. |Clima |
| 2. |Evento Local |
| 3. |Surtido / Stock |
| 4. |Cambios en el Personal |

## 8. Limitaciones del diseño

*¿Qué podría invalidar el experimento si no se controla? ¿Qué no se podrá concluir?*

- **La perdida de potencia por promociones:**
  - limitacion dado que si existe un producto competidor esta en promocion es mas probable que lo compren y no el producto que estamos experimentando
- **Canibalización de las tiendas**:

## 9. Comparación en código (Python/R)

*Escribe `scripts/comparacion_experimento.py` (o `.R`): debe cargar `plantillas/registro_experimento.csv` y calcular el promedio de `ventas_producto` por `ubicacion`. Incluye la salida y responde:*

- ¿Qué grupo muestra mayor venta promedio en la plantilla?
El pasillo principal muestra 1335 USD en venta frente a 1040 USD del pasillo habitual.

- ¿Por qué con 4 filas no se puede concluir nada sobre el efecto de la ubicación?
No se puede concluir porque no hay niguna asignación real aleatoria, los datos son muy pocos(4) no tenemos control de temporada, ni promociones en el grupo pasillo y no hya medida de variabilidad

- Si el experimento se ejecutara con tu protocolo, ¿qué le faltaría a este análisis para ser justo?
