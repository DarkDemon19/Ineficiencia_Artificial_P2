# Salto atras dirigido por conflictos

def Revisar_reglas(Asignacion):
    # regla:
    # nodos conectados no pueden estar en la misma zona

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
                return False, ("misma_zona", Nodo2)

    # regla:
    # Hospital no puede estar en Zona_3
    if "Hospital" in Asignacion:
        if Asignacion["Hospital"] == "Zona_3":
            return False, ("hospital_zona", None)

    return True, None

def Salto_atras_conflictos(Variables, Dominios):
    # mapa de indices
    Indice_variable = {}

    for Posicion, Variable in enumerate(Variables):
        Indice_variable[Variable] = Posicion

    Historial_debug = []

    def Intentar(Index, Asignacion_actual):
        # si ya termine
        if Index == len(Variables):
            return Asignacion_actual.copy(), None

        Variable_actual = Variables[Index]

        Mejor_salto = None

        # probar valores
        for Valor in Dominios[Variable_actual]:
            Asignacion_actual[Variable_actual] = Valor

            Ok, Conflicto = Revisar_reglas(Asignacion_actual)

            Historial_debug.append(
                f"Probando {Variable_actual} = {Valor} -> {'ok' if Ok else 'conflicto'}"
            )

            if Ok:
                Solucion, Salto = Intentar(
                    Index + 1,
                    Asignacion_actual
                )

                if Solucion is not None:
                    return Solucion, None

                if Salto is not None:
                    if Mejor_salto is None or Salto < Mejor_salto:
                        Mejor_salto = Salto

            else:
                Tipo_conflicto, Dato_extra = Conflicto

                if Tipo_conflicto == "misma_zona":
                    Variable_conflictiva = Dato_extra
                    Salto_conflicto = Indice_variable.get(
                        Variable_conflictiva,
                        Index - 1
                    )

                elif Tipo_conflicto == "hospital_zona":
                    Salto_conflicto = Indice_variable["Hospital"]

                else:
                    Salto_conflicto = Index - 1

                if Mejor_salto is None or Salto_conflicto < Mejor_salto:
                    Mejor_salto = Salto_conflicto

        # quitar variable
        del Asignacion_actual[Variable_actual]

        return None, Mejor_salto

    Solucion_final, _ = Intentar(0, {})

    return Solucion_final, Historial_debug

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

    # ejecutar algoritmo
    Solucion, Debug = Salto_atras_conflictos(
        Variables,
        Dominios
    )

    print("Solucion encontrada:")
    print(Solucion)

    print("\nPasos del algoritmo:")
    for Linea in Debug:
        print(Linea)