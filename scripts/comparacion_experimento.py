# comparacion_experimento.py — Comparación de grupos (Python)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   python scripts/comparacion_experimento.py

# TODO 1: carga plantillas/registro_experimento.csv con pandas
import pandas as pd
df = pd.read_csv("registro_experimento.csv")
print(df.head())
print("*" * 5)
# TODO 2: calcula e imprime el promedio de ventas_producto por ubicacion
promedio = df.groupby("ubicacion")["ventas_producto"].mean()
print(promedio)
print("*" * 5)
# TODO 3: imprime el número de registros por grupo (value_counts)
print(df["ubicacion"].value_counts())
# TODO 4: escribe 2–3 líneas de interpretación (sección 9 de la plantilla):
#         por qué con 4 filas no se puede concluir y qué le faltaría al análisis

#################################################################################

# Diseño del experimento
import pandas as pd
import numpy as np # paquete que se usa calculos matematicos o estadisticos basicos
# En este caso usamos numpy para la aleatoriedad del producto en cada tienda para cada semana


# crear un arreglo de tiendas
tiendas = ["Quito Norte", "Quito Sur", "Guayaquil Centro", "Guayaquil Norte",
           "Cuenca Centro", "Cuenca Sur", "Ambato Centro", "Manta", "Loja",
           "Machala"]

# definir arreglo de semanas
semanas = [1, 2, 3, 4]
# Sorteo de la condicion inicial
rng = np.random.default_rng(1234597) # la funcion .defaul_rng( aqui debemos poner una semilla diferente, no los mismos numeros)
primera = rng.choice(["pasillo_principal", "pasillo_habitual"],
                     size=len(tiendas))#va a generar una lista de 10 elementos asociados a los valores que le dimos como fil

filas = []
for tienda, cond in zip(tiendas, primera):
  otra = "habitual" if cond == "pasillo_principal" else "pasillo_principal"
  for s in semanas:
    filas.append({"tienda": tienda, "semilla" : s,
                  "ubicacion": cond if s%2 == 1 else otra})

print(filas)