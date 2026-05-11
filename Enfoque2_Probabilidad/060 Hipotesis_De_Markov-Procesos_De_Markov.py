# Simula un proceso de Markov con 3 estados
# genera una secuencia de cambios
# y muestra su evolucion en el tiempo

# Para calculos numericos
import numpy as np

# Para crear graficas
import matplotlib.pyplot as plt

class Proceso_de_markov:
    def __init__(self, Matriz_transicion):
        # guardar matriz de transicion
        self.Matriz_transicion = Matriz_transicion

        # numero de estados
        self.Numero_estados = Matriz_transicion.shape[0]

    def Simular(self, Estado_inicial, Numero_pasos):
        # guardar secuencia
        Estados = [
            Estado_inicial
        ]

        # estado actual
        Estado_actual = Estado_inicial

        # avanzar paso a paso
        for _ in range(Numero_pasos):

            Estado_actual = np.random.choice(
                self.Numero_estados,
                p=self.Matriz_transicion[Estado_actual]
            )

            Estados.append(
                Estado_actual
            )

        return Estados

# matriz de transicion
Matriz_transicion = np.array([
    [0.1, 0.6, 0.3],
    [0.4, 0.4, 0.2],
    [0.3, 0.3, 0.4]
])

# crear proceso
Markov = Proceso_de_markov(
    Matriz_transicion
)

# estado inicial
Estado_inicial = 0

# numero de pasos
Numero_pasos = 100

# simular proceso
Secuencia_estados = Markov.Simular(
    Estado_inicial,
    Numero_pasos
)

# crear grafica
plt.plot(
    Secuencia_estados,
    marker="o",
    linestyle="-",
    color="purple"
)

# titulo
plt.title(
    "Simulacion de proceso de Markov"
)

# etiquetas
plt.xlabel(
    "Paso"
)

plt.ylabel(
    "Estado"
)

# cuadricula
plt.grid()

# mostrar grafica
plt.show()