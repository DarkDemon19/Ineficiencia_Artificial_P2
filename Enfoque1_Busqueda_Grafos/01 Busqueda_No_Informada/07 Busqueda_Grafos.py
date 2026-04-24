# Busqueda en grafos
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

def Busqueda_en_grafo(Grafo, Inicio):
    # recorre el grafo desde inicio
    # no repite nodos
    # regresa el orden de visita

    if Inicio not in Grafo:
        return []

    Visitados = set([Inicio])
    Cola = deque([Inicio])
    Orden = []

    while Cola:
        Actual = Cola.popleft()
        Orden.append(Actual)

        # revisar vecinos
        for Vecino in Grafo.get(Actual, []):
            if Vecino not in Visitados:
                Visitados.add(Vecino)
                Cola.append(Vecino)

    return Orden

def Hay_camino(Grafo, Inicio, Objetivo):
    # revisar si existe camino entre dos nodos

    if Inicio == Objetivo:
        return True

    if Inicio not in Grafo or Objetivo not in Grafo:
        return False

    Visitados = set([Inicio])
    Cola = deque([Inicio])

    while Cola:
        Actual = Cola.popleft()

        if Actual == Objetivo:
            return True

        for Vecino in Grafo.get(Actual, []):
            if Vecino not in Visitados:
                Visitados.add(Vecino)
                Cola.append(Vecino)

    return False

if __name__ == "__main__":

    # cargar grafo desde csv
    Grafo = Cargar_grafo_csv(DATA_PATH, bidireccional=False)

    print("Grafo:")
    for Nodo, Vecinos in Grafo.items():
        print(Nodo, "->", Vecinos)

    # pruebas
    Prueba1 = Busqueda_en_grafo(Grafo, "Casa")
    print("\nOrden de visita desde Casa:", Prueba1)

    Prueba2 = Hay_camino(Grafo, "Casa", "Cine")
    print("\nHay camino Casa -> Cine?:", Prueba2)

    Prueba3 = Hay_camino(Grafo, "Casa", "Garaje")
    print("\nHay camino Casa -> Garaje?:", Prueba3)

    Prueba4 = Hay_camino(Grafo, "Casa", "Hospital")
    print("\nHay camino Casa -> Hospital?:", Prueba4)

    Prueba5 = Hay_camino(Grafo, "Casa", "Aeropuerto")
    print("\nHay camino Casa -> Aeropuerto?:", Prueba5)