# Calcula la probabilidad de una secuencia de observaciones
# usando el algoritmo hacia adelante en un modelo oculto de Markov

# probabilidades de transicion
Probabilidades_transicion = {
    "Fernanda": {
        "Fernanda": 0.6,
        "Emmanuel": 0.3,
        "Emiliano": 0.1
    },

    "Emmanuel": {
        "Fernanda": 0.2,
        "Emmanuel": 0.5,
        "Emiliano": 0.3
    },

    "Emiliano": {
        "Fernanda": 0.1,
        "Emmanuel": 0.4,
        "Emiliano": 0.5
    }
}

# probabilidades de emision
Probabilidades_emision = {
    "Fernanda": {
        "si": 0.7,
        "no": 0.3
    },

    "Emmanuel": {
        "si": 0.4,
        "no": 0.6
    },

    "Emiliano": {
        "si": 0.8,
        "no": 0.2
    }
}

# probabilidades iniciales
Probabilidades_iniciales = {
    "Fernanda": 0.5,
    "Emmanuel": 0.3,
    "Emiliano": 0.2
}

# secuencia observada
Secuencia_observaciones = [
    "si",
    "no",
    "si"
]

def Calcular_probabilidad(Secuencia_observaciones):
    # inicializar primer paso
    Probabilidades_actuales = {
        Estado:
        Probabilidades_iniciales[Estado] *
        Probabilidades_emision[Estado][Secuencia_observaciones[0]]

        for Estado in Probabilidades_iniciales
    }

    # recorrer observaciones restantes
    for Observacion in Secuencia_observaciones[1:]:

        Probabilidades_siguientes = {}

        for Estado in Probabilidades_transicion:

            # calcular probabilidad total
            Probabilidades_siguientes[Estado] = sum(
                Probabilidades_actuales[Estado_anterior] *
                Probabilidades_transicion[Estado_anterior][Estado]

                for Estado_anterior in Probabilidades_transicion
            ) * Probabilidades_emision[Estado][Observacion]

        # actualizar probabilidades
        Probabilidades_actuales = Probabilidades_siguientes

    # sumar probabilidad final
    return sum(
        Probabilidades_actuales.values()
    )

# ejecutar calculo
Probabilidad_resultado = Calcular_probabilidad(
    Secuencia_observaciones
)

# mostrar resultado
print(
    "Probabilidad de la secuencia de observaciones:",
    Probabilidad_resultado
)