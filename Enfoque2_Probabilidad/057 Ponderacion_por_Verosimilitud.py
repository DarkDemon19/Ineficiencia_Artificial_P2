# Calcula inferencia aproximada
# usando ponderacion de verosimilitud

# Para generar valores aleatorios
import random

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

# orden correcto de muestreo
Orden_vars = [
    "virus",
    "clima_frio",
    "fiebre",
    "sudor"
]

def Prob_true_de_nodo(Nodo, Asignacion, Red_local):
    # obtener probabilidad del nodo en True
    Padres = Red_local[Nodo]["padres"]

    Clave = tuple(
        Asignacion[Padre] for Padre in Padres
    )

    return Red_local[Nodo]["cpt"][Clave]

def Samplear_lw(Red_local, Orden, Evidencia):
    # generar muestra con peso
    Asignacion = {}
    Peso = 1.0

    for Nodo in Orden:
        Probabilidad_true = Prob_true_de_nodo(
            Nodo,
            Asignacion,
            Red_local
        )

        if Nodo in Evidencia:
            Valor_observado = Evidencia[Nodo]
            Asignacion[Nodo] = Valor_observado

            # ajustar peso por evidencia
            if Valor_observado is True:
                Peso *= Probabilidad_true

            else:
                Peso *= 1 - Probabilidad_true

        else:
            Asignacion[Nodo] = (
                random.random() < Probabilidad_true
            )

    return Asignacion, Peso

def Lw_inferencia(
    Variable_consulta,
    Evidencia,
    Red_local,
    Orden,
    Numero_muestras
):
    # acumular pesos
    Peso_true = 0.0
    Peso_false = 0.0

    for _ in range(Numero_muestras):
        Asignacion, Peso = Samplear_lw(
            Red_local,
            Orden,
            Evidencia
        )

        if Asignacion[Variable_consulta] is True:
            Peso_true += Peso

        else:
            Peso_false += Peso

    Total = Peso_true + Peso_false

    # evitar division entre cero
    if Total == 0:
        return {
            True: 0.0,
            False: 0.0
        }

    return {
        True: Peso_true / Total,
        False: Peso_false / Total
    }

# ejecutar consulta
Resultado = Lw_inferencia(
    Variable_consulta="fiebre",
    Evidencia={
        "sudor": True
    },
    Red_local=Red,
    Orden=Orden_vars,
    Numero_muestras=5000
)

# mostrar resultado
print(
    "Probabilidad aproximada con ponderacion de verosimilitud:"
)

print(
    "Fiebre = True ->",
    round(Resultado[True], 4)
)

print(
    "Fiebre = False ->",
    round(Resultado[False], 4)
)