# Realiza clasificacion con k-NN
# y agrupamiento con k-means usando datos sinteticos

# Para calculos numericos
import numpy as np

# Para crear graficas
import matplotlib.pyplot as plt

# Para generar datos de ejemplo
from sklearn.datasets import make_blobs

# Para dividir datos
from sklearn.model_selection import train_test_split

# Para clasificacion k-NN
from sklearn.neighbors import KNeighborsClassifier

# Para agrupamiento k-means
from sklearn.cluster import KMeans

# numero de muestras
Numero_muestras = 300

# numero de caracteristicas
Numero_caracteristicas = 2

# numero de clusters
Numero_clusters = 3

# generar datos
X, Y = make_blobs(
    n_samples=Numero_muestras,
    centers=Numero_clusters,
    cluster_std=0.60,
    random_state=0
)

# dividir datos
X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)

# valor de vecinos
K = 3

# crear modelo k-NN
Knn = KNeighborsClassifier(
    n_neighbors=K
)

# entrenar modelo k-NN
Knn.fit(
    X_train,
    Y_train
)

# realizar predicciones
Predicciones = Knn.predict(
    X_test
)

# crear figura
plt.figure(
    figsize=(12, 6)
)

# grafica de k-NN
plt.subplot(
    1,
    2,
    1
)

plt.scatter(
    X_test[:, 0],
    X_test[:, 1],
    c=Predicciones,
    cmap="viridis",
    edgecolor="k",
    s=50
)

# titulo k-NN
plt.title(
    f"Clasificacion usando k-NN K={K}"
)

# etiquetas k-NN
plt.xlabel(
    "Caracteristica 1"
)

plt.ylabel(
    "Caracteristica 2"
)

# crear modelo k-means
Kmeans = KMeans(
    n_clusters=Numero_clusters
)

# entrenar modelo k-means
Kmeans.fit(
    X
)

# obtener centros
Centros = Kmeans.cluster_centers_

# grafica de k-means
plt.subplot(
    1,
    2,
    2
)

plt.scatter(
    X[:, 0],
    X[:, 1],
    c=Kmeans.labels_,
    cmap="viridis",
    edgecolor="k",
    s=50
)

# graficar centros
plt.scatter(
    Centros[:, 0],
    Centros[:, 1],
    c="red",
    s=200,
    marker="X",
    label="Centros"
)

# titulo k-means
plt.title(
    "Clustering usando k-means"
)

# etiquetas k-means
plt.xlabel(
    "Caracteristica 1"
)

plt.ylabel(
    "Caracteristica 2"
)

# leyenda
plt.legend()

# ajustar grafica
plt.tight_layout()

# mostrar grafica
plt.show()