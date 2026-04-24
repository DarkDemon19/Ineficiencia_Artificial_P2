# Busqueda tabu

def Mejor_vecino_no_tabu(Actual, Vecinos, Valor, Tabu):
    # buscar mejor vecino que no este en tabu
    Candidato = None
    Mejor_valor = None

    for Vecino in Vecinos.get(Actual, []):
        if Vecino in Tabu:
            continue

        Valor_vecino = Valor(Vecino)

        if Candidato is None or Valor_vecino > Mejor_valor:
            Candidato = Vecino
            Mejor_valor = Valor_vecino

    return Candidato

def Busqueda_tabu(Inicio, Vecinos, Valor, Tam_tabu, Max_iter):
    # iniciar busqueda
    Actual = Inicio
    Mejor_global = Actual
    Historial = [Actual]

    # lista tabu
    Tabu = set([Actual])
    Cola_tabu = [Actual]

    # repetir hasta maximo de iteraciones
    for _ in range(Max_iter):
        Siguiente = Mejor_vecino_no_tabu(Actual, Vecinos, Valor, Tabu)

        # si no hay vecino valido
        if Siguiente is None:
            break

        # avanzar
        Actual = Siguiente
        Historial.append(Actual)

        # agregar a tabu
        Tabu.add(Actual)
        Cola_tabu.append(Actual)

        # controlar tamaño tabu
        if len(Cola_tabu) > Tam_tabu:
            Viejo = Cola_tabu.pop(0)

            if Viejo in Tabu:
                Tabu.remove(Viejo)

        # actualizar mejor global
        if Valor(Actual) > Valor(Mejor_global):
            Mejor_global = Actual

    return Mejor_global, Historial

if __name__ == "__main__":

    # grafo basado en el CSV y las rutas directas
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

    # valores basados en los costos
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
    Mejor1, Pasos1 = Busqueda_tabu(
        Inicio="Casa",
        Vecinos=Vecinos,
        Valor=Valor,
        Tam_tabu=3,
        Max_iter=10
    )

    print("Mejor estado encontrado:", Mejor1)
    print("Pasos recorridos:", Pasos1)

    Mejor2, Pasos2 = Busqueda_tabu(
        Inicio="Tacon",
        Vecinos=Vecinos,
        Valor=Valor,
        Tam_tabu=3,
        Max_iter=10
    )

    print("\nMejor estado encontrado desde Tacon:", Mejor2)
    print("Pasos recorridos:", Pasos2)