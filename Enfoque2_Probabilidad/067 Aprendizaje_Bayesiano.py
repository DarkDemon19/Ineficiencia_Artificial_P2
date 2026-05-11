# Implementa un clasificador Naive Bayes
# usando datos de ejemplo para predecir una clase

# Para calculos numericos
import numpy as np

# Para manejar datos en tabla
import pandas as pd

# Para dividir datos
from sklearn.model_selection import train_test_split

# Para crear modelo Naive Bayes
from sklearn.naive_bayes import GaussianNB

# Para calcular precision
from sklearn.metrics import accuracy_score

# datos de ejemplo
Datos = {
    "Caracteristica1": [
        1.0,
        2.0,
        1.5,
        1.2,
        2.5,
        1.8,
        2.2,
        1.0,
        1.4,
        2.0
    ],

    "Caracteristica2": [
        0.5,
        1.5,
        1.0,
        0.7,
        2.0,
        1.5,
        1.8,
        0.6,
        1.1,
        1.4
    ],

    "Clase": [
        "A",
        "B",
        "A",
        "A",
        "B",
        "B",
        "A",
        "A",
        "B",
        "B"
    ]
}

# crear dataframe
Df = pd.DataFrame(
    Datos
)

# separar caracteristicas
X = Df[
    [
        "Caracteristica1",
        "Caracteristica2"
    ]
]

# separar clase
Y = Df[
    "Clase"
]

# dividir entrenamiento y prueba
X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)

# crear modelo
Modelo = GaussianNB()

# entrenar modelo
Modelo.fit(
    X_train,
    Y_train
)

# realizar predicciones
Y_pred = Modelo.predict(
    X_test
)

# calcular precision
Precision = accuracy_score(
    Y_test,
    Y_pred
)

# mostrar predicciones
print(
    "Predicciones del modelo:",
    Y_pred
)

# mostrar precision
print(
    "Precision del modelo:",
    Precision
)