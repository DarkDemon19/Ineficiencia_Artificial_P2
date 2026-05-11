# Genera oraciones con una gramatica probabilistica lexicalizada
# eligiendo reglas segun sus probabilidades

# Para seleccion aleatoria
import random

class Lexicalized_pcfg:
    def __init__(self):
        # definir gramatica lexicalizada
        self.Gramatica = {
            "S": [
                (
                    "NP VP",
                    1.0
                )
            ],

            "NP": [
                (
                    "Det Noun",
                    0.7
                ),
                (
                    "Adj Noun",
                    0.3
                )
            ],

            "VP": [
                (
                    "Verb NP",
                    1.0
                )
            ],

            "Det": [
                (
                    "el",
                    0.5
                ),
                (
                    "la",
                    0.5
                )
            ],

            "Adj": [
                (
                    "rapido",
                    0.6
                ),
                (
                    "lento",
                    0.4
                )
            ],

            "Noun": [
                (
                    "perro",
                    0.4
                ),
                (
                    "gato",
                    0.4
                ),
                (
                    "pajaro",
                    0.2
                )
            ],

            "Verb": [
                (
                    "corre",
                    0.7
                ),
                (
                    "salta",
                    0.3
                )
            ]
        }

    def Generar_oracion(self, Simbolo="S"):
        # si es terminal
        if Simbolo not in self.Gramatica:
            return Simbolo

        # obtener producciones
        Producciones = self.Gramatica[
            Simbolo
        ]

        # calcular probabilidad total
        Total_probabilidad = sum(
            Probabilidad
            for _, Probabilidad in Producciones
        )

        # generar valor aleatorio
        Valor_aleatorio = random.uniform(
            0,
            Total_probabilidad
        )

        Acumulado = 0

        # elegir produccion
        for Produccion, Probabilidad in Producciones:
            Acumulado += Probabilidad

            if Valor_aleatorio <= Acumulado:
                return " ".join(
                    self.Generar_oracion(
                        Subsimbolo
                    )

                    for Subsimbolo in Produccion.split()
                )

# crear instancia
Modelo_lexicalizado = Lexicalized_pcfg()

# generar oracion
Oracion_generada = Modelo_lexicalizado.Generar_oracion()

# mostrar resultado
print(
    "Oracion generada:",
    Oracion_generada
)