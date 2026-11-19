
import sys
from pathlib import Path

import pandas as pd

RAIZ = Path(__file__).resolve().parent.parent
SALIDA = RAIZ / "plantillas" / "encuesta_respuestas.csv"

# Columnas del export, en el mismo orden en que aparecen en el formulario.
COLUMNAS_FORMULARIO = [
    "marca_temporal", "consentimiento", "encuestador",
    "mayor_18", "reside_quito", "compra_30_dias", "cliente_retailandina",
    "edad", "frecuencia_visita", "satisfaccion_general", "recomendaria",
    "interes_programa", "beneficio_preferido", "aspecto_mejora", "comentario",
]

# Orden final del CSV que se comparte.
COLUMNAS_SALIDA = [
    "respuesta_id", "fecha", "encuestador", "consentimiento",
    "mayor_18", "reside_quito", "compra_30_dias", "cliente_retailandina",
    "edad", "frecuencia_visita", "satisfaccion_general", "recomendaria",
    "interes_programa", "beneficio_preferido", "aspecto_mejora", "comentario",
    "origen",
]

if len(sys.argv) != 2:
    sys.exit("Uso: python scripts/anonimizar_respuestas.py <export_crudo.csv>")

crudo = pd.read_csv(sys.argv[1], dtype=str, keep_default_na=False)
if crudo.shape[1] != len(COLUMNAS_FORMULARIO):
    sys.exit(f"Se esperaban {len(COLUMNAS_FORMULARIO)} columnas y llegaron {crudo.shape[1]}")

df = crudo.set_axis(COLUMNAS_FORMULARIO, axis=1)
df = df.apply(lambda col: col.str.strip()).replace("", pd.NA)

# El export ya viene en orden cronológico: ese orden define los identificadores.
df["respuesta_id"] = [f"R{i:03d}" for i in range(1, len(df) + 1)]
df["fecha"] = pd.to_datetime(df["marca_temporal"].str[:10], format="%Y/%m/%d").dt.strftime("%Y-%m-%d")

codigos = {nombre: f"E{i}" for i, nombre in enumerate(df["encuestador"].dropna().unique(), start=1)}
df["encuestador"] = df["encuestador"].map(codigos)

df["consentimiento"] = df["consentimiento"].str.split(" (", regex=False).str[0]
df["edad"] = pd.to_numeric(df["edad"]).astype("Int64")
for escala in ["satisfaccion_general", "interes_programa"]:
    df[escala] = df[escala].str.extract(r"^(\d)", expand=False).astype("Int64")

df["origen"] = "real"

df[COLUMNAS_SALIDA].to_csv(SALIDA, index=False, encoding="utf-8")
print(f"{len(df)} respuestas reales anonimizadas -> {SALIDA.relative_to(RAIZ)}")
print(f"Integrantes codificados: {len(codigos)} (E1 a E{len(codigos)})")
