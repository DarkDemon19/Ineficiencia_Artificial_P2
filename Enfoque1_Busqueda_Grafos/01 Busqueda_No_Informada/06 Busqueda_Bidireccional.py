# Busqueda bidireccional
from collections import deque  # para usar colas (FIFO)

def Camino_rebuilder(Padres_i, Padres_o, punto):
    # arma el camino final desde inicio hasta objetivo

    # parte desde inicio hasta el punto de encuentro
    Camino_i = [punto]
    n = Padres_i[punto]
    while n is not None:
        Camino_i.append(n)
        n = Padres_i[n]
    Camino_i.reverse()

    # parte desde el punto hasta el objetivo
    Camino_o = []
    n = Padres_o[punto]
    while n is not None:
        Camino_o.append(n)
        n = Padres_o[n]

    return Camino_i + Camino_o

def Busqueda_bi(grafo, inicio, objetivo):

    # caso simple
    if inicio == objetivo:
        return [inicio]

    # validar nodos
    if inicio not in grafo or objetivo not in grafo:
        return None

    # visitados de cada lado
    Visita_i = {inicio}
    Visita_o = {objetivo}

    # colas de cada lado
    Cola_i = deque([inicio])
    Cola_o = deque([objetivo])

    # padres para reconstruir camino
    Padre_i = {inicio: None}
    Padre_o = {objetivo: None}

    # mientras haya nodos en ambas colas
    while Cola_i and Cola_o:

        # avanzar desde inicio
        Actual_i = Cola_i.popleft()

        for Vecino in grafo.get(Actual_i, []):
            if Vecino not in Visita_i:
                Visita_i.add(Vecino)
                Padre_i[Vecino] = Actual_i
                Cola_i.append(Vecino)

                # si ya lo vio el otro lado, se encontraron
                if Vecino in Visita_o:
                    return Camino_rebuilder(Padre_i, Padre_o, Vecino)

        # avanzar desde objetivo (al revés)
        Actual_o = Cola_o.popleft()

        for nodo, vecinos in grafo.items():
            if Actual_o in vecinos:
                if nodo not in Visita_o:
                    Visita_o.add(nodo)
                    Padre_o[nodo] = Actual_o
                    Cola_o.append(nodo)

                    # si ya lo vio el lado inicio, se encontraron
                    if nodo in Visita_i:
                        return Camino_rebuilder(Padre_i, Padre_o, nodo)

    # no hay camino
    return None

if __name__ == "__main__":

    # grafo basado en el CSV
    grafo = {
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

    # pruebas
    Prueba1 = Busqueda_bi(grafo, "Casa", "Cine")
    print("Camino Casa -> Cine:", Prueba1)

    Prueba2 = Busqueda_bi(grafo, "Casa", "Garaje")
    print("Camino Casa -> Garaje:", Prueba2)