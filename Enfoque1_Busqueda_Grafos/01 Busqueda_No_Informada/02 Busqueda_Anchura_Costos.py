# Busqueda en anchura de costo uniforme
import heapq
import csv
from pathlib import Path

# ruta al CSV dentro de carpeta Datos
DATA_PATH = Path(__file__).resolve().parent / "Datos" / "Rutas.csv"

def Cargar_grafo_csv_costos(Ruta_csv):
    # cargar grafo desde CSV
    Grafo = {}

    with Ruta_csv.open(newline='', encoding='utf-8') as Archivo:
        Reader = csv.DictReader(Archivo)
        for Fila in Reader:
            Inicio = Fila["Inicio"].strip()
            Fin = Fila["Fin"].strip()

            Grafo.setdefault(Inicio, {})
            Grafo.setdefault(Fin, {})

    # costos de las rutas
    Grafo["Casa"]["Autolavado"] = 100
    Grafo["Casa"]["Estetica"] = 550
    Grafo["Estetica"]["Garaje"] = 400
    Grafo["Autolavado"]["Tacon"] = 150
    Grafo["Tacon"]["Ammu_Nation"] = 250
    Grafo["Tacon"]["Paintspray"] = 950
    Grafo["Tacon"]["Hospital"] = 250
    Grafo["Ammu_Nation"]["Concesionario"] = 100
    Grafo["Ammu_Nation"]["Cine"] = 600

    # rutas directas extras desde Casa
    Grafo["Casa"]["Hospital"] = 450
    Grafo["Casa"]["Garaje"] = 650
    Grafo["Casa"]["Tacon"] = 450
    Grafo["Casa"]["Paintspray"] = 1650
    Grafo["Casa"]["Ammu_Nation"] = 700
    Grafo["Casa"]["Concesionario"] = 750
    Grafo["Casa"]["Cine"] = 1600

    return Grafo

def Busqueda_costo_uniforme(Grafo, Inicio, Objetivo):
    # caso simple
    if Inicio == Objetivo:
        return [Inicio], 0

    # validar nodos
    if Inicio not in Grafo or Objetivo not in Grafo:
        return None, None

    # costo acumulado
    Costos = {Inicio: 0}

    # padres del camino
    Padres = {Inicio: None}

    # cola de prioridad
    Cola = [(0, Inicio)]

    # recorrer por menor costo
    while Cola:
        Costo_actual, Actual = heapq.heappop(Cola)

        # si ya llegue
        if Actual == Objetivo:
            Camino = [Actual]
            Paso = Padres[Actual]

            while Paso is not None:
                Camino.append(Paso)
                Paso = Padres[Paso]

            Camino.reverse()
            return Camino, Costo_actual

        # revisar vecinos
        for Vecino, Costo_arista in Grafo.get(Actual, {}).items():
            Nuevo_costo = Costo_actual + Costo_arista

            if Vecino not in Costos or Nuevo_costo < Costos[Vecino]:
                Costos[Vecino] = Nuevo_costo
                Padres[Vecino] = Actual
                heapq.heappush(Cola, (Nuevo_costo, Vecino))

    # no existe camino
    return None, None

if __name__ == "__main__":

    # cargar grafo con costos
    Grafo = Cargar_grafo_csv_costos(DATA_PATH)

    print("Grafo con costos:")
    for Nodo, Vecinos in Grafo.items():
        print(Nodo, "->", Vecinos)

    # pruebas
    Prueba1, Costo1 = Busqueda_costo_uniforme(Grafo, "Casa", "Cine")
    print("\nCamino Casa -> Cine:", Prueba1)
    print("Costo total:", Costo1)

    Prueba2, Costo2 = Busqueda_costo_uniforme(Grafo, "Casa", "Garaje")
    print("\nCamino Casa -> Garaje:", Prueba2)
    print("Costo total:", Costo2)

    Prueba3, Costo3 = Busqueda_costo_uniforme(Grafo, "Casa", "Hospital")
    print("\nCamino Casa -> Hospital:", Prueba3)
    print("Costo total:", Costo3)

    Prueba4, Costo4 = Busqueda_costo_uniforme(Grafo, "Casa", "Concesionario")
    print("\nCamino Casa -> Concesionario:", Prueba4)
    print("Costo total:", Costo4)