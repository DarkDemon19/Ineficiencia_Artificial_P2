# Estima la posicion de un objeto
# usando mediciones con ruido y filtro de Kalman

# Para calculos numericos
import numpy as np

# intervalo de tiempo
Dt = 1.0

# matriz de transicion
A = np.array([
    [1, Dt],
    [0, 1]
])

# matriz de observacion
H = np.array([
    [1, 0]
])

# ruido de proceso
Q = np.array([
    [1, 0],
    [0, 1]
]) * 0.001

# ruido de medicion
R = np.array([
    [1]
]) * 0.1

# estado inicial
X = np.array([
    [0],
    [1]
])

# covarianza inicial
P = np.eye(2)

def Filtro_kalman(Z):
    # usar variables globales
    global X, P

    # prediccion
    X = A @ X
    P = A @ P @ A.T + Q

    # calcular error de medicion
    Y = Z - H @ X

    # calcular incertidumbre
    S = H @ P @ H.T + R

    # calcular ganancia
    K = P @ H.T @ np.linalg.inv(S)

    # actualizar estado
    X = X + K @ Y

    # actualizar covarianza
    P = (np.eye(2) - K @ H) @ P

    return X[0, 0]

# mediciones ruidosas
Mediciones = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10
]

# guardar estimaciones
Estimaciones = []

print(
    "Estimaciones con Filtro de Kalman:"
)

for Z in Mediciones:
    Estimacion = Filtro_kalman(
        np.array([
            [Z]
        ])
    )

    Estimaciones.append(
        Estimacion
    )

    print(
        f"Medicion: {Z} -> Estimacion: {Estimacion:.2f}"
    )