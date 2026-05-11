# Entrena una red neuronal simple
# para aprender la funcion XOR usando ReLU

# Para crear Red Neuronal
import numpy as np

def Relu(X):
    # funcion de activacion ReLU
    return np.maximum(0, X)

def Relu_derivada(X):
    # derivada de ReLU
    return np.where(X > 0, 1, 0)

class Red_neuronal:
    def __init__(self, Input_size, Hidden_size, Output_size):
        # iniciar pesos y sesgos
        self.W1 = np.random.rand(Input_size, Hidden_size) * 0.01
        self.B1 = np.zeros((1, Hidden_size))

        self.W2 = np.random.rand(Hidden_size, Output_size) * 0.01
        self.B2 = np.zeros((1, Output_size))

    def Forward(self, X):
        # propagacion hacia adelante
        self.Z1 = np.dot(X, self.W1) + self.B1
        self.A1 = Relu(self.Z1)

        self.Z2 = np.dot(self.A1, self.W2) + self.B2

        return self.Sigmoid(self.Z2)

    def Sigmoid(self, X):
        # salida entre 0 y 1
        return 1 / (1 + np.exp(-X))

    def Backward(self, X, Y, Output):
        # calcular error de salida
        Output_error = Output - Y
        Output_delta = Output_error * Output * (1 - Output)

        # calcular error oculto
        Hidden_error = Output_delta.dot(self.W2.T)
        Hidden_delta = Hidden_error * Relu_derivada(self.Z1)

        # actualizar parametros
        self.W2 -= self.A1.T.dot(Output_delta) * 0.01
        self.B2 -= np.sum(Output_delta, axis=0, keepdims=True) * 0.01

        self.W1 -= X.T.dot(Hidden_delta) * 0.01
        self.B1 -= np.sum(Hidden_delta, axis=0, keepdims=True) * 0.01

    def Entrenar(self, X, Y, Epochs=1000):
        # entrenar red neuronal
        for Epoch in range(Epochs):
            Output = self.Forward(X)

            self.Backward(
                X,
                Y,
                Output
            )

            if Epoch % 100 == 0:
                Loss = np.mean(
                    np.square(Y - Output)
                )

                print(
                    f"Epoch {Epoch}, Loss: {Loss}"
                )

# datos de entrada XOR
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

# salidas esperadas
Y = np.array([
    [0],
    [1],
    [1],
    [0]
])

# crear red neuronal
Red = Red_neuronal(
    Input_size=2,
    Hidden_size=2,
    Output_size=1
)

# entrenar red neuronal
Red.Entrenar(
    X,
    Y
)

# realizar predicciones
Predicciones = Red.Forward(X)

print("\nPredicciones despues del entrenamiento:")
print(Predicciones)