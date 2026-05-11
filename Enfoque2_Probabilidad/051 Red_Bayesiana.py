# Representa una red bayesiana simple
# mostrando relaciones entre variables y probabilidades condicionales

# nodos de la red
Nodos = [
    "fumar",
    "cancer",
    "tos"
]

# dependencias entre nodos
Padres = {
    "fumar": [],
    "cancer": ["fumar"],
    "tos": ["fumar", "cancer"]
}

# probabilidad inicial de fumar
P_fumar = 0.3

def P_cancer_dado_fumar(Fuma):
    # calcular probabilidad de cancer segun fumar

    if Fuma:
        return 0.2

    else:
        return 0.01

def P_tos_dado_fumar_y_cancer(Fuma, Tiene_cancer):
    # calcular probabilidad de tos segun fumar y cancer

    if Tiene_cancer:
        return 0.9

    elif Fuma and not Tiene_cancer:
        return 0.5

    else:
        return 0.1

# mostrar estructura de la red
print(
    "Nodos de la red bayesiana:",
    Nodos
)

print(
    "Padres de cada nodo:",
    Padres
)

# mostrar probabilidades
print(
    "\nEjemplos de probabilidades:"
)

print(
    "P(fumar = True) =",
    P_fumar
)

print(
    "P(cancer = True | fumar = True) =",
    P_cancer_dado_fumar(True)
)

print(
    "P(cancer = True | fumar = False) =",
    P_cancer_dado_fumar(False)
)

print(
    "P(tos = True | fuma = True, cancer = True) =",
    P_tos_dado_fumar_y_cancer(True, True)
)

print(
    "P(tos = True | fuma = True, cancer = False) =",
    P_tos_dado_fumar_y_cancer(True, False)
)

print(
    "P(tos = True | fuma = False, cancer = False) =",
    P_tos_dado_fumar_y_cancer(False, False)
)