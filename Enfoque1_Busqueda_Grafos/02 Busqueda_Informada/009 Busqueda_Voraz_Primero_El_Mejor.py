# Busqueda voraz primero el mejor
import heapq

def Busqueda_voraz(Grafo, Heuristica, Inicio, Objetivo):
    # caso simple
    if Inicio == Objetivo:
        return [Inicio]

    # cola de prioridad
    Abiertos = []
    heapq.heappush(
        Abiertos,
        (Heuristica.get(Inicio, float("inf")), Inicio, [Inicio])
    )

    # nodos visitados
    Visitados = set([Inicio])

    # recorrer por mejor heuristica
    while Abiertos:
        _, Actual, Camino = heapq.heappop(Abiertos)

        # si ya llegue
        if Actual == Objetivo:
            return Camino

        # revisar vecinos
        for Vecino in Grafo.get(Actual, []):
            if Vecino not in Visitados:
                Visitados.add(Vecino)

                Nuevo_camino = Camino + [Vecino]

                heapq.heappush(
                    Abiertos,
                    (Heuristica.get(Vecino, float("inf")), Vecino, Nuevo_camino)
                )

    # si no encontro camino
    return None

if __name__ == "__main__":

    # grafo basado en CSV
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

    # heuristica 
    # menor numero significa que se ve mas cercano
    Heuristica = {
        "Casa": 1000,
        "Autolavado": 550,
        "Estetica": 550,
        "Garaje": 650,
        "Tacon": 450,
        "Ammu_Nation": 250,
        "Paintspray": 950,
        "Hospital": 450,
        "Concesionario": 100,
        "Cine": 0
    }

    # pruebas
    Prueba1 = Busqueda_voraz(Grafo, Heuristica, "Casa", "Cine")
    print("Camino voraz Casa -> Cine:", Prueba1)

    Prueba2 = Busqueda_voraz(Grafo, Heuristica, "Casa", "Hospital")
    print("Camino voraz Casa -> Hospital:", Prueba2)

    Prueba3 = Busqueda_voraz(Grafo, Heuristica, "Casa", "Garaje")
    print("Camino voraz Casa -> Garaje:", Prueba3)

    Prueba4 = Busqueda_voraz(Grafo, Heuristica, "Casa", "Aeropuerto")
    print("Camino voraz Casa -> Aeropuerto:", Prueba4)