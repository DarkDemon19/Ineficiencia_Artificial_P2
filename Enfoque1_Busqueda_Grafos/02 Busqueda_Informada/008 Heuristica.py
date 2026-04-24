# Heuristicas

def Mejor_vecino_por_heuristica(Grafo, Heuristica, Actual):
    # elegir el vecino con menor heuristica
    Vecinos = Grafo.get(Actual, [])

    if not Vecinos:
        return None

    Mejor = min(Vecinos, key=lambda Vecino: Heuristica.get(Vecino, float("inf")))

    return Mejor

def Camino_greedy(Grafo, Heuristica, Inicio, Objetivo):
    # avanzar usando la mejor heuristica
    Actual = Inicio
    Camino = [Actual]
    Visitados = set([Actual])

    while Actual != Objetivo:
        Siguiente = Mejor_vecino_por_heuristica(Grafo, Heuristica, Actual)

        # si no hay a donde ir
        if Siguiente is None:
            return Camino, False

        # si se repite, se detiene
        if Siguiente in Visitados:
            return Camino, False

        Camino.append(Siguiente)
        Visitados.add(Siguiente)
        Actual = Siguiente

    return Camino, True

if __name__ == "__main__":

    # grafo basado en tu CSV
    Grafo = {
        "Casa": ["Autolavado", "Estetica"],
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

    # heuristica hacia Cine
    # menor numero significa que esta mas cerca del objetivo
    Heuristica = {
        "Cine": 0,
        "Concesionario": 1,
        "Ammu_Nation": 1,
        "Hospital": 3,
        "Paintspray": 3,
        "Tacon": 2,
        "Autolavado": 3,
        "Garaje": 5,
        "Estetica": 4,
        "Casa": 5
    }

    # pruebas
    Prueba1, Exito1 = Camino_greedy(Grafo, Heuristica, "Casa", "Cine")
    print("Camino Casa -> Cine:", Prueba1)
    print("¿Llego al objetivo?:", Exito1)

    Prueba2, Exito2 = Camino_greedy(Grafo, Heuristica, "Casa", "Hospital")
    print("\nCamino Casa -> Hospital:", Prueba2)
    print("¿Llego al objetivo?:", Exito2)

    Prueba3, Exito3 = Camino_greedy(Grafo, Heuristica, "Casa", "Garaje")
    print("\nCamino Casa -> Garaje:", Prueba3)
    print("¿Llego al objetivo?:", Exito3)