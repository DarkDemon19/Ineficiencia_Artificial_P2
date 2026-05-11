# Genera datos sinteticos y aplica K-means
# para agrupar puntos y mostrar sus centros

# Para calculos numericos
import numpy as np

# Para crear graficas
import matplotlib.pyplot as plt

# Para generar datos de ejemplo
from sklearn.datasets import make_blobs

# Para aplicar K-means
from sklearn.cluster import KMeans

# numero de muestras
Numero_muestras = 300

# numero de caracteristicas
Numero_caracteristicas = 2

# numero de clusters
Numero_clusters = 4

# generar datos
X, _ = make_blobs(
    n_samples=Numero_muestras,
    centers=Numero_clusters,
    cluster_std=0.60,
    random_state=42
)

# graficar datos originales
plt.scatter(
    X[:, 0],
    X[:, 1],
    s=30,
    alpha=0.5
)

# titulo
plt.title(
    "Datos generados para agrupamiento"
)

# etiquetas
plt.xlabel(
    "Caracteristica 1"
)

plt.ylabel(
    "Caracteristica 2"
)

# cuadricula
plt.grid(True)

# mostrar grafica
plt.show()

# crear modelo K-means
Kmeans = KMeans(
    n_clusters=Numero_clusters,
    random_state=42
)

# entrenar modelo
Kmeans.fit(
    X
)

# obtener etiquetas
Labels = Kmeans.labels_

# obtener centros
Centros = Kmeans.cluster_centers_

# graficar clusters
plt.scatter(
    X[:, 0],
    X[:, 1],
    c=Labels,
    s=30,
    cmap="viridis",
    alpha=0.5
)

# graficar centros
plt.scatter(
    Centros[:, 0],
    Centros[:, 1],
    c="red",
    s=200,
    marker="X",
    label="Centros de Clusters"
)

# titulo
plt.title(
    "Resultado del agrupamiento K-means"
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

# mostrar centros
print(
    "Centros de los clusters:"
)

print(
    Centros
)