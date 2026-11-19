#Relleno simulado del CSV de la encuesta

from pathlib import Path

import numpy as np
import pandas as pd

RAIZ = Path(__file__).resolve().parent.parent
RUTA = RAIZ / "plantillas" / "encuesta_respuestas.csv"
TOTAL_FILAS = 80
SEMILLA = 2026

OPCIONES = {
    "frecuencia_visita": ["Varias veces por semana", "Semanal", "Quincenal",
                          "Mensual", "Menos de una vez al mes"],
    "satisfaccion_general": [1, 2, 3, 4, 5],
    "recomendaria": ["Sí", "No"],
    "interes_programa": [1, 2, 3, 4, 5],
    "beneficio_preferido": ["Descuentos directos", "Acumulación de puntos",
                            "Promociones personalizadas",
                            "Productos o recompensas gratuitas", "Otro", "Ninguno"],
    "aspecto_mejora": ["Precios", "Atención al cliente", "Rapidez en caja",
                       "Variedad de productos", "Disponibilidad de productos",
                       "Limpieza y comodidad", "Ninguno", "Otro"],
}
FILTROS = ["mayor_18", "reside_quito", "compra_30_dias", "cliente_retailandina"]

df = pd.read_csv(RUTA, dtype={"satisfaccion_general": "Int64",
                              "interes_programa": "Int64", "edad": "Int64"})
reales = df[df["origen"] == "real"]
validas = reales[reales[FILTROS].eq("Sí").all(axis=1)]
n_sim = TOTAL_FILAS - len(reales)

rng = np.random.default_rng(SEMILLA)
sim = pd.DataFrame({
    "respuesta_id": [f"R{i:03d}" for i in range(len(reales) + 1, TOTAL_FILAS + 1)],
    "consentimiento": "Sí",
    **{filtro: "Sí" for filtro in FILTROS},
})

edad = rng.normal(validas["edad"].mean(), validas["edad"].std(), size=n_sim)
sim["edad"] = np.maximum(18, np.round(edad)).astype(int)

for columna, opciones in OPCIONES.items():
    conteo = validas[columna].value_counts().reindex(opciones, fill_value=0)
    prob = (conteo + 1) / (conteo + 1).sum()
    sim[columna] = rng.choice(opciones, size=n_sim, p=prob.to_numpy())

sim["origen"] = "simulada"

final = pd.concat([reales, sim[[c for c in df.columns if c in sim.columns]]],
                  ignore_index=True)[df.columns]
final.to_csv(RUTA, index=False, encoding="utf-8")
print(f"Reales: {len(reales)} (válidas: {len(validas)}) · simuladas: {n_sim} · total: {len(final)}")
