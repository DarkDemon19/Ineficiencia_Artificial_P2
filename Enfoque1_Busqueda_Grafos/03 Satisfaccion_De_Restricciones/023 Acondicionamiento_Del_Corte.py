# Acondicionamiento del corte

def Es_valida(Asignacion, Reglas):
    # revisar reglas
    for Regla in Reglas:
        if not Regla(Asignacion):
            return False

    return True

def Backtracking_simple(Variables, Dominios, Reglas, Asignacion_actual=None):
    # crear asignacion inicial
    if Asignacion_actual is None:
        Asignacion_actual = {}

    # si ya se asigno todo
    if len(Asignacion_actual) == len(Variables):
        if Es_valida(Asignacion_actual, Reglas):
            return Asignacion_actual.copy()

        return None

    # buscar variable pendiente
    for Variable in Variables:
        if Variable not in Asignacion_actual:
            Variable_pendiente = Variable
            break

    # probar valores
    for Valor in Dominios[Variable_pendiente]:
        Nueva_asignacion = Asignacion_actual.copy()
        Nueva_asignacion[Variable_pendiente] = Valor

        if Es_valida(Nueva_asignacion, Reglas):
            Resultado = Backtracking_simple(
                Variables,
                Dominios,
                Reglas,
                Nueva_asignacion
            )

            if Resultado is not None:
                return Resultado

    return None

def Generar_asignaciones_cutset(Cutset_vars, Dominios, Reglas, Base=None):
    # crear base inicial
    if Base is None:
        Base = {}

    # si ya se asigno todo el cutset
    if len(Base) == len(Cutset_vars):
        if Es_valida(Base, Reglas):
            return [Base.copy()]

        return []

    # buscar variable actual
    Index = len(Base)
    Variable_actual = Cutset_vars[Index]

    Posibles = []

    # probar valores
    for Valor in Dominios[Variable_actual]:
        Nueva_base = Base.copy()
        Nueva_base[Variable_actual] = Valor

        if Es_valida(Nueva_base, Reglas):
            Siguientes = Generar_asignaciones_cutset(
                Cutset_vars,
                Dominios,
                Reglas,
                Nueva_base
            )

            Posibles.extend(Siguientes)

    return Posibles

def Acondicionamiento_del_corte(Variables, Dominios, Reglas, Cutset_vars):
    # generar opciones del corte
    Opciones_cutset = Generar_asignaciones_cutset(
        Cutset_vars,
        Dominios,
        Reglas
    )

    # probar cada opcion
    for Asignacion_cutset in Opciones_cutset:

        Restantes = []

        for Variable in Variables:
            if Variable not in Asignacion_cutset:
                Restantes.append(Variable)

        Solucion = Backtracking_simple(
            Restantes,
            Dominios,
            Reglas,
            Asignacion_cutset.copy()
        )

        if Solucion is not None:
            return Solucion

    return None

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

    # variables del corte
    # se eligen nodos con mas conexiones
    Cutset_vars = [
        "Tacon",
        "Ammu_Nation"
    ]

    # ejecutar algoritmo
    Solucion = Acondicionamiento_del_corte(
        Variables,
        Dominios,
        Reglas,
        Cutset_vars
    )

    print("Solucion con acondicionamiento del corte:")
    print(Solucion)