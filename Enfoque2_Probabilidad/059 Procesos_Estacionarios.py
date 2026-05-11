# Genera un proceso estacionario de ruido blanco
# calcula su media y varianza
# y muestra la señal en el tiempo

# Para calculos numericos
import numpy as np

# Para crear graficas
import matplotlib.pyplot as plt

# numero de muestras
Numero_muestras = 1000

# media del proceso
Media = 0

# desviacion estandar
Desviacion_estandar = 1

# generar ruido blanco
Ruido_blanco = np.random.normal(
    Media,
    Desviacion_estandar,
    Numero_muestras
)

# crear grafica
plt.plot(
    Ruido_blanco,
    color="blue",
    alpha=0.7,
    label="Ruido Blanco"
)

# titulo
plt.title(
    "Proceso estacionario - Ruido blanco"
)

# etiquetas
plt.xlabel(
    "Tiempo"
)

plt.ylabel(
    "Valor"
)

# cuadricula
plt.grid()

# leyenda
plt.legend()

# mostrar grafica
plt.show()

# calcular media
Media_calculada = np.mean(
    Ruido_blanco
)

# calcular varianza
Varianza_calculada = np.var(
    Ruido_blanco
)

# mostrar resultados
print(
    f"Media calculada: {Media_calculada:.2f}"
)

print(
    f"Varianza calculada: {Varianza_calculada:.2f}"
)