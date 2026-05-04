# Busqueda local: minimos conflictos
import random

def Contar_conflictos(Asignacion, Reglas):
    # contar reglas rotas
    Conflictos = 0

    for Regla in Reglas:
        if not Regla(Asignacion):
            Conflictos += 1

    return Conflictos

def Variables_en_conflicto(Asignacion, Reglas):
    # detectar variables con conflicto
    Malas = set()

    for Regla in Reglas:
        if not Regla(Asignacion):
            for Variable in Asignacion:
                Malas.add(Variable)

    return list(Malas)

def Mejor_valor_para(Variable, Asignacion, Dominios, Reglas):
    # buscar valor con menos conflictos
    Mejor_opcion = None
    Mejor_conflicto = None

    for Posible_valor in Dominios[Variable]:
        Copia = Asignacion.copy()
        Copia[Variable] = Posible_valor

        Conflictos = Contar_conflictos(Copia, Reglas)

        if Mejor_opcion is None or Conflictos < Mejor_conflicto:
            Mejor_opcion = Posible_valor
            Mejor_conflicto = Conflictos

    return Mejor_opcion

def Minimos_conflictos(Variables, Dominios, Reglas, Intentos_max, Pasos_max):
    # historial del proceso
    Historial = []

    for _ in range(Intentos_max):

        # asignacion inicial aleatoria
        Asignacion = {}

        for Variable in Variables:
            Asignacion[Variable] = random.choice(Dominios[Variable])

        Historial.append(Asignacion.copy())

        # corregir conflictos
        for _ in range(Pasos_max):

            if Contar_conflictos(Asignacion, Reglas) == 0:
                return Asignacion, Historial

            Malas = Variables_en_conflicto(Asignacion, Reglas)

            if not Malas:
                return Asignacion, Historial

            Variable_a_arreglar = random.choice(Malas)

            Mejor_valor = Mejor_valor_para(
                Variable_a_arreglar,
                Asignacion,
                Dominios,
                Reglas
            )

            Asignacion[Variable_a_arreglar] = Mejor_valor
            Historial.append(Asignacion.copy())

    return None, Historial

if __name__ == "__main__":

    # variables basadas en nodos reales
    Variables = [
        "Autolavado",
        "Estetica",
        "Garaje",
        "Tacon",
        "Ammu_Nation",
        "Paintspray",
        "Hospital",
        "Concesionario",
        "Cine"
    ]

    # dominios
    Dominios = {}

    for Variable in Variables:
        Dominios[Variable] = [
            "Zona_1",
            "Zona_2",
            "Zona_3"
        ]

    # regla:
    # nodos conectados no pueden compartir zona
    def Regla_conexiones(Asignacion):

        Conexiones = [
            ("Estetica", "Garaje"),
            ("Autolavado", "Tacon"),
            ("Tacon", "Ammu_Nation"),
            ("Tacon", "Paintspray"),
            ("Tacon", "Hospital"),
            ("Ammu_Nation", "Concesionario"),
            ("Ammu_Nation", "Cine")
        ]

        for Nodo1, Nodo2 in Conexiones:
            if Nodo1 in Asignacion and Nodo2 in Asignacion:
                if Asignacion[Nodo1] == Asignacion[Nodo2]:
                    return False

        return True

    # regla:
    # Hospital no puede estar en Zona_3
    def Regla_hospital(Asignacion):
        if "Hospital" in Asignacion:
            return Asignacion["Hospital"] != "Zona_3"

        return True

    Reglas = [
        Regla_conexiones,
        Regla_hospital
    ]

    # ejecutar algoritmo
    Solucion, Historial = Minimos_conflictos(
        Variables=Variables,
        Dominios=Dominios,
        Reglas=Reglas,
        Intentos_max=10,
        Pasos_max=20
    )

    print("Solucion encontrada:")
    print(Solucion)

    print("\nProceso:")
    for Paso, Asignacion in enumerate(Historial):
        print("Paso", Paso, "->", Asignacion)