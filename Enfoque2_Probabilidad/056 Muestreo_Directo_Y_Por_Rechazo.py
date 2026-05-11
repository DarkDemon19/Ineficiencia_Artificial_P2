# Calcula inferencia aproximada
# usando muestreo directo y muestreo por rechazo

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

def Samplear_una_vez(Red_local, Orden):
    # generar una muestra completa
    Asignacion = {}

    for Nodo in Orden:
        Probabilidad_true = Prob_true_de_nodo(
            Nodo,
            Asignacion,
            Red_local
        )

        Asignacion[Nodo] = (
            random.random() < Probabilidad_true
        )

    return Asignacion

def Muestreo_directo(Red_local, Orden, Numero_muestras):
    # generar varias muestras
    Datos = []

    for _ in range(Numero_muestras):
        Datos.append(
            Samplear_una_vez(
                Red_local,
                Orden
            )
        )

    return Datos

def Cumple_evidencia(Muestra, Evidencia):
    # verificar evidencia
    for Variable, Valor in Evidencia.items():

        if Muestra[Variable] != Valor:
            return False

    return True

def Muestreo_por_rechazo(
    Red_local,
    Orden,
    Numero_muestras,
    Variable_consulta,
    Evidencia
):
    # contadores
    Conteo_true = 0
    Conteo_false = 0

    # generar muestras
    for _ in range(Numero_muestras):

        Muestra = Samplear_una_vez(
            Red_local,
            Orden
        )

        # descartar si no cumple evidencia
        if not Cumple_evidencia(
            Muestra,
            Evidencia
        ):
            continue

        # contar valores validos
        if Muestra[Variable_consulta] is True:
            Conteo_true += 1

        else:
            Conteo_false += 1

    Total_validas = (
        Conteo_true +
        Conteo_false
    )

    # evitar division entre cero
    if Total_validas == 0:
        return {
            True: 0.0,
            False: 0.0
        }

    Probabilidad_true = (
        Conteo_true / Total_validas
    )

    Probabilidad_false = (
        Conteo_false / Total_validas
    )

    return {
        True: Probabilidad_true,
        False: Probabilidad_false
    }

# ejecutar consulta
Resultado = Muestreo_por_rechazo(
    Red_local=Red,
    Orden=Orden_vars,
    Numero_muestras=5000,
    Variable_consulta="fiebre",
    Evidencia={
        "sudor": True
    }
)

# mostrar resultado
print(
    "Probabilidad aproximada con muestreo por rechazo:"
)

print(
    "Fiebre = True ->",
    round(Resultado[True], 4)
)

print(
    "Fiebre = False ->",
    round(Resultado[False], 4)
)