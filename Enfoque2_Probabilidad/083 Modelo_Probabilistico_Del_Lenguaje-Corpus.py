# Implementa un modelo de lenguaje con bigramas
# para predecir la siguiente palabra de un texto

# Para calculos numericos
import numpy as np

# Para crear diccionarios anidados
from collections import defaultdict

class Ngram_language_model:
    def __init__(self, N):
        # guardar valor de n
        self.N = N

        # guardar ngramas
        self.Ngramas = defaultdict(
            lambda: defaultdict(int)
        )

        # guardar vocabulario
        self.Vocabulario = set()

    def Entrenar(self, Texto):
        # separar texto en palabras
        Tokens = Texto.lower().split()

        # guardar palabras unicas
        self.Vocabulario.update(
            Tokens
        )

        # generar ngramas
        for Indice in range(len(Tokens) - self.N + 1):

            Ngrama = tuple(
                Tokens[
                    Indice:
                    Indice + self.N
                ]
            )

            Prefijo = Ngrama[:-1]

            self.Ngramas[Prefijo][Ngrama[-1]] += 1

    def Predecir(self, Prefijo):
        # convertir prefijo
        Prefijo = tuple(
            Prefijo.lower().split()
        )

        # validar tamaño del prefijo
        if len(Prefijo) != self.N - 1:
            raise ValueError(
                f"El prefijo debe tener {self.N - 1} palabras."
            )

        # obtener conteos
        Conteos_siguiente = self.Ngramas[
            Prefijo
        ]

        # validar si hay prediccion
        if not Conteos_siguiente:
            return None

        # total de apariciones
        Total_conteo = sum(
            Conteos_siguiente.values()
        )

        # calcular probabilidades
        Probabilidades = {
            Palabra: Conteo / Total_conteo
            for Palabra, Conteo in Conteos_siguiente.items()
        }

        # elegir palabra mas probable
        Palabra_predicha = max(
            Probabilidades,
            key=Probabilidades.get
        )

        return Palabra_predicha, Probabilidades[Palabra_predicha]

# texto de entrenamiento
Texto_corpus = """
La inteligencia artificial es una rama de la informatica.
La inteligencia artificial busca crear sistemas que imiten la inteligencia humana.
Los modelos de lenguaje son una parte importante de la inteligencia artificial.
"""

# crear modelo n-grama
Modelo_ngram = Ngram_language_model(
    N=2
)

# entrenar modelo
Modelo_ngram.Entrenar(
    Texto_corpus
)

# prefijo de prueba
Prefijo = "la"

# predecir palabra
Prediccion, Probabilidad = Modelo_ngram.Predecir(
    Prefijo
)

# mostrar resultado
print(
    f"Prediccion para '{Prefijo}': {Prediccion} Probabilidad: {Probabilidad:.4f}"
)