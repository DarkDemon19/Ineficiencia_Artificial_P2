# Encuentra la secuencia de estados mas probable
# usando el algoritmo de Viterbi en un HMM

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

def Viterbi(Prob_inicial, Matriz_transicion, Matriz_emision, Observacion_seq):
    # obtener dimensiones
    Numero_estados = len(Estados)
    Numero_observaciones = len(Observacion_seq)

    # crear matrices
    T1 = np.zeros(
        (
            Numero_estados,
            Numero_observaciones
        )
    )

    T2 = np.zeros(
        (
            Numero_estados,
            Numero_observaciones
        ),
        dtype=int
    )

    # inicializar primer paso
    T1[:, 0] = Prob_inicial * Matriz_emision[
        :,
        Observacion_seq[0]
    ]

    # calcular probabilidades
    for Tiempo in range(1, Numero_observaciones):

        for Estado in range(Numero_estados):
            Prob_transicion = (
                T1[:, Tiempo - 1] *
                Matriz_transicion[:, Estado]
            )

            T1[Estado, Tiempo] = (
                np.max(Prob_transicion) *
                Matriz_emision[Estado, Observacion_seq[Tiempo]]
            )

            T2[Estado, Tiempo] = np.argmax(
                Prob_transicion
            )

    # reconstruir camino
    Camino_optimo = np.zeros(
        Numero_observaciones,
        dtype=int
    )

    Camino_optimo[-1] = np.argmax(
        T1[:, -1]
    )

    for Tiempo in range(Numero_observaciones - 2, -1, -1):
        Camino_optimo[Tiempo] = T2[
            Camino_optimo[Tiempo + 1],
            Tiempo + 1
        ]

    # convertir indices a nombres
    Camino_estado = [
        Estados[Indice]
        for Indice in Camino_optimo
    ]

    return Camino_estado

# ejecutar Viterbi
Camino_optimo = Viterbi(
    Prob_inicial,
    Matriz_transicion,
    Matriz_emision,
    Observacion_seq
)

# mostrar observaciones
print(
    "Secuencia de observaciones:",
    [
        Observaciones[Indice]
        for Indice in Observacion_seq
    ]
)

# mostrar camino mas probable
print(
    "Camino de estados mas probable:",
    Camino_optimo
)