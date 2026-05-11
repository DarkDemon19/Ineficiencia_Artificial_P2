# Genera un grafico de dispersion
# usando datos aleatorios con colores y tamaños variables

# Para calculos numericos
import numpy as np

# Para crear graficas
import matplotlib.pyplot as plt

# fijar semilla
np.random.seed(
    0
)

# numero de puntos
Numero_puntos = 100

# generar coordenadas X
Valores_x = np.random.rand(
    Numero_puntos
) * 100

# generar coordenadas Y
Valores_y = np.random.rand(
    Numero_puntos
) * 100

# generar colores
Colores = np.random.rand(
    Numero_puntos
)

# generar tamaños
Tamanos = np.random.rand(
    Numero_puntos
) * 100

# crear figura
plt.figure(
    figsize=(10, 6)
)

# crear grafico de dispersion
plt.scatter(
    Valores_x,
    Valores_y,
    c=Colores,
    s=Tamanos,
    alpha=0.5,
    cmap="viridis"
)

# titulo
plt.title(
    "Grafico de dispersion de datos aleatorios",
    fontsize=16
)

# etiqueta eje X
plt.xlabel(
    "Eje X",
    fontsize=14
)

# etiqueta eje Y
plt.ylabel(
    "Eje Y",
    fontsize=14
)

# cuadricula
plt.grid(True)

# barra de color
plt.colorbar(
    label="Colores"
)

# mostrar grafica
plt.show()