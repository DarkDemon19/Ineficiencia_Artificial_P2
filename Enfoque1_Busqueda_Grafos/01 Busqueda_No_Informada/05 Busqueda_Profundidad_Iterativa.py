# Busqueda en profundidad iterativa
import csv
from pathlib import Path

# ruta al CSV dentro de carpeta Datos
DATA_PATH = Path(__file__).resolve().parent / "Datos" / "Rutas.csv"

def Cargar_grafo_csv(Ruta_csv):
    # cargar grafo desde CSV
    Grafo = {}

    with Ruta_csv.open(newline='', encoding='utf-8') as Archivo:
        Reader = csv.DictReader(Archivo)
        for Fila in Reader:
            Inicio = Fila["Inicio"].strip()
            Fin = Fila["Fin"].strip()

            Grafo.setdefault(Inicio, []).append(Fin)
            Grafo.setdefault(Fin, [])

    return Grafo

def Profundidad_limitada(Grafo, Actual, Objetivo, Limite, Camino=None):
    # crear camino en la primera llamada
    if Camino is None:
        Camino = [Actual]

    # si ya llegue
    if Actual == Objetivo:
        return Camino

    # si ya no puedo bajar mas
    if Limite == 0:
        return None

    # revisar vecinos
    for Vecino in Grafo.get(Actual, []):
        if Vecino in Camino:
            continue

        Resultado = Profundidad_limitada(
            Grafo,
            Vecino,
            Objetivo,
            Limite - 1,
            Camino + [Vecino]
        )

        if Resultado is not None:
            return Resultado

    return None

def Profundidad_iterativa(Grafo, Inicio, Objetivo, Limite_max):
    # validar nodos
    if Inicio not in Grafo or Objetivo not in Grafo:
        return None, None

    # probar limite por limite
    for Limite in range(1, Limite_max + 1):
        Camino = Profundidad_limitada(
            Grafo,
            Inicio,
            Objetivo,
            Limite
        )

        if Camino is not None:
            return Camino, Limite

    return None, None

if __name__ == "__main__":

    # cargar grafo desde CSV
    Grafo = Cargar_grafo_csv(DATA_PATH)

    print("Grafo:")
    for Nodo, Vecinos in Grafo.items():
        print(Nodo, "->", Vecinos)

    # pruebas
    Prueba1, Limite1 = Profundidad_iterativa(Grafo, "Casa", "Cine", 10)
    print("\nCamino Casa -> Cine:", Prueba1)
    print("Limite usado:", Limite1)

    Prueba2, Limite2 = Profundidad_iterativa(Grafo, "Casa", "Garaje", 10)
    print("\nCamino Casa -> Garaje:", Prueba2)
    print("Limite usado:", Limite2)

    Prueba3, Limite3 = Profundidad_iterativa(Grafo, "Casa", "Hospital", 10)
    print("\nCamino Casa -> Hospital:", Prueba3)
    print("Limite usado:", Limite3)

    Prueba4, Limite4 = Profundidad_iterativa(Grafo, "Casa", "Aeropuerto", 10)
    print("\nCamino Casa -> Aeropuerto:", Prueba4)
    print("Limite usado:", Limite4)