# Simula eventos inciertos
# para observar probabilidades cuando no existe certeza total

# Para generar eventos aleatorios
import random

def Evento_aleatorio():
    # generar evento con probabilidad aproximada de 30%
    Numero = random.random()

    if Numero < 0.3:
        return True

    else:
        return False

def Medir_incertidumbre(Intentos):
    # contar ocurrencias del evento
    Pasa = 0
    No_pasa = 0

    for _ in range(Intentos):

        if Evento_aleatorio():
            Pasa += 1

        else:
            No_pasa += 1

    # calcular probabilidad aproximada
    Probabilidad_aproximada = Pasa / Intentos

    return {
        "Veces_paso": Pasa,
        "Veces_no_paso": No_pasa,
        "Probabilidad_aproximada": Probabilidad_aproximada
    }

# ejecutar simulacion
Resultado = Medir_incertidumbre(
    Intentos=1000
)

# mostrar resultados
print(
    "Veces que el evento ocurrio:",
    Resultado["Veces_paso"]
)

print(
    "Veces que el evento no ocurrio:",
    Resultado["Veces_no_paso"]
)

print(
    "Probabilidad aproximada:",
    round(Resultado["Probabilidad_aproximada"], 3)
)

# resumen final
print(
    "- No existe certeza absoluta en una prueba individual"
)

print(
    "- Solo se estima una probabilidad aproximada"
)

print(
    "- Esto representa manejo de incertidumbre"
)