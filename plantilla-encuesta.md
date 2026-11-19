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
6. Revisar, de forma descriptiva, si la satisfacción y la recomendación cambian según la frecuencia de compra.

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
| Región | Residentes del Distrito Metropolitano de Quito | Es la ciudad donde vive todo el equipo, así que la recolección es alcanzable; además evita mezclar ciudades con precios, competencia y tiendas distintas. |
| Edad | 18 años o más | Son personas que deciden y pagan sus compras, y que pueden dar su consentimiento sin intervención de un representante. |
| Compra reciente | Al menos una compra en un supermercado en los últimos 30 días | Asegura que la persona califique su experiencia con un recuerdo fresco y no con una impresión antigua. |
| Cliente de RetailAndina | Hace sus compras habituales en RetailAndina | Las preguntas son sobre RetailAndina y su programa; quien no compra ahí no puede calificar la tienda. Este límite se agregó al pasar del borrador al formulario final. |
| Participación | Voluntaria, con consentimiento informado | La encuesta solo continúa si la persona acepta el tratamiento de sus datos. |

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
- **Integrante responsable:** "Seleccione el evaluador responsable del registro". Lo marca el integrante que hizo el contacto; no es una pregunta para el participante y en el CSV se guarda codificado (E1 a E4).

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

## 7. Verificación con herramientas (Python/R)

**Herramienta seleccionada:** Python 3 con la biblioteca pandas.

**Archivo:** `scripts/verificacion_encuesta.py`

El script tendrá como objetivo comprobar la estructura del CSV, detectar valores faltantes, verificar los tipos de datos y analizar las distribuciones de satisfacción y recomendación.

Además, permitirá separar respuestas reales y simuladas, evitando que los registros artificiales distorsionen la interpretación de los resultados.

### 7.1. Código de verificación

```python
from pathlib import Path
import pandas as pd

# TODO 1: Cargar el CSV con pandas
ruta = (
    Path(__file__).resolve().parent.parent
    / "plantillas"
    / "encuesta_respuestas.csv"
)

df = pd.read_csv(ruta)

print("=== AUDITORÍA DE ENCUESTA ===")
print("Registros:", len(df))
print("Columnas:", len(df.columns))

# TODO 2: Mostrar los dtypes
print("\n=== TIPOS DE DATOS ===")
print(df.dtypes)

# TODO 3: Mostrar los datos faltantes
print("\n=== DATOS FALTANTES ===")
print(df.isna().sum())

# TODO 4: Distribuciones generales
for columna in [
    "satisfaccion_general",
    "recomendaria"
]:
    print(f"\n=== {columna} ===")
    print(
        df[columna].value_counts(
            dropna=False
        ).sort_index()
    )

# Separar las respuestas reales de las simuladas
if "origen" in df.columns:
    reales = df.loc[
        df["origen"].astype(str).str.lower()
        == "real"
    ].copy()

    simuladas = df.loc[
        df["origen"].astype(str).str.lower()
        == "simulada"
    ].copy()

    print("\n=== ORIGEN DE LOS DATOS ===")
    print("Reales:", len(reales))
    print("Simuladas:", len(simuladas))
else:
    raise ValueError(
        "El CSV debe contener la columna origen"
    )

# Auditoría únicamente de registros reales
print("\n=== ANÁLISIS DE RESPUESTAS REALES ===")

if reales.empty:
    print("Aún no existen respuestas reales.")
else:
    for columna in [
        "satisfaccion_general",
        "recomendaria"
    ]:
        print(f"\n{columna}:")
        print(
            reales[columna].value_counts(
                dropna=False
            ).sort_index()
        )

    print("\nFaltantes en registros reales:")
    print(reales.isna().sum())

    print("\nPorcentaje de recomendación:")
    recomendacion = (
        reales["recomendaria"].eq("Si").mean()
        * 100
    )
    print(f"{recomendacion:.2f}%")

    print("\nSatisfacción favorable (4 o 5):")
    validas = pd.to_numeric(
        reales["satisfaccion_general"],
        errors="coerce"
    ).dropna()

    if len(validas) > 0:
        porcentaje = validas.ge(4).mean() * 100
        print(f"{porcentaje:.2f}%")
    else:
        print("Sin puntuaciones válidas")

    # Revisión de variables adicionales
    for columna in [
        "frecuencia_visita",
        "interes_programa",
        "beneficio_preferido",
        "aspecto_mejora"
    ]:
        if columna in reales.columns:
            print(f"\nDistribución de {columna}:")
            print(
                reales[columna].value_counts(
                    dropna=False
                )
            )

    # Comprobaciones de validez
    if "edad" in reales.columns:
        edad = pd.to_numeric(
            reales["edad"],
            errors="coerce"
        )
        print(
            "\nEdades inválidas:",
            (edad.lt(18) | edad.isna()).sum()
        )

    for columna in [
        "satisfaccion_general",
        "interes_programa"
    ]:
        if columna in reales.columns:
            valores = pd.to_numeric(
                reales[columna],
                errors="coerce"
            )
            invalidos = (
                ~valores.isin([1, 2, 3, 4, 5])
            ).sum()
            print(
                f"Valores inválidos en {columna}:",
                invalidos
            )

    # Posibles señales de sesgo
    print("\n=== INTERPRETACIÓN PRELIMINAR ===")
    print(
        "Una concentración de participantes "
        "en una sola categoría puede indicar "
        "un problema de cobertura."
    )
    print(
        "Una concentración extrema de "
        "respuestas positivas requiere "
        "revisar un posible sesgo de respuesta."
    )
    print(
        "El sesgo de no respuesta necesita "
        "también el registro de invitaciones "
        "y rechazos."
    )
```

### 7.2. Ejecución sobre el CSV de ejemplo

El CSV original del repositorio contiene cuatro filas ilustrativas, tres marcadas como reales y una como simulada.

Estas filas son únicamente ejemplos suministrados en la plantilla del laboratorio y no constituyen resultados recolectados por el Equipo 3.

Al ejecutar la auditoría sobre ese archivo se obtienen diez columnas:

| Columna | Dtype detectado | Faltantes |
|---|---|---:|
| `respuesta_id` | `object` | 0 |
| `fecha` | `object` | 0 |
| `ciudad` | `object` | 0 |
| `edad` | `int64` | 0 |
| `genero` | `object` | 0 |
| `frecuencia_visita` | `object` | 0 |
| `satisfaccion_general` | `int64` | 0 |
| `recomendaria` | `object` | 0 |
| `comentario` | `object` | 1 |
| `origen` | `object` | 0 |

**Distribución de satisfacción general, cuatro registros de ejemplo:**

| Satisfacción | Frecuencia |
|---|---:|
| 3 | 1 |
| 4 | 2 |
| 5 | 1 |

**Distribución de recomendación, cuatro registros de ejemplo:**

| Recomendación | Frecuencia |
|---|---:|
| Si | 3 |
| No | 1 |

**Separación por origen:**

| Origen | Registros |
|---|---:|
| real | 3 |
| simulada | 1 |

Los resultados anteriores únicamente demuestran el funcionamiento de la auditoría sobre datos ilustrativos.

### 7.3. ¿Coinciden los tipos con la predicción de la sección 4?

Sí, los campos compartidos entre el CSV original y el cuestionario propuesto presentan tipos coherentes con las predicciones.

Las columnas `edad` y `satisfaccion_general` se interpretan como `int64`, mientras que las variables categóricas almacenadas mediante etiquetas se interpretan como `object`.

En particular, la satisfacción se registra numéricamente pero sigue siendo una variable ordinal.

Las variables nuevas `interes_programa`, `beneficio_preferido` y `aspecto_mejora` deberán agregarse al CSV cuando se implemente el cuestionario definitivo. Sus tipos y valores se comprobarán después de aplicar la encuesta.

### 7.4. ¿Cuántos datos faltantes hay por columna?

En el CSV original de ejemplo se detecta un único dato faltante en la columna `comentario`. Las demás columnas presentan cero valores faltantes.

El campo `comentario` es opcional, por lo que la ausencia de un valor no constituye necesariamente un error de calidad. Es importante distinguir los datos no obligatorios de los datos requeridos para los indicadores principales.

### 7.5. Interpretación de los posibles sesgos

**Sesgo de selección:**

Una acumulación de participantes en un único grupo de edad o frecuencia de compra podría sugerir una cobertura limitada. Por ejemplo, una muestra compuesta casi exclusivamente por estudiantes universitarios no describiría adecuadamente la diversidad de compradores adultos de Quito.

**Sesgo de no respuesta:**

Para detectar este problema será necesario comparar las invitaciones realizadas con las encuestas válidas recibidas. Si un grupo de invitados responde significativamente menos que otro, podría existir un mecanismo de no respuesta asociado con sus características.

La presencia de celdas vacías también permitirá estudiar la no respuesta a preguntas específicas, pero no reemplaza el registro de las personas que nunca completaron el formulario.

**Sesgo de respuesta:**

Una distribución extremadamente concentrada en los valores más altos de satisfacción o en recomendaciones positivas podría justificar una revisión del instrumento y de las condiciones de aplicación. Esta concentración no demuestra por sí sola que exista sesgo.

**Interpretación de las filas reales del CSV de ejemplo:**

Al excluir la fila simulada, quedan tres registros ilustrativos con puntuaciones 3, 4 y 5, respectivamente. Dos de ellos incluyen recomendaciones afirmativas y uno una recomendación negativa.

El número de registros es demasiado pequeño y corresponde a datos de ejemplo. Por consiguiente, no se presentan conclusiones sobre los consumidores reales ni se atribuyen estos resultados al Equipo 3.

**Conclusión de la verificación:**

La auditoría permite comprobar que el CSV puede leerse correctamente, verificar los tipos de datos, identificar los valores faltantes y examinar las distribuciones solicitadas. La interpretación definitiva dependerá de las respuestas reales recolectadas y de la evaluación del procedimiento de muestreo.

---

## Conclusiones preliminares del diseño

1. El diseño de la encuesta establece una relación directa entre la satisfacción de los consumidores y las decisiones de la gerencia sobre programas de fidelización. Los indicadores definidos permiten obtener información descriptiva para identificar prioridades comerciales y oportunidades de mejora.

2. La combinación de un cuestionario estructurado, un muestreo declarado de forma transparente, medidas de confidencialidad y verificaciones mediante Python ofrece un procedimiento reproducible para el laboratorio. No obstante, las conclusiones deberán reconocer las limitaciones del muestreo por conveniencia y diferenciar estrictamente las respuestas reales de los registros simulados.

**Estado del trabajo:** Diseño propuesto. Pendientes de ejecución: aprobación del enfoque, aplicación de la encuesta, actualización del CSV y auditoría final con respuestas reales.
