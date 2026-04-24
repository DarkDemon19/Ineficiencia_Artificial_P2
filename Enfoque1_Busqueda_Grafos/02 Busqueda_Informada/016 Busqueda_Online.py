# Busqueda online

def Paso_online(Actual, Mundo_real, Memoria_local, Visitados):
    # descubrir vecinos del nodo actual
    Vecinos_reales = Mundo_real.get(Actual, [])

    # guardar lo descubierto
    Memoria_local[Actual] = Vecinos_reales[:]

    # guardar opciones no visitadas
    Opciones = []

    for Vecino in Vecinos_reales:
        if Vecino not in Visitados:
            Opciones.append(Vecino)

    return Opciones

def Busqueda_online(Inicio, Objetivo, Mundo_real, Max_pasos):
    # iniciar recorrido
    Actual = Inicio
    Camino_recorrido = [Actual]

    # memoria del agente
    Memoria_local = {}

    # nodos visitados
    Visitados = set([Actual])

    # recorrer paso a paso
    for _ in range(Max_pasos):

        # si ya llegue
        if Actual == Objetivo:
            return Camino_recorrido, Memoria_local, True

        # descubrir opciones
        Opciones = Paso_online(
            Actual,
            Mundo_real,
            Memoria_local,
            Visitados
        )

        # si no hay opciones
        if not Opciones:
            return Camino_recorrido, Memoria_local, False

        # elegir siguiente opcion
        Siguiente = Opciones[0]

        # avanzar
        Actual = Siguiente
        Visitados.add(Actual)
        Camino_recorrido.append(Actual)

    # si no llego dentro del limite
    return Camino_recorrido, Memoria_local, False

if __name__ == "__main__":

    # mundo real basado en tu CSV y tus rutas directas
    Mundo_real = {
        "Casa": ["Autolavado", "Estetica", "Hospital", "Garaje", "Tacon", "Paintspray", "Ammu_Nation", "Concesionario", "Cine"],
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

    # costos de tus rutas
    Costos = {
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

    # prueba
    Camino1, Memoria1, Exito1 = Busqueda_online(
        Inicio="Casa",
        Objetivo="Cine",
        Mundo_real=Mundo_real,
        Max_pasos=10
    )

    print("Camino recorrido:", Camino1)
    print("Llego al objetivo?:", Exito1)

    print("\nMemoria aprendida:")
    for Nodo, Vecinos in Memoria1.items():
        print(Nodo, "->", Vecinos)

    # segunda prueba
    Camino2, Memoria2, Exito2 = Busqueda_online(
        Inicio="Casa",
        Objetivo="Hospital",
        Mundo_real=Mundo_real,
        Max_pasos=10
    )

    print("\nCamino recorrido Casa -> Hospital:", Camino2)
    print("Llego al objetivo?:", Exito2)

    print("\nMemoria aprendida:")
    for Nodo, Vecinos in Memoria2.items():
        print(Nodo, "->", Vecinos)