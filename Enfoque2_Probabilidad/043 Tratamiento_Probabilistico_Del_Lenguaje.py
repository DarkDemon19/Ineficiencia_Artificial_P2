# Analiza un corpus de noticias
# para encontrar palabras comunes y predecir palabras siguientes

# Para analizar texto con NLTK
import nltk
from nltk.corpus import brown
from nltk.probability import FreqDist, ConditionalFreqDist

# descargar recursos necesarios
nltk.download("brown")
nltk.download("punkt")

# obtener palabras del corpus de noticias
Corpus = brown.words(
    categories="news"
)

# calcular frecuencia de palabras
Frecuencia = FreqDist(
    Corpus
)

print("10 palabras mas comunes en el corpus:")

for Palabra, Cantidad in Frecuencia.most_common(10):
    print(
        f"{Palabra}: {Cantidad}"
    )

# crear bigramas
Bigramas = nltk.bigrams(
    Corpus
)

# calcular frecuencia condicional
Frecuencia_condicional = ConditionalFreqDist(
    Bigramas
)

def Predecir_siguiente(Palabra_actual, Numero=3):
    # predecir palabras siguientes
    Palabra_actual = Palabra_actual.lower()

    if Palabra_actual in Frecuencia_condicional:
        Palabras_probables = Frecuencia_condicional[
            Palabra_actual
        ].most_common(Numero)

        print(
            f"\nPalabras mas probables despues de '{Palabra_actual}':"
        )

        for Palabra, Cantidad in Palabras_probables:
            print(
                f"{Palabra}: {Cantidad}"
            )

    else:
        print(
            f"\nNo se encontraron predicciones para '{Palabra_actual}'."
        )

# ejemplo de prediccion
Predecir_siguiente(
    "the"
)