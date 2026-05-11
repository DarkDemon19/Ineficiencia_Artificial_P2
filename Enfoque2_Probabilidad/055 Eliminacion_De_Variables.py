# Calcula inferencia por eliminacion de variables
# reduciendo factores dentro de una red bayesiana

# Para crear combinaciones
import itertools

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

def Todas_asignaciones(Variables_lista):
    # generar combinaciones True y False
    for Valores in itertools.product(
        [True, False],
        repeat=len(Variables_lista)
    ):
        yield dict(
            zip(Variables_lista, Valores)
        )

def Hacer_factor(Variable, Red_local):
    # crear factor desde una variable
    Padres = Red_local[Variable]["padres"]
    Variables_factor = [Variable] + Padres
    Tabla = {}

    for Asignacion in Todas_asignaciones(Variables_factor):
        Clave_padres = tuple(
            Asignacion[Padre] for Padre in Padres
        )

        P_true = Red_local[Variable]["cpt"][Clave_padres]

        if Asignacion[Variable] is True:
            P_valor = P_true

        else:
            P_valor = 1 - P_true

        Fila = tuple(
            Asignacion[Var] for Var in Variables_factor
        )

        Tabla[Fila] = P_valor

    return {
        "vars": Variables_factor,
        "table": Tabla
    }

def Restringir_factor(Factor, Variable, Valor):
    # aplicar evidencia al factor
    if Variable not in Factor["vars"]:
        return Factor

    Indice = Factor["vars"].index(Variable)

    Nuevas_vars = [
        Var for Var in Factor["vars"]
        if Var != Variable
    ]

    Nueva_tabla = {}

    for Fila, Probabilidad in list(Factor["table"].items()):
        if Fila[Indice] == Valor:
            Fila_sin = tuple(
                Valor_fila
                for Indice_fila, Valor_fila in enumerate(Fila)
                if Indice_fila != Indice
            )

            Nueva_tabla[Fila_sin] = Probabilidad

    return {
        "vars": Nuevas_vars,
        "table": Nueva_tabla
    }

def Multiplicar_factores(Factor1, Factor2):
    # multiplicar factores
    Variables1 = Factor1["vars"]
    Variables2 = Factor2["vars"]

    Nuevas_vars = list(
        dict.fromkeys(Variables1 + Variables2)
    )

    Nueva_tabla = {}

    for Asignacion in Todas_asignaciones(Nuevas_vars):
        Fila1 = tuple(
            Asignacion[Variable] for Variable in Variables1
        )

        Fila2 = tuple(
            Asignacion[Variable] for Variable in Variables2
        )

        if Fila1 in Factor1["table"] and Fila2 in Factor2["table"]:
            Fila_nueva = tuple(
                Asignacion[Variable] for Variable in Nuevas_vars
            )

            Nueva_tabla[Fila_nueva] = (
                Factor1["table"][Fila1] *
                Factor2["table"][Fila2]
            )

    return {
        "vars": Nuevas_vars,
        "table": Nueva_tabla
    }

def Sumar_fuera(Factor, Variable):
    # eliminar variable sumando sus valores
    if Variable not in Factor["vars"]:
        return Factor

    Indice = Factor["vars"].index(Variable)

    Nuevas_vars = [
        Var for Var in Factor["vars"]
        if Var != Variable
    ]

    Nueva_tabla = {}

    for Fila, Probabilidad in Factor["table"].items():
        Fila_sin = tuple(
            Valor_fila
            for Indice_fila, Valor_fila in enumerate(Fila)
            if Indice_fila != Indice
        )

        Nueva_tabla[Fila_sin] = Nueva_tabla.get(
            Fila_sin,
            0.0
        ) + Probabilidad

    return {
        "vars": Nuevas_vars,
        "table": Nueva_tabla
    }

def Normalizar_en_var(Factor, Variable_objetivo):
    # normalizar resultado final
    Indice = Factor["vars"].index(Variable_objetivo)

    Distribucion = {
        True: 0.0,
        False: 0.0
    }

    for Fila, Probabilidad in Factor["table"].items():
        Valor_variable = Fila[Indice]
        Distribucion[Valor_variable] += Probabilidad

    Total = Distribucion[True] + Distribucion[False]

    if Total != 0:
        Distribucion[True] /= Total
        Distribucion[False] /= Total

    return Distribucion

def Inferencia_eliminacion(Variable_consulta, Evidencia, Red_local):
    # crear factores iniciales
    Factores = [
        Hacer_factor(Variable, Red_local)
        for Variable in Red_local.keys()
    ]

    # aplicar evidencia
    for Variable_evidencia, Valor_evidencia in Evidencia.items():
        Factores = [
            Restringir_factor(
                Factor,
                Variable_evidencia,
                Valor_evidencia
            )
            for Factor in Factores
        ]

    # elegir variables ocultas
    Todas = list(
        Red_local.keys()
    )

    Ocultas = [
        Variable for Variable in Todas
        if Variable != Variable_consulta and Variable not in Evidencia
    ]

    # eliminar variables ocultas
    for Variable in Ocultas:
        Con_variable = [
            Factor for Factor in Factores
            if Variable in Factor["vars"]
        ]

        Sin_variable = [
            Factor for Factor in Factores
            if Variable not in Factor["vars"]
        ]

        if len(Con_variable) == 0:
            Factores = Sin_variable
            continue

        Combinado = Con_variable[0]

        for Factor2 in Con_variable[1:]:
            Combinado = Multiplicar_factores(
                Combinado,
                Factor2
            )

        Reducido = Sumar_fuera(
            Combinado,
            Variable
        )

        Factores = Sin_variable + [Reducido]

    # multiplicar factores restantes
    Final = Factores[0]

    for Factor2 in Factores[1:]:
        Final = Multiplicar_factores(
            Final,
            Factor2
        )

    # regresar distribucion normalizada
    return Normalizar_en_var(
        Final,
        Variable_consulta
    )

# ejecutar consulta
Resultado = Inferencia_eliminacion(
    Variable_consulta="fiebre",
    Evidencia={
        "sudor": True
    },
    Red_local=Red
)

# mostrar resultado
print(
    "Resultado inferencia con eliminacion de variables:"
)

print(
    "Fiebre = True ->",
    round(Resultado[True], 4)
)

print(
    "Fiebre = False ->",
    round(Resultado[False], 4)
)