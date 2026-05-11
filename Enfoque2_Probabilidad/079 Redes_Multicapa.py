# Implementa una red neuronal multicapa
# para clasificar datos sinteticos tipo moons

# Para calculos numericos
import numpy as np

# Para crear graficas
import matplotlib.pyplot as plt

# Para generar datos tipo moons
from sklearn.datasets import make_moons

# Para dividir datos
from sklearn.model_selection import train_test_split

# Para normalizar datos
from sklearn.preprocessing import StandardScaler

# Para crear red neuronal
from tensorflow import keras
from tensorflow.keras import layers

# generar datos
X, Y = make_moons(
    n_samples=1000,
    noise=0.1,
    random_state=42
)

# dividir datos
X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)

# crear normalizador
Scaler = StandardScaler()

# normalizar entrenamiento
X_train = Scaler.fit_transform(
    X_train
)

# normalizar prueba
X_test = Scaler.transform(
    X_test
)

# crear modelo
Modelo = keras.Sequential([
    layers.Dense(
        8,
        activation="relu",
        input_shape=(2,)
    ),

    layers.Dense(
        4,
        activation="relu"
    ),

    layers.Dense(
        1,
        activation="sigmoid"
    )
])

# compilar modelo
Modelo.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

# entrenar modelo
Historial = Modelo.fit(
    X_train,
    Y_train,
    epochs=100,
    batch_size=10,
    validation_split=0.2
)

# evaluar modelo
Loss, Precision = Modelo.evaluate(
    X_test,
    Y_test
)

# mostrar precision
print(
    f"Precision del modelo en conjunto de prueba: {Precision:.2f}"
)

# crear figura
plt.figure(
    figsize=(12, 4)
)

# grafica de perdida
plt.subplot(
    1,
    2,
    1
)

plt.plot(
    Historial.history["loss"],
    label="Loss"
)

plt.plot(
    Historial.history["val_loss"],
    label="Val Loss"
)

plt.title(
    "Perdida durante el entrenamiento"
)

plt.xlabel(
    "Epocas"
)

plt.ylabel(
    "Perdida"
)

plt.legend()

# grafica de precision
plt.subplot(
    1,
    2,
    2
)

plt.plot(
    Historial.history["accuracy"],
    label="Accuracy"
)

plt.plot(
    Historial.history["val_accuracy"],
    label="Val Accuracy"
)

plt.title(
    "Precision durante el entrenamiento"
)

plt.xlabel(
    "Epocas"
)

plt.ylabel(
    "Precision"
)

plt.legend()

# ajustar grafica
plt.tight_layout()

# mostrar grafica
plt.show()

