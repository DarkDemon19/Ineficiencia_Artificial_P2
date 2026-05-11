# Calcula la probabilidad de una secuencia de observaciones
# usando los algoritmos hacia adelante y hacia atras en un HMM

# Para calculos numericos
import numpy as np

# estados del modelo
Estados = [
    "Soleado",
    "Lluvioso"
]

# observaciones posibles
Observaciones = [
    "Caminar",
    "Comprar",
    "Limpiar"
]

# probabilidades iniciales
Prob_inicial = np.array([
    0.6,
    0.4
])

# matriz de transicion
Matriz_transicion = np.array([
    [0.7, 0.3],
    [0.4, 0.6]
])

# matriz de emision
Matriz_emision = np.array([
    [0.1, 0.4, 0.5],
    [0.6, 0.3, 0.1]
])

# secuencia de observaciones
Observacion_seq = [
    0,
    1,
    2
]

def Hacia_adelante(Prob_inicial, Matriz_transicion, Matriz_emision, Observacion_seq):
    # crear matriz alfa
    Alfa = np.zeros(
        (
            len(Observacion_seq),
            len(Estados)
        )
    )

    # paso inicial
    Alfa[0, :] = Prob_inicial * Matriz_emision[
        :,
        Observacion_seq[0]
    ]

    # calcular hacia adelante
    for Tiempo in range(1, len(Observacion_seq)):

        for Estado in range(len(Estados)):
            Alfa[Tiempo, Estado] = np.sum(
                Alfa[Tiempo - 1] *
                Matriz_transicion[:, Estado]
            ) * Matriz_emision[
                Estado,
                Observacion_seq[Tiempo]
            ]

    return Alfa

def Hacia_atras(Matriz_transicion, Matriz_emision, Observacion_seq):
    # crear matriz beta
    Beta = np.zeros(
        (
            len(Observacion_seq),
            len(Estados)
        )
    )

    # paso final
    Beta[-1, :] = 1

    # calcular hacia atras
    for Tiempo in range(len(Observacion_seq) - 2, -1, -1):

        for Estado in range(len(Estados)):
            Beta[Tiempo, Estado] = np.sum(
                Matriz_transicion[Estado, :] *
                Matriz_emision[:, Observacion_seq[Tiempo + 1]] *
                Beta[Tiempo + 1]
            )

    return Beta

# ejecutar algoritmo hacia adelante
Alfa = Hacia_adelante(
    Prob_inicial,
    Matriz_transicion,
    Matriz_emision,
    Observacion_seq
)

# ejecutar algoritmo hacia atras
Beta = Hacia_atras(
    Matriz_transicion,
    Matriz_emision,
    Observacion_seq
)

# calcular probabilidad total
Probabilidad_observaciones = np.sum(
    Alfa[-1, :]
)

# mostrar resultado
print(
    f"Probabilidad de la secuencia de observaciones: {Probabilidad_observaciones:.4f}"
)

print(
    "Alfa hacia adelante:"
)

print(
    Alfa
)

print(
    "Beta hacia atras:"
)

print(
    Beta
)