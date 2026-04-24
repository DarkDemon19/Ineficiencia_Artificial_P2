# Busqueda en anchura
from collections import deque
import csv
from pathlib import Path

# ruta al CSV dentro de carpeta Datos
DATA_PATH = Path(__file__).resolve().parent / "Datos" / "Rutas.csv"

def Cargar_grafo_csv(Ruta_csv, bidireccional=False):
    # cargar grafo desde CSV
    Grafo = {}

    with Ruta_csv.open(newline='', encoding='utf-8') as Archivo:
        Reader = csv.DictReader(Archivo)
        for Fila in Reader:
            Inicio = Fila["Inicio"].strip()
            Fin = Fila["Fin"].strip()

            Grafo.setdefault(Inicio, []).append(Fin)
            Grafo.setdefault(Fin, [])

            if bidireccional:
                Grafo.setdefault(Fin, []).append(Inicio)

    return Grafo

def Busqueda_anchura_camino(Grafo, Inicio, Objetivo):
    # caso simple
    if Inicio == Objetivo:
        return [Inicio]

    # validar nodos
    if Inicio not in Grafo or Objetivo not in Grafo:
        return None

    # estructuras
    Visitados = {Inicio}
    Cola = deque([Inicio])
    Padres = {Inicio: None}

    # recorrer niveles
    while Cola:
        Actual = Cola.popleft()

        for Vecino in Grafo.get(Actual, []):
            if Vecino not in Visitados:
                Visitados.add(Vecino)
                Padres[Vecino] = Actual

                # si encontramos objetivo
                if Vecino == Objetivo:
                    Camino = [Vecino]
                    Paso = Padres[Vecino]

                    while Paso is not None:
                        Camino.append(Paso)
                        Paso = Padres[Paso]

                    Camino.reverse()
                    return Camino

                Cola.append(Vecino)

    return None

def Busqueda_anchura_orden(Grafo, Inicio):
    # validar nodo
    if Inicio not in Grafo:
        return []

    Visitados = {Inicio}
    Cola = deque([Inicio])
    Orden = [Inicio]

    # recorrido BFS
    while Cola:
        Actual = Cola.popleft()

        for Vecino in Grafo.get(Actual, []):
            if Vecino not in Visitados:
                Visitados.add(Vecino)
                Cola.append(Vecino)
                Orden.append(Vecino)

    return Orden

if __name__ == "__main__":

    # cargar grafo desde Datos/Rutas.csv
    Grafo = Cargar_grafo_csv(DATA_PATH, bidireccional=False)

    print("Grafo:")
    for Nodo, Vecinos in Grafo.items():
        print(Nodo, "->", Vecinos)

    # pruebas
    Prueba1 = Busqueda_anchura_orden(Grafo, "Casa")
    print("\nOrden desde Casa:", Prueba1)

    Prueba2 = Busqueda_anchura_camino(Grafo, "Casa", "Cine")
    print("\nCamino Casa -> Cine:", Prueba2)

    Prueba3 = Busqueda_anchura_camino(Grafo, "Casa", "Garaje")
    print("\nCamino Casa -> Garaje:", Prueba3)

    Prueba4 = Busqueda_anchura_camino(Grafo, "Casa", "Hospital")
    print("\nCamino Casa -> Hospital:", Prueba4)