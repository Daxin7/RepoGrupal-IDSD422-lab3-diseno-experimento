# Plantilla de diseño — Encuesta de satisfacción (Hito 1)

**Asignatura:** Estadística y Programación para Ciencia de Datos I (IDSD422)  
**Institución:** Escuela Politécnica Nacional  
**Empresa:** RetailAndina S.A.  
**Equipo:** 3  
**Integrantes:**
- Jhon Solorzano
- Said Bravo
- David Jácome
- Deysi Guachamin

**Entrega:** Hito 1 final, con datos · 19/11/2026  
**Repositorio (fork):** https://github.com/Daxin7/RepoGrupal-IDSD422-lab3-diseno-experimento  
**Enfoque del equipo:** Programa de fidelización: satisfacción y beneficios valorados por clientes habituales adultos de RetailAndina en Quito.  
**Datos:** encuesta aplicada del 5 al 9 de noviembre de 2026 · `plantillas/encuesta_respuestas.csv`

---

## 1. Objetivo de la encuesta

**Objetivo (frase medible):**

Medir, en una muestra de 15 a 30 clientes habituales adultos de RetailAndina en Quito, qué porcentaje está satisfecho con la cadena (4 o 5 en una escala de 1 a 5), qué porcentaje la recomendaría, qué porcentaje está interesado en un programa de fidelización (4 o 5) y cuál es el beneficio que más prefiere, para que la gerencia decida con qué beneficio lanzar el programa.

**Decisión de gerencia que apoya:**

RetailAndina va a lanzar un programa de fidelización y tiene que definir con qué beneficio arrancar (descuentos, puntos, promociones personalizadas o recompensas) y qué tan atractivo resulta el programa para sus clientes actuales. La encuesta también señala qué aspecto de la tienda conviene corregir, porque un programa de fidelización rinde menos si la experiencia de compra tiene fallas básicas.

**Objetivos específicos:**

1. Describir cómo se reparten los niveles de satisfacción con RetailAndina en la escala de 1 a 5.
2. Calcular la proporción de clientes que recomendaría RetailAndina a otra persona.
3. Medir el interés en participar en un programa de fidelización de RetailAndina.
4. Identificar el beneficio preferido entre descuentos directos, acumulación de puntos, promociones personalizadas y productos o recompensas gratuitas.
5. Identificar el aspecto que los clientes consideran más urgente de mejorar.
6. Revisar, de forma descriptiva, si la satisfacción y el interés en el programa cambian según la frecuencia de compra.

**Indicadores:**

| Indicador | Cómo se calcula | Pregunta |
|---|---|---|
| Satisfacción favorable | % de respuestas 4 o 5 en satisfacción | P3 |
| Satisfacción promedio | promedio de la escala 1–5, solo como resumen descriptivo | P3 |
| Recomendación | % de respuestas "Sí" | P4 |
| Interés en el programa | % de respuestas 4 o 5 en interés | P5 |
| Beneficio preferido | opción más elegida y su porcentaje | P6 |
| Prioridad de mejora | aspecto más elegido y su porcentaje | P7 |

Todos los indicadores se calculan solo con las respuestas reales válidas (`origen = real` y las cuatro preguntas filtro en "Sí"). Como la muestra es pequeña y por conveniencia, los resultados sirven para orientar la decisión, no para afirmar cómo piensan todos los clientes de RetailAndina en Quito.

## 2. Población objetivo

**Población:**

Personas de 18 años o más que viven en el Distrito Metropolitano de Quito, que compraron en un supermercado durante los últimos 30 días y que hacen sus compras habituales en RetailAndina.

**Límites y justificación:**

| Límite | Quién entra | Por qué |
|---|---|---|
| Región | Residentes del Distrito Metropolitano de Quito | Es la ciudad donde estudia el equipo y donde está su red de contactos, así que la recolección es alcanzable; además evita mezclar ciudades con precios, competencia y tiendas distintas. |
| Edad | 18 años o más | Son personas que deciden y pagan sus compras, y que pueden dar su consentimiento sin intervención de un representante. |
| Compra reciente | Al menos una compra en un supermercado en los últimos 30 días | Asegura que la persona califique su experiencia con un recuerdo fresco y no con una impresión antigua. |
| Cliente de RetailAndina | Hace sus compras habituales en RetailAndina | Las preguntas son sobre RetailAndina y su programa; quien no compra ahí no puede calificar la tienda. Este límite se agregó al pasar del borrador al formulario final. |
| Participación | Voluntaria, con consentimiento informado | Solo se usan las respuestas de quienes aceptan el tratamiento de sus datos. |

**Cómo se verifica:** el formulario abre con el consentimiento y cuatro preguntas filtro (sección 4). Si la persona no compra habitualmente en RetailAndina, el formulario termina ahí. Los otros tres filtros no cortaban el formulario, así que se aplican al limpiar los datos: solo cuentan como válidas las respuestas con los cuatro filtros en "Sí".

**Criterios de inclusión:**

- Tener 18 años o más.
- Vivir en Quito.
- Haber comprado en un supermercado en los últimos 30 días.
- Hacer las compras habituales en RetailAndina.
- Aceptar participar y responder una sola vez.

**Criterios de exclusión:**

- No cumplir alguno de los cuatro filtros.
- No dar el consentimiento.
- Registros duplicados.
- Respuestas en las que no se puede confirmar la elegibilidad, por ejemplo, una persona que responde que no tiene 18 años pero luego anota una edad mayor.

**Unidad de análisis:**

Cada cliente habitual adulto de RetailAndina en Quito que completa la encuesta.

**Marco de selección:**

El equipo no tiene acceso a una lista de todos los clientes de RetailAndina con datos de contacto. En la práctica, el marco fue la red de contactos de los cuatro integrantes (familiares, amigos, compañeros y sus referidos) que cumplían los filtros. Esa red es mucho más pequeña y parecida entre sí que la población, y esa diferencia se tiene en cuenta al interpretar los resultados (sección 5).

## 3. Método de muestreo

**Método aplicado en campo:**

Muestreo no probabilístico por conveniencia con referidos y cuota por integrante: cada uno de los cuatro integrantes invitó a personas de su red que cumplían los filtros, con una meta de 6 respuestas por persona.

**Por qué este método:**

- No hay una lista de clientes de RetailAndina con datos de contacto a la que el equipo pueda acceder, así que un sorteo sobre toda la población no era posible.
- La recolección se hizo en pocos días (semana del feriado de noviembre) y sin presupuesto; la red de contactos era la vía realista para conseguir entre 15 y 30 respuestas.
- La cuota por integrante evita que un solo círculo de contactos domine la muestra.
- El costo de esta elección es claro: las personas no tienen una probabilidad conocida de ser elegidas, así que los resultados no se generalizan a todos los clientes de Quito. Se usan como una primera lectura para la gerencia.

**Tamaño:**

La meta fue de 24 respuestas reales (6 por integrante), dentro del rango de 15 a 30 que pide la guía. Se recibieron 23 formularios y 16 cumplieron todos los filtros:

| Integrante | Formularios recibidos | Respuestas válidas |
|---|---:|---:|
| Deysi Guachamin | 6 | 5 |
| David Jácome | 6 | 5 |
| Jhon Solorzano | 6 | 3 |
| Said Bravo | 5 | 3 |
| **Total** | **23** | **16** |

**Forma de selección en campo:**

1. Cada integrante armó una lista de posibles participantes de su red: familiares, amigos, compañeros y personas referidas por ellos.
2. La idea era cubrir distintas edades y frecuencias de compra; en la práctica, la red terminó concentrada en personas jóvenes (sección 5).
3. A cada persona se le compartió el formulario, con una explicación del propósito académico y del carácter voluntario de la encuesta.
4. El formulario verificó los filtros de entrada y registró qué integrante hizo el contacto.
5. Cada persona respondió una sola vez; después se apartaron los registros que no cumplían los filtros.

**Equivalente en código (Python):**

Como no existía una lista de clientes con contactos, el sorteo no se pudo aplicar en campo. La línea de código muestra cómo se elegiría a las personas si RetailAndina entregara su base de clientes, y sirve de referencia para ver qué tan lejos quedó la muestra por conveniencia. Para probarla se usa `data/clientes_400.csv`, la base de clientes de RetailAndina del laboratorio de muestreo (no tiene datos de contacto): se filtra la población (Quito, 18 años o más) y se sortean 24 personas por grupo de edad, respetando el peso que tiene cada grupo en la base (muestreo estratificado proporcional). Se estratifica por edad porque es la variable en la que la muestra por conveniencia quedó más desbalanceada.

```python
import pandas as pd

clientes = pd.read_csv("data/clientes_400.csv")
marco = clientes[(clientes["ciudad"] == "Quito") & (clientes["edad"] >= 18)].copy()
marco["grupo_edad"] = pd.cut(marco["edad"], [17, 29, 44, 65], labels=["18-29", "30-44", "45-65"])

muestra = marco.groupby("grupo_edad", observed=True).sample(frac=24 / len(marco), random_state=2026)
```

El script completo, que además reparte la lista en 6 contactos por integrante, está en `scripts/muestreo_encuesta.py` y se ejecuta desde la raíz con `python scripts/muestreo_encuesta.py`.

**Corrida (semilla 2026):**

```text
Marco (Quito, 18+): 200 clientes · muestra: 24 · semilla: 2026
  E1: C065, C009, C066, C030, C175, C115
  E2: C097, C053, C108, C033, C110, C099
  E3: C146, C116, C047, C190, C165, C130
  E4: C067, C016, C076, C189, C056, C074

Composición por grupo de edad:
            marco_n  muestra_n  marco_%  muestra_%
grupo_edad
18-29            49          6     24.5       25.0
30-44           100         12     50.0       50.0
45-65            51          6     25.5       25.0

Edad en la muestra: mínimo 18, máximo 53, media 36.9
```

**Lectura de la corrida:**

El sorteo respeta el peso de cada grupo de edad: 25 % de 18 a 29 años, 50 % de 30 a 44 y 25 % de 45 a 65, prácticamente igual que la base. La muestra real por conveniencia, en cambio, quedó entera en el grupo de 18 a 29 años. Con la misma semilla la lista sale siempre igual; con otra semilla cambian las personas, pero no la proporción por grupo. Como referencia, un sorteo simple con la misma semilla (`marco.sample(n=24, random_state=2026)`) dejó fuera a todo el grupo de 18 a 29 años: estratificar evita que el azar deje un grupo sin representación.

## 4. Cuestionario (5–10 preguntas)

Esta sección reproduce el cuestionario tal como se aplicó en el formulario, con las mismas preguntas y opciones que llegan al CSV.

**Inicio del formulario:**

- **Consentimiento:** un texto basado en la Ley Orgánica de Protección de Datos Personales (sección 6), con la opción "Sí (Autorizo el tratamiento de datos personales y acepto participar voluntariamente)".
- **Integrante responsable:** "Seleccione el evaluador responsable del registro". Identifica al integrante que hizo el contacto; no es una pregunta sobre el participante y en el CSV se guarda codificado (E1 a E4).

**Preguntas filtro (Sí / No):**

| Filtro | Columna en el CSV |
|---|---|
| ¿Tiene 18 años o más? | `mayor_18` |
| ¿Reside en Quito? | `reside_quito` |
| ¿Ha realizado al menos una compra en un supermercado durante los últimos 30 días? | `compra_30_dias` |
| ¿Realiza sus compras habituales en RetailAndina? | `cliente_retailandina` |

Los filtros comprueban que la persona pertenece a la población (sección 2) y no cuentan entre las ocho preguntas del cuestionario. Si la persona responde "No" a la última, el formulario termina.

### Cuestionario principal

| # | Pregunta (texto aplicado) | Opciones | Tipo de variable | Dtype esperado | Columna |
|---|---|---|---|---|---|
| P1 | ¿Cuál es su edad en años cumplidos? | Número entero, 18 o más | Numérica discreta | `int64` | `edad` |
| P2 | ¿Con qué frecuencia realiza compras en RetailAndina? | Varias veces por semana; Semanal; Quincenal; Mensual; Menos de una vez al mes | Categórica ordinal | `object` | `frecuencia_visita` |
| P3 | En general, ¿qué tan satisfecho está con RetailAndina? | 1 = Muy insatisfecho; 2 = Insatisfecho; 3 = Ni satisfecho ni insatisfecho; 4 = Satisfecho; 5 = Muy satisfecho | Categórica ordinal | `int64` | `satisfaccion_general` |
| P4 | ¿Recomendaría RetailAndina a otra persona? | Sí; No | Categórica binaria | `object` | `recomendaria` |
| P5 | ¿Qué tanto le interesaría participar en un programa de fidelización de RetailAndina? | 1 = Nada interesado; 2 = Poco interesado; 3 = Ni interesado ni desinteresado; 4 = Interesado; 5 = Muy interesado | Categórica ordinal | `int64` | `interes_programa` |
| P6 | ¿Cuál de estos beneficios preferiría recibir de RetailAndina mediante un programa de fidelización? | Descuentos directos; Acumulación de puntos; Promociones personalizadas; Productos o recompensas gratuitas; Otro; Ninguno | Categórica nominal | `object` | `beneficio_preferido` |
| P7 | ¿Cuál es el principal aspecto que debería mejorar RetailAndina? | Precios; Atención al cliente; Rapidez en caja; Variedad de productos; Disponibilidad de productos; Limpieza y comodidad; Ninguno; Otro | Categórica nominal | `object` | `aspecto_mejora` |
| P8 | ¿Desea agregar algún comentario o sugerencia sobre su experiencia de compra en RetailAndina? | Respuesta abierta y opcional | Texto libre (cualitativa) | `object` | `comentario` |

**Por qué las preguntas cumplen las reglas:**

- **Neutras:** ninguna empuja hacia una respuesta. Se pregunta "¿qué tan satisfecho está?" y no "¿qué tan buena le parece la tienda?", y las escalas tienen un punto medio y extremos equilibrados.
- **Específicas:** cada pregunta nombra a RetailAndina y un solo tema.
- **Una idea por pregunta:** ninguna mezcla dos temas; por ejemplo, precio y atención son opciones distintas dentro de P7, no una pregunta doble.
- **Opciones completas y sin cruces:** P6 y P7 incluyen "Otro" y "Ninguno" para que nadie se quede sin una opción que lo represente.

**Notas sobre el dtype:**

- El dtype es una pista, no la clasificación. `satisfaccion_general` e `interes_programa` llegan como números, pero son ordinales: un 4 no vale el doble que un 2. Su promedio se usa solo como resumen descriptivo.
- En el CSV completo, `edad`, `satisfaccion_general` e `interes_programa` se cargan como `float64` y no como `int64`, porque las dos personas que no compran en RetailAndina dejaron esas celdas vacías y pandas representa el vacío con `NaN`. El entero se recupera al leer con `dtype={"edad": "Int64"}` (lo mismo para las dos escalas).
- Las columnas de texto aparecen como `object` en pandas 2 (la versión de Colab) y como `str` en pandas 3; en ambos casos se trata de texto.

**Cambios respecto del borrador (20/10):**

| Borrador | Formulario aplicado | Motivo |
|---|---|---|
| Preguntas sobre "el supermercado donde compra habitualmente" | Preguntas sobre RetailAndina | El objetivo es evaluar a RetailAndina y su programa |
| Tres preguntas filtro | Cuatro, con "¿Realiza sus compras habituales en RetailAndina?" | Asegurar que quien responde pueda calificar a RetailAndina |
| Opción "Si" | Opción "Sí" | Es la grafía del formulario; el CSV usa una sola |
| Sin registro del integrante | Campo del integrante responsable | Controlar la cuota de 6 por integrante |

**Reglas de registro en el CSV:**

- Una fila por persona y una columna por pregunta, con las opciones escritas exactamente como en el formulario.
- Las escalas de P3 y P5 se guardan como el número (1 a 5), sin la etiqueta.
- Sin nombres, cédulas, teléfonos, correos ni direcciones.
- Celda vacía cuando la persona no respondió o el formulario terminó en el filtro.
- Columna `origen` con `real` o `simulada` en todas las filas.

**Ajuste detectado al aplicar la encuesta:**

Tres personas respondieron "No" a "¿Tiene 18 años o más?" y después anotaron 18, 19 y 27 años. Lo más probable es un error al marcar, pero no se puede confirmar, así que esas respuestas se excluyen del análisis. En una próxima aplicación conviene que cada filtro corte el formulario y que la pregunta de edad solo acepte números desde 18.

## 5. Análisis de sesgos

La evidencia de esta sección sale solo de las respuestas reales (filtrando `origen = real`); las filas simuladas no se usan para hablar de sesgos.

| Sesgo potencial | Qué se observó en los datos reales | Mitigación viable |
|---|---|---|
| **1. Sesgo de selección (cobertura):** al reclutar en la red de los integrantes, la muestra se parece a ellos y no a la población de clientes. | Las 16 respuestas válidas tienen entre 19 y 29 años (media de 21,4). En la base de clientes del curso, solo el 24,5 % de los adultos de Quito está en ese rango. No hay nadie de 30 años o más, un grupo con mucho peso entre quienes hacen las compras del hogar. | Fijar cuotas por grupo de edad (por ejemplo, 6 personas de 18–29, 12 de 30–44 y 6 de 45 o más, como en la corrida de la sección 3); pedir a cada integrante al menos dos contactos entre familiares mayores o vecinos; y, si la empresa entrega su base de clientes, reemplazar la conveniencia por el sorteo estratificado de la sección 3. |
| **2. Sesgo de respuesta por cortesía:** quien conoce al encuestador tiende a contestar de forma más amable de lo que realmente piensa. | Las 16 personas respondieron que recomendarían RetailAndina, incluso las 6 que calificaron su satisfacción con un 3 (ni satisfecho ni insatisfecho). Un 100 % de recomendación junto a una satisfacción apenas favorable (62,5 % con 4 o 5) es una señal de respuestas complacientes. | Que la persona llene el formulario sola y sin que el integrante vea sus respuestas; recordar al inicio que no hay respuestas correctas y que nadie sabrá qué contestó; y cambiar el "Sí / No" de P4 por una escala de 0 a 10, que deja espacio para una recomendación tibia. |

**Otros riesgos a vigilar:**

- **No respuesta:** de las personas contactadas, **[COMPLETAR: n]** no contestaron el formulario (sección 7). Si quienes no respondieron son, por ejemplo, los contactos de más edad o los menos satisfechos, la muestra queda todavía más inclinada hacia lo positivo. Se mitiga con un recordatorio a los dos o tres días y manteniendo el formulario corto.
- **Error en los filtros:** tres personas se contradijeron en la pregunta de edad (sección 4). Sus respuestas se excluyeron y el formulario debe corregirse para la próxima aplicación.

**Qué se puede concluir y qué no:**

Con 16 respuestas de personas jóvenes de la red del equipo, los resultados describen a ese grupo y no a todos los clientes de RetailAndina en Quito. Por eso no se calculan márgenes de error ni intervalos de confianza: suponen un muestreo aleatorio que aquí no existió.

## 6. Confidencialidad (RA3)

**Datos personales que se piden y por qué:**

La encuesta pide solo lo necesario para cumplir el objetivo:

- **Edad:** para confirmar que la persona es mayor de edad y describir el perfil de la muestra.
- **Filtros de residencia, compra reciente y cliente habitual:** para confirmar que la persona pertenece a la población.
- **Opiniones de compra:** frecuencia, satisfacción, recomendación, interés, beneficio preferido y aspecto de mejora, que son el contenido de la encuesta.

No se pidieron nombres, cédulas, teléfonos, correos, direcciones ni datos económicos, y el formulario no recolectó correos (el export no trae esa columna).

**Consentimiento informado:**

El formulario abre con un texto basado en la Ley Orgánica de Protección de Datos Personales (LOPDP). Explica que el tratamiento se apoya en la voluntad expresa del participante (art. 7, num. 1) y en un consentimiento libre, específico, informado e inequívoco (art. 8); que se respetan los principios de transparencia, finalidad, minimización de datos y confidencialidad (art. 10) y el derecho a una información clara (art. 12); que las respuestas se usan solo con fines estadísticos y académicos y se anonimizan (art. 4); y que la persona puede revocar su autorización y ejercer sus derechos de acceso, rectificación, eliminación, oposición, portabilidad y suspensión (arts. 13 a 20). Las 23 personas que respondieron aceptaron.

**Plan de anonimización (aplicado):**

| Dato del export crudo | Qué se hizo antes de compartir | Por qué |
|---|---|---|
| Marca temporal con fecha y hora | Se conserva solo la fecha, en formato AAAA-MM-DD | La hora exacta, cruzada con quién hizo el contacto, puede delatar a una persona |
| Nombre del integrante que registró | Se reemplaza por un código (E1 a E4) | El CSV queda sin nombres; el código basta para controlar la cuota |
| Texto completo del consentimiento | Se reduce a "Sí" | Es la misma información, sin texto repetido |
| Cada persona | Identificador R001 a R023 según el orden de llegada | El código no se puede ligar a una identidad |
| Escalas con etiqueta ("4 = Satisfecho") | Solo el número | Es una codificación; no cambia el contenido |
| Comentarios abiertos | Revisión manual antes de publicar | Solo hubo uno ("sin comentarios") y no contiene datos personales |

**Cómo se aplica:**

`scripts/anonimizar_respuestas.py` lee el export crudo desde una ruta fuera del repositorio y escribe `plantillas/encuesta_respuestas.csv`. Así el proceso queda documentado y se puede repetir sin editar los datos a mano.

**Almacenamiento y publicación:**

- El export crudo se conserva fuera del repositorio, con acceso solo para los integrantes. El `.gitignore` bloquea los nombres típicos de ese archivo (`datos_crudos/`, `*crudo*.csv`, `Encuesta de satisfacción*.csv`) para evitar subirlo por error.
- En GitHub solo se publica el CSV anonimizado.
- Las filas simuladas llevan `origen = simulada`, para que nadie las confunda con personas reales.

**Riesgo que queda:**

Con 23 personas de una red conocida, la combinación de edad, fecha e integrante podría permitir que alguien cercano adivine quién respondió. Por eso los resultados se presentan siempre agregados y no se publican cruces de respuestas por integrante y fecha.

## 7. Datos de la encuesta aplicada y verificación (Python)

### 7.1. Recolección

- **Fechas:** del 5 al 9 de noviembre de 2026 (3 respuestas el 5, 4 el 8 y 16 el 9).
- **Instrumento:** formulario en línea (Google Forms) con el cuestionario de la sección 4, compartido por cada integrante con su red de contactos.
- **Archivo:** `plantillas/encuesta_respuestas.csv`, anonimizado según la sección 6.

### 7.2. Participantes y no respuesta (solo parte real)

| Etapa | Personas |
|---|---:|
| Personas contactadas | **[COMPLETAR: n]** |
| No contestaron el formulario (no respuesta) | **[COMPLETAR: n]** |
| Respondieron el formulario | 23 |
| Terminaron en el filtro "compra habitual en RetailAndina" | 2 |
| Excluidas por contradicción en el filtro de edad | 3 |
| Excluidas por no residir en Quito | 1 |
| Excluidas por no haber comprado en los últimos 30 días | 1 |
| **Respuestas reales válidas** | **16** |

**Tasa de respuesta** = 23 ÷ personas contactadas × 100 = **[COMPLETAR] %**.

Las 23 filas reales están en el CSV, incluidas las que no pasaron los filtros, para que la exclusión quede a la vista y se pueda repetir con código.

### 7.3. Estructura del CSV

El archivo tiene 80 filas (23 reales y 57 simuladas) y 17 columnas: una por cada pregunta del formulario (consentimiento, cuatro filtros y ocho preguntas) más cuatro de registro.

| Columna | Contenido |
|---|---|
| `respuesta_id` | Código de la fila: R001 a R023 (reales) y R024 a R080 (simuladas) |
| `fecha` | Fecha de la respuesta (AAAA-MM-DD); vacía en las simuladas |
| `encuestador` | Integrante que hizo el contacto, codificado E1 a E4; vacío en las simuladas |
| `consentimiento` | "Sí" |
| `mayor_18`, `reside_quito`, `compra_30_dias`, `cliente_retailandina` | Preguntas filtro (Sí / No) |
| `edad` a `comentario` | Preguntas P1 a P8 (sección 4) |
| `origen` | `real` o `simulada` |

Para trabajar solo con las respuestas reales válidas:

```python
import pandas as pd

df = pd.read_csv("plantillas/encuesta_respuestas.csv")
filtros = ["mayor_18", "reside_quito", "compra_30_dias", "cliente_retailandina"]
validas = df[(df["origen"] == "real") & df[filtros].eq("Sí").all(axis=1)]
```

El CSV se reconstruye desde la raíz con `python scripts/anonimizar_respuestas.py "<ruta al export crudo>"` y luego `python scripts/simular_respuestas.py`.

### 7.4. Filas simuladas (declaración)

Para tener más volumen en los análisis del capítulo 4 y del laboratorio 7, el CSV se completó hasta 80 filas con 57 respuestas simuladas, generadas con `scripts/simular_respuestas.py` (semilla 2026):

- Cada pregunta cerrada se sortea con las frecuencias de las 16 respuestas reales válidas, sumando un "voto" extra a cada opción para que también aparezcan opciones que nadie eligió, como "Varias veces por semana" u "Otro".
- La edad sale de una distribución normal con la media (21,4) y la desviación (2,4) de las edades reales, redondeada y con mínimo 18. Por eso las simuladas heredan el perfil joven de la muestra real.
- Cada pregunta se sortea por separado, así que las simuladas no reproducen la relación entre preguntas (por ejemplo, entre satisfacción y recomendación).
- Los filtros y el consentimiento van en "Sí"; fecha, integrante y comentario quedan vacíos porque no hubo una aplicación real.
- Todas llevan `origen = simulada`. No se usan para conclusiones ni para el análisis de sesgos.

### 7.5. Resultados con las respuestas reales válidas (n = 16)

| Indicador | Resultado |
|---|---|
| Satisfacción favorable (4 o 5) | 62,5 % (10 de 16) |
| Satisfacción promedio (escala 1–5) | 3,81 |
| Recomendaría RetailAndina | 100 % (16 de 16) |
| Interés en el programa (4 o 5) | 50,0 % (8 de 16) |
| Beneficio preferido | Descuentos directos: 37,5 % (6 de 16) |
| Aspecto a mejorar más elegido | Rapidez en caja: 31,3 % (5 de 16) |

Por frecuencia de compra (objetivo específico 6), la satisfacción no muestra un patrón claro, pero el interés sí: los 4 clientes que compran cada semana se declaran interesados en el programa, frente a 1 de 4 entre quienes compran una vez al mes. Con grupos tan pequeños es solo una pista, aunque tiene sentido: un programa de fidelización atrae más a quien compra seguido.

**Lectura para la gerencia:** los descuentos directos son el beneficio más pedido y la rapidez en caja es la queja principal. El interés en el programa está dividido (la mitad se declara interesada y una de cada cuatro personas, poco interesada), así que el lanzamiento necesita un beneficio concreto y fácil de entender. La recomendación del 100 % se toma con cautela por el posible sesgo de cortesía (sección 5). Todo esto describe a 16 clientes jóvenes de la red del equipo, no a toda la clientela de Quito.

### 7.6. Verificación con Python (opcional en esta entrega)

`scripts/verificacion_encuesta.py` (con sus TODOs completos) carga el CSV y reporta dtypes, faltantes y distribuciones. Resumen de la corrida sobre las 80 filas:

| Columnas | Dtype al cargar | Faltantes | Explicación |
|---|---|---:|---|
| `respuesta_id`, `consentimiento`, filtros, `origen` | texto | 0 | Completas |
| `fecha`, `encuestador` | texto | 57 | Vacías solo en las simuladas |
| `edad`, `satisfaccion_general`, `interes_programa` | `float64` | 2 | Las 2 personas que terminaron en el filtro de RetailAndina |
| `frecuencia_visita`, `recomendaria`, `beneficio_preferido`, `aspecto_mejora` | texto | 2 | Las mismas 2 personas |
| `comentario` | texto | 79 | Pregunta opcional; solo una persona escribió algo |

Los dtypes coinciden con lo previsto en la sección 4, con la diferencia de los `float64` explicada allí. Los faltantes no son errores de captura: responden al diseño del formulario (corte en el filtro y comentario opcional) y a las filas simuladas.

---

## Conclusiones

1. La encuesta cerró su ciclo: 23 personas respondieron el formulario y 16 cumplieron todos los filtros, dentro del rango de 15 a 30 respuestas reales. Con ellas, la gerencia tiene una primera lectura: descuentos directos como beneficio más pedido y rapidez en caja como principal aspecto a mejorar.
2. Los datos muestran los límites del muestreo por conveniencia: todas las respuestas válidas vienen de personas de 19 a 29 años y la recomendación es unánime incluso con satisfacción neutral. Antes de decidir el lanzamiento conviene repetir la encuesta con cuotas por edad o con el sorteo estratificado de la sección 3, y con un formulario que la persona llene sola.
3. El CSV queda listo para los siguientes análisis: anonimizado, con una columna por pregunta y con las filas simuladas declaradas en `origen`, de modo que cualquier conclusión pueda limitarse a las respuestas reales.
