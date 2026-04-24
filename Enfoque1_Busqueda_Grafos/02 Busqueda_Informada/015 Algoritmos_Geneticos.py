# Algoritmos geneticos
import random

def Crear_individuo(Nodos):
    # crear posible camino
    Individuo = ["Casa"]

    Actual = "Casa"

    while Actual != "Cine":
        Vecinos = Nodos.get(Actual, [])

        if not Vecinos:
            break

        Siguiente = random.choice(Vecinos)

        if Siguiente in Individuo:
            break

        Individuo.append(Siguiente)
        Actual = Siguiente

    return Individuo

def Puntaje(Individuo, Costos):
    # menor costo = mejor puntaje
    Costo_total = 0

    for i in range(len(Individuo) - 1):
        Actual = Individuo[i]
        Siguiente = Individuo[i + 1]

        if Siguiente in Costos.get(Actual, {}):
            Costo_total += Costos[Actual][Siguiente]
        else:
            return -9999

    if Individuo[-1] != "Cine":
        return -9999

    return -Costo_total

def Seleccionar_padres(Poblacion, Costos, Cantidad):
    # elegir mejores caminos
    Poblacion_ordenada = sorted(
        Poblacion,
        key=lambda Ind: Puntaje(Ind, Costos),
        reverse=True
    )

    return Poblacion_ordenada[:Cantidad]

def Cruzar(Padre1, Padre2):
    # mezclar dos caminos
    for Nodo in Padre1:
        if Nodo in Padre2 and Nodo != "Casa":
            Corte1 = Padre1.index(Nodo)
            Corte2 = Padre2.index(Nodo)
            Hijo = Padre1[:Corte1] + Padre2[Corte2:]
            return Hijo

    return Padre1[:]

def Mutar(Individuo, Nodos, Prob_mutacion):
    # cambiar una parte del camino
    if random.random() < Prob_mutacion:
        Posicion = random.randint(0, len(Individuo) - 1)
        Nodo = Individuo[Posicion]

        Vecinos = Nodos.get(Nodo, [])

        if Vecinos:
            Nuevo = random.choice(Vecinos)
            Individuo = Individuo[:Posicion + 1]
            Individuo.append(Nuevo)

            Actual = Nuevo

            while Actual != "Cine":
                Vecinos = Nodos.get(Actual, [])

                if not Vecinos:
                    break

                Siguiente = random.choice(Vecinos)

                if Siguiente in Individuo:
                    break

                Individuo.append(Siguiente)
                Actual = Siguiente

    return Individuo

def Algoritmo_genetico(Nodos, Costos, Tam_poblacion, Generaciones, Prob_mutacion, Padres_a_tomar):
    # crear poblacion inicial
    Poblacion = []

    for _ in range(Tam_poblacion):
        Poblacion.append(Crear_individuo(Nodos))

    Historial_mejor = []

    # repetir generaciones
    for _ in range(Generaciones):
        Padres = Seleccionar_padres(Poblacion, Costos, Padres_a_tomar)

        Nueva_poblacion = []

        for Padre in Padres:
            Nueva_poblacion.append(Padre[:])

        while len(Nueva_poblacion) < Tam_poblacion:
            Padre1 = random.choice(Padres)
            Padre2 = random.choice(Padres)

            Hijo = Cruzar(Padre1, Padre2)
            Hijo = Mutar(Hijo, Nodos, Prob_mutacion)

            Nueva_poblacion.append(Hijo)

        Poblacion = Nueva_poblacion

        Mejor = max(Poblacion, key=lambda Ind: Puntaje(Ind, Costos))
        Historial_mejor.append((Mejor[:], Puntaje(Mejor, Costos)))

    Mejor_final = max(Poblacion, key=lambda Ind: Puntaje(Ind, Costos))

    return Mejor_final, Puntaje(Mejor_final, Costos), Historial_mejor

if __name__ == "__main__":

    # grafo basado en tu CSV y tus rutas directas
    Nodos = {
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

    # costos de tus rutas
    Costos = {
        "Casa": {
            "Autolavado": 100,
            "Estetica": 550,
            "Hospital": 450,
            "Garaje": 650,
            "Tacon": 450,
            "Paintspray": 1650,
            "Ammu_Nation": 700,
            "Concesionario": 750,
            "Cine": 1600
        },
        "Estetica": {
            "Garaje": 400
        },
        "Autolavado": {
            "Tacon": 150
        },
        "Tacon": {
            "Ammu_Nation": 250,
            "Paintspray": 950,
            "Hospital": 250
        },
        "Ammu_Nation": {
            "Concesionario": 100,
            "Cine": 600
        },
        "Garaje": {},
        "Paintspray": {},
        "Hospital": {},
        "Concesionario": {},
        "Cine": {}
    }

    Tam_poblacion = 8
    Generaciones = 20
    Prob_mutacion = 0.2
    Padres_a_tomar = 3

    Mejor, Score, Historial = Algoritmo_genetico(
        Nodos,
        Costos,
        Tam_poblacion,
        Generaciones,
        Prob_mutacion,
        Padres_a_tomar
    )

    print("Mejor camino encontrado:", Mejor)
    print("Puntaje:", Score)
    print("Costo total:", -Score)

    print("\nMejores por generacion:")
    for Gen_idx, (Ind, Sc) in enumerate(Historial):
        print("Gen", Gen_idx, "->", Ind, "puntaje:", Sc, "costo:", -Sc)