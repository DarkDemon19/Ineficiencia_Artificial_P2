# Busqueda de temple simulado
import random
import math

def Elegir_vecino_aleatorio(Actual, Vecinos):
    # elegir un vecino al azar
    Opciones = Vecinos.get(Actual, [])

    if not Opciones:
        return None

    return random.choice(Opciones)

def Temple_simulado(Inicio, Vecinos, Valor, Temp_inicial, Factor_enfriar, Iter_max):
    # iniciar busqueda
    Actual = Inicio
    Mejor_global = Actual
    Historial = [Actual]

    # temperatura inicial
    Temp = Temp_inicial

    # repetir hasta maximo de iteraciones
    for _ in range(Iter_max):
        Vecino = Elegir_vecino_aleatorio(Actual, Vecinos)

        # si no hay vecino
        if Vecino is None:
            break

        Valor_actual = Valor(Actual)
        Valor_vecino = Valor(Vecino)

        # si el vecino es mejor
        if Valor_vecino > Valor_actual:
            Actual = Vecino

        else:
            # aceptar a veces un vecino peor
            Diferencia = Valor_vecino - Valor_actual
            Probabilidad = math.exp(Diferencia / Temp) if Temp > 0 else 0

            if random.random() < Probabilidad:
                Actual = Vecino

        # guardar paso
        Historial.append(Actual)

        # actualizar mejor global
        if Valor(Actual) > Valor(Mejor_global):
            Mejor_global = Actual

        # enfriar temperatura
        Temp = Temp * Factor_enfriar

        # detener si la temperatura es muy baja
        if Temp <= 0.0001:
            break

    return Mejor_global, Historial

if __name__ == "__main__":

    # grafo basado en el CSV y las rutas directas
    Vecinos = {
        "Casa": ["Autolavado", "Estetica", "Hospital", "Garaje", "Tacon", "Paintspray", "Ammu_Nation", "Concesionario", "Cine"],
        "Estetica": ["Garaje"],
        "Autolavado": ["Tacon"],
        "Tacon": ["Ammu_Nation", "Paintspray", "Hospital"],
        "Ammu_Nation": ["Concesionario", "Cine"],
        "Garaje": [],
        "Paintspray": [],
        "Hospital": [],
        "Concesionario": [],
        "Cine": []
    }

    # valores basados en los costos
    # menor costo = mejor estado, por eso se usa valor negativo
    Valores = {
        "Casa": 0,
        "Autolavado": -100,
        "Estetica": -550,
        "Garaje": -650,
        "Tacon": -450,
        "Paintspray": -1650,
        "Ammu_Nation": -700,
        "Hospital": -450,
        "Concesionario": -750,
        "Cine": -1600
    }

    def Valor(Nodo):
        # regresar valor del nodo
        return Valores.get(Nodo, -9999)

    # prueba
    Mejor1, Pasos1 = Temple_simulado(
        Inicio="Casa",
        Vecinos=Vecinos,
        Valor=Valor,
        Temp_inicial=10.0,
        Factor_enfriar=0.9,
        Iter_max=50
    )

    print("Mejor estado encontrado:", Mejor1)
    print("Historial de estados visitados:", Pasos1)