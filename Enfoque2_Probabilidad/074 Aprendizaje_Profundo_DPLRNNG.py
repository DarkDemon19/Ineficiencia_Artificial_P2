# Entrena una red neuronal simple para aprender XOR
# usando ReLU en capa oculta y Sigmoid en salida

# Para calculos numericos
import numpy as np

# funcion ReLU
def Relu(X):
    return np.maximum(
        0,
        X
    )

# derivada de ReLU
def Relu_derivada(X):
    return np.where(
        X > 0,
        1,
        0
    )

class Red_neuronal:
    def __init__(self, Entrada, Oculta, Salida):
        # inicializar pesos entrada a oculta
        self.W1 = np.random.rand(
            Entrada,
            Oculta
        ) * 0.01

        # sesgo capa oculta
        self.B1 = np.zeros(
            (
                1,
                Oculta
            )
        )

        # pesos oculta a salida
        self.W2 = np.random.rand(
            Oculta,
            Salida
        ) * 0.01

        # sesgo salida
        self.B2 = np.zeros(
            (
                1,
                Salida
            )
        )

    def Sigmoid(self, X):
        # funcion Sigmoid
        return 1 / (
            1 + np.exp(-X)
        )

    def Forward(self, X):
        # capa oculta
        self.Z1 = np.dot(
            X,
            self.W1
        ) + self.B1

        self.A1 = Relu(
            self.Z1
        )

        # capa salida
        self.Z2 = np.dot(
            self.A1,
            self.W2
        ) + self.B2

        return self.Sigmoid(
            self.Z2
        )

    def Backward(self, X, Y, Output):
        # error salida
        Error_salida = Output - Y

        # delta salida
        Delta_salida = Error_salida * Output * (
            1 - Output
        )

        # error oculto
        Error_oculto = Delta_salida.dot(
            self.W2.T
        )

        # delta oculto
        Delta_oculto = Error_oculto * Relu_derivada(
            self.Z1
        )

        # actualizar pesos salida
        self.W2 -= self.A1.T.dot(
            Delta_salida
        ) * 0.01

        # actualizar sesgo salida
        self.B2 -= np.sum(
            Delta_salida,
            axis=0,
            keepdims=True
        ) * 0.01

        # actualizar pesos entrada
        self.W1 -= X.T.dot(
            Delta_oculto
        ) * 0.01

        # actualizar sesgo oculto
        self.B1 -= np.sum(
            Delta_oculto,
            axis=0,
            keepdims=True
        ) * 0.01

    def Entrenar(self, X, Y, Epochs=1000):
        # entrenar red
        for Epoch in range(Epochs):

            Output = self.Forward(
                X
            )

            self.Backward(
                X,
                Y,
                Output
            )

            # mostrar error
            if Epoch % 100 == 0:
                Loss = np.mean(
                    np.square(
                        Y - Output
                    )
                )

                print(
                    f"Epoch {Epoch}, Loss: {Loss:.4f}"
                )

# datos XOR
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

Y = np.array([
    [0],
    [1],
    [1],
    [0]
])

# crear red
Red = Red_neuronal(
    Entrada=2,
    Oculta=2,
    Salida=1
)

# entrenar red
Red.Entrenar(
    X,
    Y
)

# obtener predicciones
Predicciones = Red.Forward(
    X
)

# mostrar resultado
print(
    "Predicciones despues del entrenamiento:"
)

print(
    Predicciones
)