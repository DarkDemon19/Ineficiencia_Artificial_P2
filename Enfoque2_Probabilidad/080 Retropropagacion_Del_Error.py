# Implementa una red neuronal simple de 2 capas
# para resolver XOR usando retropropagacion

# Para calculos numericos
import numpy as np

# funcion Sigmoid
def Sigmoid(X):
    return 1 / (
        1 + np.exp(-X)
    )

# derivada de Sigmoid
def Derivada_sigmoid(X):
    return X * (
        1 - X
    )

# datos XOR
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

# salidas esperadas
Y = np.array([
    [0],
    [1],
    [1],
    [0]
])

# fijar semilla
np.random.seed(
    42
)

# tamaños de capas
Tamano_entrada = X.shape[1]

Tamano_oculta = 2

Tamano_salida = Y.shape[1]

# pesos entrada a oculta
Pesos_entrada_oculta = np.random.rand(
    Tamano_entrada,
    Tamano_oculta
)

# pesos oculta a salida
Pesos_oculta_salida = np.random.rand(
    Tamano_oculta,
    Tamano_salida
)

# tasa de aprendizaje
Tasa_aprendizaje = 0.1

# entrenamiento
for Epoch in range(10000):

    # forward capa oculta
    Entrada_oculta = np.dot(
        X,
        Pesos_entrada_oculta
    )

    Salida_oculta = Sigmoid(
        Entrada_oculta
    )

    # forward capa salida
    Entrada_salida = np.dot(
        Salida_oculta,
        Pesos_oculta_salida
    )

    Salida_predicha = Sigmoid(
        Entrada_salida
    )

    # error
    Error = Y - Salida_predicha

    # backward salida
    Delta_salida = Error * Derivada_sigmoid(
        Salida_predicha
    )

    # error oculto
    Error_oculto = Delta_salida.dot(
        Pesos_oculta_salida.T
    )

    # backward oculto
    Delta_oculto = Error_oculto * Derivada_sigmoid(
        Salida_oculta
    )

    # actualizar pesos oculta salida
    Pesos_oculta_salida += Salida_oculta.T.dot(
        Delta_salida
    ) * Tasa_aprendizaje

    # actualizar pesos entrada oculta
    Pesos_entrada_oculta += X.T.dot(
        Delta_oculto
    ) * Tasa_aprendizaje

# mostrar resultados
print(
    "Salidas de la red despues del entrenamiento:"
)

print(
    Salida_predicha
)
