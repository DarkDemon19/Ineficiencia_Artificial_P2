# Problemas de satisfaccion de restricciones (CSP)

def Es_valida(Asignacion, Restricciones):
    # revisar restricciones
    for Regla in Restricciones:
        if not Regla(Asignacion):
            return False

    return True

def Resolver_csp(Variables, Dominios, Restricciones, Asignacion_actual=None):
    # crear asignacion inicial
    if Asignacion_actual is None:
        Asignacion_actual = {}

    # si ya se asigno todo
    if len(Asignacion_actual) == len(Variables):
        return Asignacion_actual

    # buscar siguiente variable
    for Variable in Variables:
        if Variable not in Asignacion_actual:
            Siguiente_variable = Variable
            break

    # probar valores
    for Valor in Dominios[Siguiente_variable]:
        Nueva_asignacion = Asignacion_actual.copy()
        Nueva_asignacion[Siguiente_variable] = Valor

        if Es_valida(Nueva_asignacion, Restricciones):
            Resultado = Resolver_csp(
                Variables,
                Dominios,
                Restricciones,
                Nueva_asignacion
            )

            if Resultado is not None:
                return Resultado

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
        Dominios[Variable] = ["Zona_1", "Zona_2", "Zona_3"]

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

    Restricciones = [
        Regla_conexiones,
        Regla_hospital
    ]

    Solucion = Resolver_csp(
        Variables,
        Dominios,
        Restricciones
    )

    print("Asignacion encontrada:")
    print(Solucion)