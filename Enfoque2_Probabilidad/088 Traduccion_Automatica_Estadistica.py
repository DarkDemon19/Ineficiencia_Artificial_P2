# Implementa un traductor estadistico simple
# usando un diccionario para traducir palabra por palabra

class Traductor_estadistico:
    def __init__(self):
        # diccionario de traduccion
        self.Diccionario = {
            "hola": "hello",
            "adios": "goodbye",
            "gracias": "thank you",
            "por favor": "please",
            "si": "yes",
            "no": "no"
        }

    def Traducir(self, Frase):
        # dividir frase
        Palabras = Frase.split()

        # guardar traduccion
        Traduccion = []

        # recorrer palabras
        for Palabra in Palabras:

            # traducir si existe
            Traduccion.append(
                self.Diccionario.get(
                    Palabra.lower(),
                    Palabra
                )
            )

        # unir traduccion
        return " ".join(
            Traduccion
        )

# crear traductor
Traductor = Traductor_estadistico()

# frase original
Frase_original = "hola gracias por favor"

# traducir frase
Frase_traducida = Traductor.Traducir(
    Frase_original
)

# mostrar frase original
print(
    "Frase original:",
    Frase_original
)

# mostrar frase traducida
print(
    "Frase traducida:",
    Frase_traducida
)