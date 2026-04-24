# Busqueda en profundidad
import csv
from pathlib import Path

# ruta al CSV dentro de carpeta Datos
DATA_PATH = Path(__file__).resolve().parent / "Datos" / "Rutas.csv"

def Cargar_grafo_csv(Ruta_csv, bidireccional=False):
    # cargar grafo desde CSV
    Grafo = {}

    with Ruta_csv.open(newline="", encoding="utf-8") as Archivo:
        Reader = csv.DictReader(Archivo)
        for Fila in Reader:
            Inicio = Fila["Inicio"].strip()
            Fin = Fila["Fin"].strip()

            Grafo.setdefault(Inicio, []).append(Fin)
            Grafo.setdefault(Fin, [])

            if bidireccional:
                Grafo.setdefault(Fin, []).append(Inicio)

    return Grafo

def Busqueda_profundidad_camino(Grafo, Inicio, Objetivo, Visitados=None, Camino=None):
    # crear estructuras en la primera llamada
    if Visitados is None:
        Visitados = set()

    if Camino is None:
        Camino = [Inicio]

    # marcar nodo actual
    Visitados.add(Inicio)

    # si ya llegue al objetivo
    if Inicio == Objetivo:
        return Camino

    # revisar vecinos
    for Vecino in Grafo.get(Inicio, []):
        if Vecino not in Visitados:
            Resultado = Busqueda_profundidad_camino(
                Grafo,
                Vecino,
                Objetivo,
                Visitados,
                Camino + [Vecino]
            )

            # si si encontro camino
            if Resultado is not None:
                return Resultado

    # si no encontro camino
    return None

if __name__ == "__main__":

    # cargar grafo desde csv
    Grafo = Cargar_grafo_csv(DATA_PATH, bidireccional=False)

    print("Grafo:")
    for Nodo, Vecinos in Grafo.items():
        print(Nodo, "->", Vecinos)

    # pruebas
    Prueba1 = Busqueda_profundidad_camino(Grafo, "Casa", "Cine")
    print("\nCamino Casa -> Cine:", Prueba1)

    Prueba2 = Busqueda_profundidad_camino(Grafo, "Casa", "Garaje")
    print("\nCamino Casa -> Garaje:", Prueba2)

    Prueba3 = Busqueda_profundidad_camino(Grafo, "Casa", "Hospital")
    print("\nCamino Casa -> Hospital:", Prueba3)

    Prueba4 = Busqueda_profundidad_camino(Grafo, "Casa", "Aeropuerto")
    print("\nCamino Casa -> Aeropuerto:", Prueba4)