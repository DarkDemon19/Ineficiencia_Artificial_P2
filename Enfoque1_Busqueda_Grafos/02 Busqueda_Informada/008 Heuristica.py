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

        if Siguiente is None:
            return Camino, False

        if Siguiente in Visitados:
            return Camino, False

        Camino.append(Siguiente)
        Visitados.add(Siguiente)
        Actual = Siguiente

    return Camino, True

if __name__ == "__main__":

    # grafo 
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

    # heuristica basada en costos (invertida: menor costo = mejor)
    Heuristica = {
        "Cine": 0,
        "Concesionario": 100,
        "Ammu_Nation": 250,
        "Hospital": 450,
        "Tacon": 450,
        "Autolavado": 550,
        "Estetica": 550,
        "Garaje": 650,
        "Paintspray": 950,
        "Casa": 1000
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