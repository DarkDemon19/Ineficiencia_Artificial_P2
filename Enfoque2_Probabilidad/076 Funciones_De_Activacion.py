# Grafica funciones de activacion usadas en redes neuronales
# mostrando Sigmoid, Tanh, ReLU y Leaky ReLU

# Para calculos numericos
import numpy as np

# Para crear graficas
import matplotlib.pyplot as plt

# rango de valores
Valores_x = np.linspace(
    -10,
    10,
    100
)

# funcion Sigmoid
def Sigmoid(X):
    return 1 / (
        1 + np.exp(-X)
    )

# funcion Tanh
def Tanh(X):
    return np.tanh(
        X
    )

# funcion ReLU
def Relu(X):
    return np.maximum(
        0,
        X
    )

# funcion Leaky ReLU
def Leaky_relu(X, Alpha=0.01):
    return np.where(
        X > 0,
        X,
        Alpha * X
    )

# calcular valores de salida
Salida_sigmoid = Sigmoid(
    Valores_x
)

Salida_tanh = Tanh(
    Valores_x
)

Salida_relu = Relu(
    Valores_x
)

Salida_leaky_relu = Leaky_relu(
    Valores_x
)

# crear figura
plt.figure(
    figsize=(12, 8)
)

# grafica Sigmoid
plt.subplot(
    2,
    2,
    1
)

plt.plot(
    Valores_x,
    Salida_sigmoid,
    color="blue",
    label="Sigmoid"
)

plt.title(
    "Funcion Sigmoid"
)

plt.grid(True)

plt.legend()

# grafica Tanh
plt.subplot(
    2,
    2,
    2
)

plt.plot(
    Valores_x,
    Salida_tanh,
    color="orange",
    label="Tanh"
)

plt.title(
    "Funcion Tanh"
)

plt.grid(True)

plt.legend()

# grafica ReLU
plt.subplot(
    2,
    2,
    3
)

plt.plot(
    Valores_x,
    Salida_relu,
    color="green",
    label="ReLU"
)

plt.title(
    "Funcion ReLU"
)

plt.grid(True)

plt.legend()

# grafica Leaky ReLU
plt.subplot(
    2,
    2,
    4
)

plt.plot(
    Valores_x,
    Salida_leaky_relu,
    color="red",
    label="Leaky ReLU"
)

plt.title(
    "Funcion Leaky ReLU"
)

plt.grid(True)

plt.legend()

# ajustar diseño
plt.tight_layout()

# mostrar grafica
plt.show()
