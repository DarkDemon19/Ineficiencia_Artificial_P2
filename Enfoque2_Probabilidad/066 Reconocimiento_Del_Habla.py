# Simula un sistema basico de reconocimiento de palabras
# permite elegir una palabra y mostrar su interpretacion

# Para elegir opciones aleatorias
import random

# Para simular tiempo de procesamiento
import time

# lista de palabras y significado
Palabras_habladas = [
    ("hola", "saludo"),
    ("adios", "despedida"),
    ("gracias", "agradecimiento"),
    ("perdon", "disculpa"),
    ("si", "afirmacion"),
    ("no", "negacion")
]

def Reconocer_habla(Entrada_habla):
    # iniciar reconocimiento
    print(
        "\nReconociendo palabra..."
    )

    # simular procesamiento
    time.sleep(1)

    # buscar palabra
    for Palabra, Interpretacion in Palabras_habladas:

        if Entrada_habla == Palabra:
            print(
                f"Palabra '{Entrada_habla}' reconocida como: {Interpretacion}"
            )

            return Interpretacion

    # si no existe
    print(
        f"Palabra '{Entrada_habla}' no reconocida."
    )

    return "no reconocida"

def Seleccionar_palabra():
    # generar opciones disponibles
    Opciones = [
        Palabra
        for Palabra, _ in Palabras_habladas
    ]

    # agregar opcion aleatoria
    Opciones.append(
        "aleatoria"
    )

    # mostrar menu
    print(
        "Selecciona una palabra o elige 'aleatoria' para seleccion automatica:"
    )

    for Indice, Opcion in enumerate(Opciones, 1):
        print(
            f"{Indice}. {Opcion}"
        )

    # pedir eleccion
    Eleccion = input(
        "Escribe el numero de tu eleccion: "
    )

    # validar entrada
    if (
        Eleccion.isdigit() and
        1 <= int(Eleccion) <= len(Opciones)
    ):

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

# seleccionar palabra
Palabra_hablada = Seleccionar_palabra()

# mostrar palabra elegida
print(
    "Fernanda dijo:",
    Palabra_hablada
)

# reconocer palabra
Resultado = Reconocer_habla(
    Palabra_hablada
)

# mostrar resultado final
print(
    "Interpretacion final:",
    Resultado
)