# Busqueda de haz local

def Generar_siguientes(Estados_actuales, Vecinos):
    # juntar estados actuales y sus vecinos
    Nuevo_conjunto = set()

    for Estado in Estados_actuales:
        Nuevo_conjunto.add(Estado)

    for Estado in Estados_actuales:
        for Vecino in Vecinos.get(Estado, []):
            Nuevo_conjunto.add(Vecino)

    return list(Nuevo_conjunto)

def Top_k(Estados, Valor, K):
    # ordenar de mejor a peor
    Ordenados = sorted(Estados, key=lambda Nodo: Valor(Nodo), reverse=True)

    # regresar los K mejores
    return Ordenados[:K]

def Haz_local(Inicio_lista, Vecinos, Valor, K, Iter_max):
    # iniciar estados activos
    Actuales = Inicio_lista[:]

    # guardar historial
    Historial = [Actuales[:]]

    # repetir iteraciones
    for _ in range(Iter_max):
        Candidatos = Generar_siguientes(Actuales, Vecinos)

        # quedarse con los mejores
        Actuales = Top_k(Candidatos, Valor, K)

        Historial.append(Actuales[:])

    # mejor estado final
    Mejor_final = max(Actuales, key=lambda Nodo: Valor(Nodo))

    return Mejor_final, Historial

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

    # prueba
    Mejor1, Historial1 = Haz_local(
        Inicio_lista=["Casa", "Autolavado"],
        Vecinos=Vecinos,
        Valor=Valor,
        K=2,
        Iter_max=5
    )

    print("Mejor estado al final:", Mejor1)
    print("Historial del haz:")

    for Paso, Estados in enumerate(Historial1):
        print("Paso", Paso, "=>", Estados)