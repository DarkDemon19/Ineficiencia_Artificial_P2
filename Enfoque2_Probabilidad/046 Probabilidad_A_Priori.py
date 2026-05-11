# Calcula probabilidad a priori
# usando informacion inicial antes de observar resultados

# cantidad de dulces por color
Rojos = 3
Azules = 1

# total de dulces
Total = Rojos + Azules

# calcular probabilidad inicial
Probabilidad_rojo_apriori = Rojos / Total
Probabilidad_azul_apriori = Azules / Total

# mostrar probabilidades
print(
    "Probabilidad a priori de sacar dulce rojo =",
    Probabilidad_rojo_apriori
)

print(
    "Probabilidad a priori de sacar dulce azul =",
    Probabilidad_azul_apriori
)

# mostrar porcentajes
print(
    "Rojo en porcentaje =",
    Probabilidad_rojo_apriori * 100,
    "%"
)

print(
    "Azul en porcentaje =",
    Probabilidad_azul_apriori * 100,
    "%"
)