# Busqueda A*
import heapq

def A_estrella(Grafo_costos, Heuristica, Inicio, Objetivo):
    # caso simple
    if Inicio == Objetivo:
        return [Inicio], 0

    # validar nodos
    if Inicio not in Grafo_costos or Objetivo not in Grafo_costos:
        return None, None

    # costo real acumulado
    G = {Inicio: 0}

    # cola de prioridad
    Abiertos = []
    F_inicio = G[Inicio] + Heuristica.get(Inicio, float("inf"))
    heapq.heappush(Abiertos, (F_inicio, Inicio, [Inicio]))

    # nodos ya revisados
    Visitados = set()

    # recorrer usando f = g + h
    while Abiertos:
        F_actual, Actual, Camino = heapq.heappop(Abiertos)

        # si ya llegue
        if Actual == Objetivo:
            return Camino, G[Actual]

        if Actual in Visitados:
            continue

        Visitados.add(Actual)

        # revisar vecinos con costo
        for Vecino, Costo_ir in Grafo_costos.get(Actual, {}).items():
            Nuevo_G = G[Actual] + Costo_ir

            if Vecino not in G or Nuevo_G < G[Vecino]:
                G[Vecino] = Nuevo_G
                Nuevo_camino = Camino + [Vecino]

                # f = g + h
                F_vecino = Nuevo_G + Heuristica.get(Vecino, float("inf"))

                heapq.heappush(
                    Abiertos,
                    (F_vecino, Vecino, Nuevo_camino)
                )

    # no hay camino
    return None, None

if __name__ == "__main__":

    # grafo con costos basado en tus recorridos
    Grafo_costos = {
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

    # heuristica hacia Cine
    Heuristica = {
        "Casa": 500,
        "Autolavado": 400,
        "Estetica": 700,
        "Garaje": 900,
        "Tacon": 300,
        "Ammu_Nation": 100,
        "Paintspray": 500,
        "Hospital": 600,
        "Concesionario": 200,
        "Cine": 0
    }

    # pruebas
    Prueba1, Costo1 = A_estrella(Grafo_costos, Heuristica, "Casa", "Cine")
    print("Camino A* Casa -> Cine:", Prueba1)
    print("Costo total:", Costo1)

    Prueba2, Costo2 = A_estrella(Grafo_costos, Heuristica, "Casa", "Hospital")
    print("\nCamino A* Casa -> Hospital:", Prueba2)
    print("Costo total:", Costo2)

    Prueba3, Costo3 = A_estrella(Grafo_costos, Heuristica, "Casa", "Garaje")
    print("\nCamino A* Casa -> Garaje:", Prueba3)
    print("Costo total:", Costo3)

    Prueba4, Costo4 = A_estrella(Grafo_costos, Heuristica, "Casa", "Aeropuerto")
    print("\nCamino A* Casa -> Aeropuerto:", Prueba4)
    print("Costo total:", Costo4)