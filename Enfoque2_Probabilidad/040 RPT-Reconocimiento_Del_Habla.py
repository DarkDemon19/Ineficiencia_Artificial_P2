# Simula el reconocimiento de palabras
# relacionando una palabra con su significado

# Para reconocer palabras habladas
import random
import time

# palabras disponibles
Palabras_habladas = [
    ("hola", "saludo"),
    ("adios", "despedida"),
    ("gracias", "agradecimiento"),
    ("perdon", "disculpa"),
    ("si", "afirmacion"),
    ("no", "negacion")
]

def Reconocer_habla(Entrada_habla):
    # reconocer palabra ingresada
    print("\nReconociendo palabra...")

    time.sleep(1)

    for Palabra, Interpretacion in Palabras_habladas:
        if Entrada_habla == Palabra:
            print(
                f"Palabra '{Entrada_habla}' reconocida como: {Interpretacion}"
            )

            return Interpretacion

    # palabra no encontrada
    print(
        f"Palabra '{Entrada_habla}' no reconocida."
    )

    return "no reconocida"

def Seleccionar_palabra():
    # seleccionar palabra
    Opciones = [
        Palabra for Palabra, _ in Palabras_habladas
    ]

    Opciones.append("aleatoria")

    print(
        "Selecciona una palabra o elige 'aleatoria':"
    )

    for Indice, Opcion in enumerate(Opciones, 1):
        print(
            f"{Indice}. {Opcion}"
        )

    Eleccion = input(
        "Escribe el numero de tu eleccion: "
    )

    # validar eleccion
    if Eleccion.isdigit() and 1 <= int(Eleccion) <= len(Opciones):

        if Opciones[int(Eleccion) - 1] == "aleatoria":
            Palabra_hablada = random.choice(
                Opciones[:-1]
            )

        else:
            Palabra_hablada = Opciones[
                int(Eleccion) - 1
            ]

    else:
        print(
            "Eleccion no valida. Seleccionando palabra aleatoria..."
        )

        Palabra_hablada = random.choice(
            Opciones[:-1]
        )

    return Palabra_hablada

# seleccion principal
Palabra_hablada = Seleccionar_palabra()

print(
    "Palabra seleccionada:",
    Palabra_hablada
)

# reconocimiento final
Resultado = Reconocer_habla(
    Palabra_hablada
)

print(
    "Interpretacion final:",
    Resultado
)