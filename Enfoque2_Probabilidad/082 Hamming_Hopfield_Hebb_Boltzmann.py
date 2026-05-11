# Implementa una red de Hopfield
# para almacenar y recordar patrones perturbados

# Para calculos numericos
import numpy as np

# Para crear graficas
import matplotlib.pyplot as plt

class Hopfield_network:
    def __init__(self, Tamano):
        # guardar tamaño
        self.Tamano = Tamano

        # inicializar pesos
        self.Pesos = np.zeros(
            (
                Tamano,
                Tamano
            )
        )

    def Entrenar(self, Patrones):
        # entrenar con regla de Hebb
        for Patron in Patrones:
            Patron = Patron.reshape(
                self.Tamano,
                1
            )

            self.Pesos += np.dot(
                Patron,
                Patron.T
            )

        # eliminar auto conexion
        np.fill_diagonal(
            self.Pesos,
            0
        )

    def Recordar(self, Patron, Pasos=5):
        # recordar patron
        Estado = Patron.copy()

        for _ in range(Pasos):

            for Indice in range(self.Tamano):
                Entrada_neta = np.dot(
                    self.Pesos[Indice],
                    Estado
                )

                if Entrada_neta > 0:
                    Estado[Indice] = 1

                else:
                    Estado[Indice] = -1

        return Estado

    def Energia(self, Estado):
        # calcular energia del estado
        return -0.5 * np.dot(
            Estado.T,
            np.dot(
                self.Pesos,
                Estado
            )
        )

# patrones de ejemplo
Patrones = np.array([
    [1, 1, -1, -1],
    [-1, -1, 1, 1],
    [1, -1, 1, -1]
])

# crear red
Red_hopfield = Hopfield_network(
    Tamano=4
)

# entrenar red
Red_hopfield.Entrenar(
    Patrones
)

# patron perturbado
Patron_prueba = np.array([
    1,
    -1,
    -1,
    -1
])

# recordar patron
Patron_recordado = Red_hopfield.Recordar(
    Patron_prueba
)

# mostrar patrones
print(
    "Patron de prueba:",
    Patron_prueba
)

print(
    "Patron recordado:",
    Patron_recordado
)

# calcular energia original
Energia_original = Red_hopfield.Energia(
    Patron_prueba
)

# calcular energia recordada
Energia_recordada = Red_hopfield.Energia(
    Patron_recordado
)

# mostrar energia
print(
    "Energia del patron original:",
    Energia_original
)

print(
    "Energia del patron recordado:",
    Energia_recordada
)
