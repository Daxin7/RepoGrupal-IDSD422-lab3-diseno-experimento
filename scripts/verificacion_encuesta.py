# verificacion_encuesta.py — Auditoría de la encuesta (Python)
# Ejecuta desde la raíz del repositorio:
#   python scripts/verificacion_encuesta.py

import pandas as pd

FILTROS = ["mayor_18", "reside_quito", "compra_30_dias", "cliente_retailandina"]

# TODO 1: carga plantillas/encuesta_respuestas.csv con pandas
df = pd.read_csv("plantillas/encuesta_respuestas.csv")
print(f"Filas: {len(df)} · columnas: {df.shape[1]}")
print(df["origen"].value_counts().to_string(), "\n")

# TODO 2: imprime los tipos (dtypes) de cada columna
print("Tipos (dtypes):")
print(df.dtypes.to_string(), "\n")

# TODO 3: imprime el conteo de datos faltantes (NA) por columna
print("Faltantes por columna (todas las filas):")
print(df.isna().sum().to_string(), "\n")

# Las conclusiones se sacan solo con las respuestas reales y válidas
reales = df[df["origen"] == "real"]
validas = reales[reales[FILTROS].eq("Sí").all(axis=1)]
print(f"Reales: {len(reales)} · válidas (los 4 filtros en 'Sí'): {len(validas)}")
print("Filtros con 'No' entre las reales:")
print(reales[FILTROS].eq("No").sum().to_string(), "\n")

# TODO 4: imprime la distribución de satisfaccion_general y de recomendaria
for columna in ["satisfaccion_general", "recomendaria", "interes_programa",
                "frecuencia_visita", "beneficio_preferido", "aspecto_mejora"]:
    print(f"{columna} (reales válidas):")
    print(validas[columna].value_counts().sort_index().to_string(), "\n")

print("Edad (reales válidas):")
print(validas["edad"].describe().round(1).to_string(), "\n")

print("Indicadores (reales válidas):")
print(f"  satisfacción favorable (4-5): {validas['satisfaccion_general'].ge(4).mean():.1%}")
print(f"  satisfacción promedio:        {validas['satisfaccion_general'].mean():.2f}")
print(f"  recomendaría (Sí):            {validas['recomendaria'].eq('Sí').mean():.1%}")
print(f"  interés en el programa (4-5): {validas['interes_programa'].ge(4).mean():.1%}")
print("\nSatisfacción vs. recomendación (reales válidas):")
print(pd.crosstab(validas["satisfaccion_general"], validas["recomendaria"]).to_string())

# TODO 5: interpretación (sección 7 de la plantilla)
# - Selección: si casi todas las edades caen en un solo grupo, la red de contactos
#   del equipo no cubre a la población (aquí todas las válidas tienen 19-29 años).
# - Respuesta/cortesía: 100 % de "Sí" en recomendaria aun con satisfacción 3 sugiere
#   respuestas complacientes con el encuestador conocido.
# - No respuesta: se mide con el registro de contactos que no contestaron, no con el CSV.
