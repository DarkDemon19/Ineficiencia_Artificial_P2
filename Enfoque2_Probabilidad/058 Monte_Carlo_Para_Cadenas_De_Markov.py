# Aproxima una distribucion de probabilidad
# usando Monte Carlo para cadenas de Markov

# Para generar valores aleatorios
import random

# distribucion objetivo
Objetivo = {
    "estado_a": 0.1,
    "estado_b": 0.4,
    "estado_c": 0.5
}

def Prob_objetivo(Estado):
    # obtener peso del estado
    return Objetivo[Estado]

def Proponer_estado(Actual, Todos):
    # proponer nuevo estado
    Candidatos = [
        Estado for Estado in Todos
        if Estado != Actual
    ]

    return random.choice(
        Candidatos
    )

def Metropolis_hastings(Iteraciones, Estado_inicial):
    # ejecutar MCMC
    Estado_actual = Estado_inicial
    Historial = [
        Estado_actual
    ]

    Todos_estados = list(
        Objetivo.keys()
    )

    for _ in range(Iteraciones):
        Candidato = Proponer_estado(
            Estado_actual,
            Todos_estados
        )

        P_actual = Prob_objetivo(
            Estado_actual
        )

        P_candidato = Prob_objetivo(
            Candidato
        )

        # calcular aceptacion
        if P_actual == 0:
            Acepto = True

        else:
            Razon = P_candidato / P_actual

            Acepto = (
                random.random() < min(1.0, Razon)
            )

        # actualizar estado
        if Acepto:
            Estado_actual = Candidato

        Historial.append(
            Estado_actual
        )

    return Historial

def Estimar_distribucion(Muestras):
    # contar muestras
    Conteo = {}

    for Estado in Muestras:
        Conteo[Estado] = Conteo.get(
            Estado,
            0
        ) + 1

    Total = len(
        Muestras
    )

    Aproximacion = {
        Estado: Conteo[Estado] / Total
        for Estado in Conteo
    }

    return Aproximacion

# ejecutar MCMC
Muestras = Metropolis_hastings(
    Iteraciones=5000,
    Estado_inicial="estado_a"
)

# estimar distribucion
Aproximacion = Estimar_distribucion(
    Muestras
)

# mostrar resultado
print(
    "Aproximacion de la distribucion con MCMC:"
)

for Estado, Probabilidad in Aproximacion.items():
    print(
        Estado,
        "->",
        round(Probabilidad, 4)
    )