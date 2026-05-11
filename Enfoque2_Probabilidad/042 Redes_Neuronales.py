# Entrena una red neuronal para clasificacion binaria
# usando ReLU, sigmoide y perdida MSE

# Para crear Red Neuronal
import numpy as np

def Relu(X):
    # funcion de activacion ReLU
    return np.maximum(0, X)

def Relu_derivada(X):
    # derivada de ReLU
    return np.where(X > 0, 1, 0)

def Sigmoid(X):
    # funcion sigmoide
    return 1 / (1 + np.exp(-X))

def Sigmoid_derivada(X):
    # derivada de sigmoide
    S = Sigmoid(X)

    return S * (1 - S)

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
        self.A2 = Sigmoid(self.Z2)

        return self.A2

    def Backward(self, X, Y, Output, Lr=0.01):
        # retropropagacion
        Error_output = Output - Y
        Delta_output = Error_output * Sigmoid_derivada(self.Z2)

        Error_hidden = Delta_output.dot(self.W2.T)
        Delta_hidden = Error_hidden * Relu_derivada(self.Z1)

        # actualizar parametros
        self.W2 -= self.A1.T.dot(Delta_output) * Lr
        self.B2 -= np.sum(Delta_output, axis=0, keepdims=True) * Lr

        self.W1 -= X.T.dot(Delta_hidden) * Lr
        self.B1 -= np.sum(Delta_hidden, axis=0, keepdims=True) * Lr

    def Entrenar(self, X, Y, Epochs=1000, Lr=0.01):
        # entrenar red neuronal
        for Epoch in range(Epochs):
            Output = self.Forward(X)

            self.Backward(
                X,
                Y,
                Output,
                Lr
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