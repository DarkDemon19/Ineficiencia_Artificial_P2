# Implementa un perceptron con datos linealmente separables
# y muestra la linea de decision entre dos clases

# Para calculos numericos
import numpy as np

# Para crear graficas
import matplotlib.pyplot as plt

# fijar semilla
np.random.seed(
    0
)

# numero de muestras por clase
Numero_muestras = 100

# generar clase 1
X1 = np.random.randn(
    Numero_muestras,
    2
) + np.array([
    1,
    1
])

# generar clase 0
X2 = np.random.randn(
    Numero_muestras,
    2
) + np.array([
    -1,
    -1
])

# unir clases
X = np.vstack(
    (
        X1,
        X2
    )
)

# crear etiquetas
Y = np.array(
    [1] * Numero_muestras +
    [0] * Numero_muestras
)

# agregar sesgo
X_con_sesgo = np.c_[
    np.ones(
        (
            X.shape[0],
            1
        )
    ),
    X
]

# tasa de aprendizaje
Tasa_aprendizaje = 0.1

# numero de iteraciones
Numero_iteraciones = 1000

# inicializar pesos
Pesos = np.random.randn(
    X_con_sesgo.shape[1]
)

# funcion escalon
def Funcion_escalon(X):
    return 1 if X >= 0 else 0

# entrenamiento
for _ in range(Numero_iteraciones):

    for Indice in range(len(Y)):

        # salida lineal
        Salida_lineal = np.dot(
            X_con_sesgo[Indice],
            Pesos
        )

        # prediccion
        Prediccion = Funcion_escalon(
            Salida_lineal
        )

        # ajuste
        Actualizacion = Tasa_aprendizaje * (
            Y[Indice] - Prediccion
        )

        # actualizar pesos
        Pesos += Actualizacion * X_con_sesgo[
            Indice
        ]

# crear figura
plt.figure(
    figsize=(8, 6)
)

# graficar clase 0
plt.scatter(
    X[Y == 0][:, 0],
    X[Y == 0][:, 1],
    color="red",
    label="Clase 0"
)

# graficar clase 1
plt.scatter(
    X[Y == 1][:, 0],
    X[Y == 1][:, 1],
    color="blue",
    label="Clase 1"
)

# valores para linea de decision
Valores_x = np.linspace(
    -3,
    3,
    100
)

Valores_y = -(
    Pesos[0] + Pesos[1] * Valores_x
) / Pesos[2]

# graficar linea de decision
plt.plot(
    Valores_x,
    Valores_y,
    color="green",
    label="Linea de Decision"
)

# titulo
plt.title(
    "Separabilidad lineal con Perceptron"
)

# etiquetas
plt.xlabel(
    "Caracteristica 1"
)

plt.ylabel(
    "Caracteristica 2"
)

# leyenda
plt.legend()

# cuadricula
plt.grid(True)

# limites de grafica
plt.xlim(
    -3,
    3
)

plt.ylim(
    -3,
    3
)

# eje horizontal
plt.axhline(
    0,
    color="black",
    lw=0.5,
    ls="--"
)

# eje vertical
plt.axvline(
    0,
    color="black",
    lw=0.5,
    ls="--"
)

# mostrar grafica
plt.show()
