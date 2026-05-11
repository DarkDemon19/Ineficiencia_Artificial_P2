# Estima la posicion de un objeto
# usando un filtro de particulas con mediciones ruidosas

# Para calculos numericos
import numpy as np

class Filtrado_particulas:
    def __init__(self, Numero_particulas, Rango, Ruido_movimiento, Ruido_medicion):
        # guardar parametros
        self.Numero_particulas = Numero_particulas
        self.Ruido_movimiento = Ruido_movimiento
        self.Ruido_medicion = Ruido_medicion

        # crear particulas iniciales
        self.Particulas = np.random.uniform(
            -Rango,
            Rango,
            Numero_particulas
        )

    def Predecir(self, Movimiento):
        # mover particulas con ruido
        self.Particulas += Movimiento + np.random.normal(
            0,
            self.Ruido_movimiento,
            self.Numero_particulas
        )

    def Actualizar(self, Medicion):
        # calcular pesos
        Pesos = (
            1 /
            (np.sqrt(2 * np.pi) * self.Ruido_medicion)
        ) * np.exp(
            -0.5 *
            (
                (self.Particulas - Medicion) /
                self.Ruido_medicion
            ) ** 2
        )

        # normalizar pesos
        Pesos /= np.sum(
            Pesos
        )

        # remuestrear particulas
        Indices = np.random.choice(
            range(self.Numero_particulas),
            size=self.Numero_particulas,
            p=Pesos
        )

        self.Particulas = self.Particulas[
            Indices
        ]

    def Estimar(self):
        # calcular promedio de particulas
        return np.mean(
            self.Particulas
        )

# numero de particulas
Numero_particulas = 1000

# rango inicial
Rango = 10

# ruido de movimiento
Ruido_movimiento = 1.0

# ruido de medicion
Ruido_medicion = 2.0

# crear filtro
Filtro = Filtrado_particulas(
    Numero_particulas,
    Rango,
    Ruido_movimiento,
    Ruido_medicion
)

# movimientos del objeto
Movimientos = [
    1,
    1,
    1,
    1,
    1
]

# mediciones obtenidas
Mediciones = [
    1.2,
    2.8,
    4.1,
    5.9,
    7.5
]

print(
    "Estimaciones con Filtrado de Particulas:"
)

for Indice, Datos in enumerate(zip(Movimientos, Mediciones)):
    Movimiento, Medicion = Datos

    Filtro.Predecir(
        Movimiento
    )

    Filtro.Actualizar(
        Medicion
    )

    Estimacion = Filtro.Estimar()

    print(
        f"Paso {Indice + 1} -> Movimiento: {Movimiento}, Medicion: {Medicion:.2f}, Estimacion: {Estimacion:.2f}"
    )