# Crea una distribucion de probabilidad
# para representar las probabilidades de un dado justo

# probabilidades del dado
Distribucion_dado = {
    1: 1 / 6,
    2: 1 / 6,
    3: 1 / 6,
    4: 1 / 6,
    5: 1 / 6,
    6: 1 / 6
}

# mostrar distribucion
print(
    "Distribucion de probabilidad de un dado justo:\n"
)

for Cara, Probabilidad in Distribucion_dado.items():

    print(
        "Numero",
        Cara,
        "=> Probabilidad =",
        Probabilidad,
        "Equivale a",
        Probabilidad * 100,
        "%"
    )

# verificar suma total
Suma_total = 0

for Probabilidad in Distribucion_dado.values():
    Suma_total += Probabilidad

print(
    "\nLa suma de todas las probabilidades es:",
    Suma_total
)