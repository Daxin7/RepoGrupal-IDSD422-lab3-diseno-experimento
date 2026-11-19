# muestreo_encuesta.py — Sección 3: la línea de muestreo, con semilla y una corrida.
#
# Marco: data/clientes_400.csv, la base de clientes de RetailAndina usada en el
# laboratorio de muestreo (sin datos de contacto). Se filtra la población de la
# encuesta (Quito, 18 años o más) y se sortean 24 personas estratificando por grupo
# de edad con afijación proporcional; luego se reparten 6 por integrante.
#
# Uso (desde la raíz del repositorio):
#   python scripts/muestreo_encuesta.py

import pandas as pd

SEMILLA = 2026
TAMANO = 24

clientes = pd.read_csv("data/clientes_400.csv")
marco = clientes[(clientes["ciudad"] == "Quito") & (clientes["edad"] >= 18)].copy()
marco["grupo_edad"] = pd.cut(marco["edad"], [17, 29, 44, 65], labels=["18-29", "30-44", "45-65"])

muestra = marco.groupby("grupo_edad", observed=True).sample(frac=TAMANO / len(marco), random_state=SEMILLA)  # <- línea de muestreo

# Reparto de la lista sorteada: 6 contactos por integrante (E1 a E4), mezclando grupos de edad.
muestra = muestra.sample(frac=1, random_state=SEMILLA)
muestra["integrante"] = [f"E{i // 6 + 1}" for i in range(len(muestra))]

print(f"Marco (Quito, 18+): {len(marco)} clientes · muestra: {len(muestra)} · semilla: {SEMILLA}")
for integrante, grupo in muestra.groupby("integrante"):
    print(f"  {integrante}: {', '.join(grupo['cliente_id'])}")

comparacion = pd.DataFrame({
    "marco_n": marco["grupo_edad"].value_counts().sort_index(),
    "muestra_n": muestra["grupo_edad"].value_counts().sort_index(),
})
comparacion["marco_%"] = (comparacion["marco_n"] / len(marco) * 100).round(1)
comparacion["muestra_%"] = (comparacion["muestra_n"] / len(muestra) * 100).round(1)
print("\nComposición por grupo de edad:")
print(comparacion.to_string())
print(f"\nEdad en la muestra: mínimo {muestra['edad'].min()}, "
      f"máximo {muestra['edad'].max()}, media {muestra['edad'].mean():.1f}")
