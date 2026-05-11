# Simula una red neuronal simple
# realizando solo propagacion hacia adelante con ReLU

# Para calculos numericos
import numpy as np

# funcion ReLU
def Relu(X):
    return np.maximum(
        0,
        X
    )

# derivada de ReLU
def Derivada_relu(X):
    return np.where(
        X > 0,
        1,
        0
    )

class Neurona:
    def __init__(self, Numero_entradas):
        # pesos aleatorios
        self.Pesos = np.random.rand(
            Numero_entradas
        )

        # sesgo aleatorio
        self.Sesgo = np.random.rand()

    def Feedforward(self, Entrada):
        # calcular salida
        return Relu(
            np.dot(
                Entrada,
                self.Pesos
            ) + self.Sesgo
        )

class Capa:
    def __init__(self, Numero_neuronas, Numero_entradas):
        # crear neuronas
        self.Neuronas = [
            Neurona(
                Numero_entradas
            )

            for _ in range(Numero_neuronas)
        ]

    def Feedforward(self, Entrada):
        # calcular salida de toda la capa
        return np.array([
            Neurona_individual.Feedforward(
                Entrada
            )

            for Neurona_individual in self.Neuronas
        ])

# datos XOR
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

# crear capa oculta
Capa_oculta = Capa(
    Numero_neuronas=2,
    Numero_entradas=2
)

# crear capa salida
Capa_salida = Capa(
    Numero_neuronas=1,
    Numero_entradas=2
)

# mostrar resultados
print(
    "Resultados de la propagacion hacia adelante:"
)

for Entrada in X:
    # salida oculta
    Salida_oculta = Capa_oculta.Feedforward(
        Entrada
    )

    # salida final
    Salida_final = Capa_salida.Feedforward(
        Salida_oculta
    )

    print(
        f"Entrada: {Entrada}, Salida final: {Salida_final}"
    )