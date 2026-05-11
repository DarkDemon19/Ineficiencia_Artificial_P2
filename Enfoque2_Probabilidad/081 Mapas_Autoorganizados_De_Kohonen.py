# Implementa un mapa autoorganizado de Kohonen
# para representar patrones de datos en un espacio 2D

# Para calculos numericos
import numpy as np

# Para crear graficas
import matplotlib.pyplot as plt

class Kohonen_map:
    def __init__(
        self,
        Dimension_entrada,
        Tamano_mapa,
        Tasa_aprendizaje=0.5,
        Numero_iteraciones=100
    ):
        # guardar parametros
        self.Dimension_entrada = Dimension_entrada
        self.Tamano_mapa = Tamano_mapa
        self.Tasa_aprendizaje = Tasa_aprendizaje
        self.Numero_iteraciones = Numero_iteraciones

        # inicializar pesos
        self.Pesos = np.random.rand(
            Tamano_mapa[0],
            Tamano_mapa[1],
            Dimension_entrada
        )

    def Encontrar_bmu(self, X):
        # encontrar mejor unidad
        Bmu_indice = np.argmin(
            np.linalg.norm(
                self.Pesos - X,
                axis=2
            )
        )

        return np.unravel_index(
            Bmu_indice,
            self.Tamano_mapa
        )

    def Actualizar_pesos(self, X, Bmu_indice, Iteracion):
        # calcular tasa actual
        Tasa_actual = self.Tasa_aprendizaje * (
            1 - (
                Iteracion /
                self.Numero_iteraciones
            )
        )

        # recorrer mapa
        for I in range(self.Tamano_mapa[0]):

            for J in range(self.Tamano_mapa[1]):

                Distancia = np.linalg.norm(
                    np.array([
                        I,
                        J
                    ]) -
                    np.array(
                        Bmu_indice
                    )
                )

                # actualizar vecinos cercanos
                if Distancia <= 1:
                    self.Pesos[I, J] += Tasa_actual * (
                        X -
                        self.Pesos[I, J]
                    )

    def Entrenar(self, Datos):
        # entrenar mapa
        for Iteracion in range(self.Numero_iteraciones):

            for X in Datos:
                Bmu_indice = self.Encontrar_bmu(
                    X
                )

                self.Actualizar_pesos(
                    X,
                    Bmu_indice,
                    Iteracion
                )

    def Graficar_pesos(self):
        # mostrar pesos por dimension
        for Dimension in range(self.Dimension_entrada):

            plt.figure()

            plt.imshow(
                self.Pesos[:, :, Dimension],
                cmap="viridis"
            )

            plt.colorbar()

            plt.title(
                f"Pesos del mapa autoorganizado - Dimension {Dimension + 1}"
            )

            plt.xlabel(
                "Unidad de la red eje X"
            )

            plt.ylabel(
                "Unidad de la red eje Y"
            )

            plt.show()

# numero de muestras
Numero_muestras = 100

# generar datos
Datos = np.random.rand(
    Numero_muestras,
    2
)

# crear mapa
Som = Kohonen_map(
    Dimension_entrada=2,
    Tamano_mapa=(10, 10),
    Tasa_aprendizaje=0.5,
    Numero_iteraciones=100
)

# entrenar mapa
Som.Entrenar(
    Datos
)

# graficar pesos
Som.Graficar_pesos()

