# Busqueda de ascension de colinas

def Mejor_vecino(Estado_actual, Vecinos, Valor):
    # valor del nodo actual
    Valor_actual = Valor(Estado_actual)

    # buscar mejor vecino
    Candidato = None
    Mejor_valor = Valor_actual

    for Vecino in Vecinos.get(Estado_actual, []):
        Valor_vecino = Valor(Vecino)

        if Valor_vecino > Mejor_valor:
            Mejor_valor = Valor_vecino
            Candidato = Vecino

    return Candidato

def Ascension_de_colinas(Inicio, Vecinos, Valor):
    # iniciar recorrido
    Actual = Inicio
    Historial = [Actual]

    while True:
        # buscar mejora
        Siguiente = Mejor_vecino(Actual, Vecinos, Valor)

        # si no hay mejora, se detiene
        if Siguiente is None:
            return Actual, Historial

        # avanzar al mejor vecino
        Actual = Siguiente
        Historial.append(Actual)

if __name__ == "__main__":

    # grafo basado en CSV
    Vecinos = {
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

    # valores basados en  costos
    # menor costo = mejor estado, por eso se usa valor negativo
    Valores = {
        "Casa": 0,
        "Autolavado": -100,
        "Estetica": -550,
        "Garaje": -650,
        "Tacon": -450,
        "Paintspray": -1650,
        "Ammu_Nation": -700,
        "Hospital": -450,
        "Concesionario": -750,
        "Cine": -1600
    }

    def Valor(Nodo):
        # regresar valor del nodo
        return Valores.get(Nodo, -9999)

    # pruebas
    Final1, Pasos1 = Ascension_de_colinas("Casa", Vecinos, Valor)
    print("Estado final desde Casa:", Final1)
    print("Pasos:", Pasos1)

    Final2, Pasos2 = Ascension_de_colinas("Tacon", Vecinos, Valor)
    print("\nEstado final desde Tacon:", Final2)
    print("Pasos:", Pasos2)

    Final3, Pasos3 = Ascension_de_colinas("Estetica", Vecinos, Valor)
    print("\nEstado final desde Estetica:", Final3)
    print("Pasos:", Pasos3)