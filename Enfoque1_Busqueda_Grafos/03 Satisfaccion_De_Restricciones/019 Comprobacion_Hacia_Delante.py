# Comprobacion hacia delante

def Es_valida(Asignacion, Restricciones):
    # revisar restricciones
    for Regla in Restricciones:
        if not Regla(Asignacion):
            return False

    return True

def Dominio_filtrado(Variable_objetivo, Asignacion_parcial, Dominios, Restricciones):
    # revisar valores posibles para una variable
    Valores_validos = []

    for Posible_valor in Dominios[Variable_objetivo]:
        Prueba = Asignacion_parcial.copy()
        Prueba[Variable_objetivo] = Posible_valor

        if Es_valida(Prueba, Restricciones):
            Valores_validos.append(Posible_valor)

    return Valores_validos

def Forward_checking(Variables, Dominios, Restricciones, Asignacion_actual=None):
    # crear asignacion inicial
    if Asignacion_actual is None:
        Asignacion_actual = {}

    print("Intentando con asignacion:", Asignacion_actual)

    # si ya se asigno todo
    if len(Asignacion_actual) == len(Variables):
        return Asignacion_actual

    # buscar variable pendiente
    for Variable in Variables:
        if Variable not in Asignacion_actual:
            Variable_pendiente = Variable
            break

    # probar valores posibles
    for Valor in Dominios[Variable_pendiente]:
        Nueva_asignacion = Asignacion_actual.copy()
        Nueva_asignacion[Variable_pendiente] = Valor

        print(" Probando", Variable_pendiente, "=", Valor)

        # validar reglas
        if not Es_valida(Nueva_asignacion, Restricciones):
            print("  Rompe una regla")
            continue

        # revisar variables futuras
        Consistente = True

        for Otra_variable in Variables:
            if Otra_variable not in Nueva_asignacion:
                Dominio_restante = Dominio_filtrado(
                    Otra_variable,
                    Nueva_asignacion,
                    Dominios,
                    Restricciones
                )

                print("  Dominio restante para", Otra_variable, "->", Dominio_restante)

                if len(Dominio_restante) == 0:
                    print("  Sin opciones para", Otra_variable)
                    Consistente = False
                    break

        # si no es consistente, probar otro valor
        if not Consistente:
            continue

        # seguir con las demas variables
        Resultado = Forward_checking(
            Variables,
            Dominios,
            Restricciones,
            Nueva_asignacion
        )

        if Resultado is not None:
            return Resultado

    # si no hay solucion
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

    Solucion = Forward_checking(
        Variables,
        Dominios,
        Restricciones
    )

    print("\nSolucion con comprobacion hacia delante:")
    print(Solucion)