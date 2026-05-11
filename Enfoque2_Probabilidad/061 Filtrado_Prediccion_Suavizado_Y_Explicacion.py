# Simula un sistema dinamico con ruido
# filtra observaciones y estima el estado real

# Para calculos numericos
import numpy as np

# Para crear graficas
import matplotlib.pyplot as plt

# numero de pasos
Numero_pasos = 50

# arreglos del sistema
Estado_real = np.zeros(
    Numero_pasos
)

Estado_filtrado = np.zeros(
    Numero_pasos
)

Observaciones = np.zeros(
    Numero_pasos
)

# ruido del proceso
Ruido_proceso = 0.5

# ruido de observacion
Ruido_observacion = 1.0

# prediccion inicial
Prediccion_estado = 0.0

# error inicial
Prediccion_error = 1.0

# calcular factor de ganancia
Factor_ganancia = Prediccion_error / (
    Prediccion_error +
    Ruido_observacion
)

# simular sistema dinamico
for Tiempo in range(1, Numero_pasos):

    # generar estado real
    Estado_real[Tiempo] = Estado_real[Tiempo - 1] + np.random.normal(
        0,
        Ruido_proceso
    )

    # generar observacion con ruido
    Observaciones[Tiempo] = Estado_real[Tiempo] + np.random.normal(
        0,
        Ruido_observacion
    )

    # filtrar estado
    Estado_filtrado[Tiempo] = Prediccion_estado + Factor_ganancia * (
        Observaciones[Tiempo] -
        Prediccion_estado
    )

    # actualizar prediccion
    Prediccion_estado = Estado_filtrado[Tiempo]

    # actualizar error
    Prediccion_error = (
        (1 - Factor_ganancia) *
        Prediccion_error +
        Ruido_proceso
    )

# graficar estado real
plt.plot(
    Estado_real,
    label="Estado Real",
    color="green"
)

# graficar observaciones
plt.plot(
    Observaciones,
    label="Observaciones",
    color="red",
    linestyle="dotted"
)

# graficar estado filtrado
plt.plot(
    Estado_filtrado,
    label="Estado Filtrado",
    color="blue"
)

# titulo
plt.title(
    "Filtrado y prediccion en un sistema dinamico"
)

# etiquetas
plt.xlabel(
    "Tiempo"
)

plt.ylabel(
    "Valor del Estado"
)

# leyenda
plt.legend()

# cuadricula
plt.grid()

# mostrar grafica
plt.show()