# Estima parametros de una mezcla de Gaussianas
# usando el algoritmo EM con datos generados

# Para calculos numericos
import numpy as np

# Para crear graficas
import matplotlib.pyplot as plt

# Para generar datos de ejemplo
from sklearn.datasets import make_blobs

# numero de muestras
Numero_muestras = 500

# numero de caracteristicas
Numero_caracteristicas = 2

# numero de clusters
Numero_clusters = 3

# generar datos
X, _ = make_blobs(
    n_samples=Numero_muestras,
    centers=Numero_clusters,
    cluster_std=0.60,
    random_state=0
)

# graficar datos
plt.scatter(
    X[:, 0],
    X[:, 1],
    s=30
)

# titulo
plt.title(
    "Datos generados"
)

# etiquetas
plt.xlabel(
    "Caracteristica 1"
)

plt.ylabel(
    "Caracteristica 2"
)

# mostrar grafica
plt.show()

def Inicializar_parametros(X, Numero_clusters):
    # obtener dimensiones
    Numero_muestras, Numero_caracteristicas = X.shape

    # inicializar medias
    Mu = X[
        np.random.choice(
            Numero_muestras,
            Numero_clusters,
            replace=False
        )
    ]

    # inicializar covarianzas
    Cov = np.array([
        np.eye(Numero_caracteristicas)
        for _ in range(Numero_clusters)
    ])

    # inicializar pesos
    Pi = np.ones(
        Numero_clusters
    ) / Numero_clusters

    return Mu, Cov, Pi

def Gaussiana_multivariada(X, Mu, Cov):
    # calcular probabilidad gaussiana
    Numero_caracteristicas = len(
        Mu
    )

    Cov_inv = np.linalg.inv(
        Cov
    )

    Diferencia = X - Mu

    Exponente = np.einsum(
        "ij,jk->i",
        Diferencia,
        np.dot(Cov_inv, Diferencia.T)
    )

    return np.exp(
        -0.5 * Exponente
    ) / np.sqrt(
        ((2 * np.pi) ** Numero_caracteristicas) *
        np.linalg.det(Cov)
    )

def EM(X, Numero_clusters, Numero_iteraciones=100):
    # obtener dimensiones
    Numero_muestras, Numero_caracteristicas = X.shape

    # iniciar parametros
    Mu, Cov, Pi = Inicializar_parametros(
        X,
        Numero_clusters
    )

    # repetir iteraciones
    for _ in range(Numero_iteraciones):

        # paso E
        Probabilidades = np.array([
            Pi[Cluster] * Gaussiana_multivariada(
                X,
                Mu[Cluster],
                Cov[Cluster]
            )
            for Cluster in range(Numero_clusters)
        ])

        Suma_probabilidades = np.sum(
            Probabilidades,
            axis=0
        )

        Suma_probabilidades[
            Suma_probabilidades == 0
        ] = 1e-10

        Gamma = Probabilidades / Suma_probabilidades

        # paso M
        N_k = np.sum(
            Gamma,
            axis=1
        )

        Mu = np.array([
            np.sum(
                Gamma[Cluster][:, np.newaxis] * X,
                axis=0
            ) / N_k[Cluster]
            for Cluster in range(Numero_clusters)
        ])

        for Cluster in range(Numero_clusters):
            Diferencia = X - Mu[Cluster]

            Cov[Cluster] = np.dot(
                Gamma[Cluster] * Diferencia.T,
                Diferencia
            ) / N_k[Cluster]

        Pi = N_k / Numero_muestras

    return Mu, Cov, Pi

# ejecutar EM
Mu, Cov, Pi = EM(
    X,
    Numero_clusters
)

# mostrar centros
print(
    "Centros de los clusters:"
)

print(
    Mu
)

# mostrar covarianzas
print(
    "\nMatrices de covarianza:"
)

print(
    Cov
)

# mostrar probabilidades
print(
    "\nProbabilidades a priori:"
)

print(
    Pi
)