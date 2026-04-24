# Busqueda en profundidad limitada
import csv
from pathlib import Path

# ruta al CSV dentro de carpeta Datos
DATA_PATH = Path(__file__).resolve().parent / "Datos" / "Rutas.csv"

def Cargar_grafo_csv(Ruta_csv):
    # cargar grafo desde CSV
    Grafo = {}

    with Ruta_csv.open(newline="", encoding="utf-8") as Archivo:
        Reader = csv.DictReader(Archivo)
        for Fila in Reader:
            Inicio = Fila["Inicio"].strip()
            Fin = Fila["Fin"].strip()

            Grafo.setdefault(Inicio, []).append(Fin)
            Grafo.setdefault(Fin, [])

    return Grafo

def Busqueda_profundidad_limitada(Grafo, Actual, Objetivo, Limite, Camino=None):
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

        Resultado = Busqueda_profundidad_limitada(
            Grafo,
            Vecino,
            Objetivo,
            Limite - 1,
            Camino + [Vecino]
        )

        # si encontro camino
        if Resultado is not None:
            return Resultado

    # si no encontro camino
    return None

if __name__ == "__main__":

    # cargar grafo desde CSV
    Grafo = Cargar_grafo_csv(DATA_PATH)

    print("Grafo:")
    for Nodo, Vecinos in Grafo.items():
        print(Nodo, "->", Vecinos)

    # pruebas
    Prueba1 = Busqueda_profundidad_limitada(Grafo, "Casa", "Cine", Limite=3)
    print("\nLimite = 3 | Casa -> Cine:", Prueba1)

    Prueba2 = Busqueda_profundidad_limitada(Grafo, "Casa", "Cine", Limite=4)
    print("\nLimite = 4 | Casa -> Cine:", Prueba2)

    Prueba3 = Busqueda_profundidad_limitada(Grafo, "Casa", "Garaje", Limite=2)
    print("\nLimite = 2 | Casa -> Garaje:", Prueba3)

    Prueba4 = Busqueda_profundidad_limitada(Grafo, "Casa", "Hospital", Limite=3)
    print("\nLimite = 3 | Casa -> Hospital:", Prueba4)

    Prueba5 = Busqueda_profundidad_limitada(Grafo, "Casa", "Aeropuerto", Limite=5)
    print("\nLimite = 5 | Casa -> Aeropuerto:", Prueba5)