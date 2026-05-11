# Implementa una gramatica libre de contexto probabilistica
# para generar oraciones aleatorias segun reglas definidas

# Para seleccion aleatoria
import random

class Pcfg:
    def __init__(self):
        # definir reglas probabilisticas
        self.Producciones = {
            "S": [
                (
                    ["NP", "VP"],
                    0.9
                ),
                (
                    ["VP"],
                    0.1
                )
            ],

            "NP": [
                (
                    ["Det", "N"],
                    1.0
                )
            ],

            "VP": [
                (
                    ["V", "NP"],
                    0.5
                ),
                (
                    ["V"],
                    0.5
                )
            ],

            "Det": [
                (
                    ["el"],
                    0.5
                ),
                (
                    ["la"],
                    0.5
                )
            ],

            "N": [
                (
                    ["gato"],
                    0.5
                ),
                (
                    ["perro"],
                    0.5
                )
            ],

            "V": [
                (
                    ["come"],
                    0.5
                ),
                (
                    ["ve"],
                    0.5
                )
            ]
        }

    def Generar_oracion(self, Simbolo="S"):
        # si es terminal
        if Simbolo not in self.Producciones:
            return Simbolo

        # obtener producciones posibles
        Producciones_disponibles = self.Producciones[
            Simbolo
        ]

        # separar reglas y probabilidades
        Reglas, Probabilidades = zip(
            *Producciones_disponibles
        )

        # elegir regla
        Seleccion = random.choices(
            Reglas,
            weights=Probabilidades,
            k=1
        )[0]

        # construir oracion
        return " ".join(
            self.Generar_oracion(
                Subsimbolo
            )

            for Subsimbolo in Seleccion
        )

# crear instancia
Modelo_pcfg = Pcfg()

# generar oracion
Oracion_generada = Modelo_pcfg.Generar_oracion()

# mostrar resultado
print(
    "Oracion generada:",
    Oracion_generada
)