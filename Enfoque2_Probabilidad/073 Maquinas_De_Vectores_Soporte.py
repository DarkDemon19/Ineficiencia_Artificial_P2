# Implementa un clasificador SVM con kernel RBF
# usando datos sinteticos tipo media luna

# Para calculos numericos
import numpy as np

# Para crear graficas
import matplotlib.pyplot as plt

# Para generar datos tipo moons
from sklearn.datasets import make_moons

# Para dividir datos
from sklearn.model_selection import train_test_split

# Para modelo SVM
from sklearn.svm import SVC

# generar datos con ruido
X, Y = make_moons(
    n_samples=300,
    noise=0.2,
    random_state=42
)

# dividir datos
X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)

# crear modelo SVM
Svm_modelo = SVC(
    kernel="rbf",
    gamma="scale"
)

# entrenar modelo
Svm_modelo.fit(
    X_train,
    Y_train
)

# realizar predicciones
Predicciones = Svm_modelo.predict(
    X_test
)

# crear grafica
plt.figure(
    figsize=(8, 6)
)

# mostrar clasificacion
plt.scatter(
    X_test[:, 0],
    X_test[:, 1],
    c=Predicciones,
    cmap="viridis",
    edgecolor="k",
    s=50
)

# titulo
plt.title(
    "Clasificacion usando SVM con Kernel RBF"
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

# calcular precision
Precision = Svm_modelo.score(
    X_test,
    Y_test
)

# mostrar resultado
print(
    f"Precision del modelo: {Precision:.2f}"
)