# Muestra la probabilidad de obtener diferentes cantidades de caras
# despues de varios lanzamientos de moneda con distribucion binomial

# Para mostrar Distribucion binomial
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# numero de intentos realizados
Numero_lanzamientos = 10

# probabilidad de exito
Probabilidad_exito = 0.5

# posibles resultados
Valores_x = np.arange(
    0,
    Numero_lanzamientos + 1
)

# calcular probabilidades
Probabilidades = binom.pmf(
    Valores_x,
    Numero_lanzamientos,
    Probabilidad_exito
)

# crear grafica
plt.figure(
    figsize=(10, 6)
)

# graficar los valores obtenidos
plt.stem(
    Valores_x,
    Probabilidades,
    basefmt=" ",
    use_line_collection=True
)

# etiquetas del grafico
plt.xlabel("Numero de exitos")
plt.ylabel("Probabilidad")

# titulo del grafico
plt.title(
    "Distribucion binomial"
)

# cuadricula
plt.grid(True)

# mostrar tabla o grafo
plt.show()