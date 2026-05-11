# Calcula inferencia por enumeracion
# usando evidencia dentro de una red bayesiana

# estructura de la red
Red = {
    "virus": {
        "padres": [],
        "cpt": {
            (): 0.1
        }
    },

    "clima_frio": {
        "padres": [],
        "cpt": {
            (): 0.3
        }
    },

    "fiebre": {
        "padres": [
            "virus",
            "clima_frio"
        ],
        "cpt": {
            (True, True): 0.9,
            (True, False): 0.8,
            (False, True): 0.6,
            (False, False): 0.05
        }
    },

    "sudor": {
        "padres": [
            "fiebre"
        ],
        "cpt": {
            (True,): 0.85,
            (False,): 0.1
        }
    }
}

# orden de variables
Orden_vars = [
    "virus",
    "clima_frio",
    "fiebre",
    "sudor"
]

def Prob_var_true(Variable, Evidencia, Red_local):
    # obtener probabilidad de variable verdadera
    Padres = Red_local[Variable]["padres"]

    Clave = tuple(
        Evidencia[Padre] for Padre in Padres
    )

    return Red_local[Variable]["cpt"][Clave]

def Prob_de_var(Variable, Valor, Evidencia, Red_local):
    # obtener probabilidad segun valor
    P_true = Prob_var_true(
        Variable,
        Evidencia,
        Red_local
    )

    if Valor is True:
        return P_true

    else:
        return 1 - P_true

def Enumerar_todo(Variables_restantes, Evidencia, Red_local):
    # enumerar variables faltantes
    if len(Variables_restantes) == 0:
        return 1.0

    Variable = Variables_restantes[0]
    Resto = Variables_restantes[1:]

    if Variable in Evidencia:
        Probabilidad = Prob_de_var(
            Variable,
            Evidencia[Variable],
            Evidencia,
            Red_local
        )

        return Probabilidad * Enumerar_todo(
            Resto,
            Evidencia,
            Red_local
        )

    else:
        Total = 0.0

        for Valor in [
            True,
            False
        ]:
            Nueva_evidencia = Evidencia.copy()
            Nueva_evidencia[Variable] = Valor

            Probabilidad = Prob_de_var(
                Variable,
                Valor,
                Nueva_evidencia,
                Red_local
            )

            Total += Probabilidad * Enumerar_todo(
                Resto,
                Nueva_evidencia,
                Red_local
            )

        return Total

def Normalizar(Distribucion):
    # normalizar para que sume 1
    Suma = sum(
        Distribucion.values()
    )

    return {
        Llave: Valor / Suma
        for Llave, Valor in Distribucion.items()
    }

def Preguntar(Variable_objetivo, Evidencia, Red_local, Orden):
    # calcular probabilidad con evidencia
    Distribucion = {}

    for Valor in [
        True,
        False
    ]:
        Evidencia_temporal = Evidencia.copy()
        Evidencia_temporal[Variable_objetivo] = Valor

        Distribucion[Valor] = Enumerar_todo(
            Orden,
            Evidencia_temporal,
            Red_local
        )

    return Normalizar(
        Distribucion
    )

# realizar consulta
Resultado = Preguntar(
    "fiebre",
    {
        "sudor": True
    },
    Red,
    Orden_vars
)

# mostrar resultado
print(
    "Probabilidad de fiebre dado sudor = True:"
)

print(
    "Fiebre = True ->",
    round(Resultado[True], 4)
)

print(
    "Fiebre = False ->",
    round(Resultado[False], 4)
)