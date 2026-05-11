# Implementa un perceptron simple para clasificar
# dos clases en datos 2D y mostrar la linea de decision

# Para calculos numericos
import numpy as np

# Para crear graficas
import matplotlib.pyplot as plt

# fijar semilla
np.random.seed(
    0
)

# numero de muestras
Numero_muestras = 100

# generar puntos aleatorios
X = np.random.randn(
    Numero_muestras,
    2
)

# generar clases
Y = np.array([
    1 if Valor[0] + Valor[1] > 0 else 0

    for Valor in X
])

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

    for Indice in range(Numero_muestras):

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

# graficar linea
plt.plot(
    Valores_x,
    Valores_y,
    color="green",
    label="Linea de Decision"
)

# titulo
plt.title(
    "Perceptron Clasificacion de dos clases"
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

# mostrar grafica
plt.show()
