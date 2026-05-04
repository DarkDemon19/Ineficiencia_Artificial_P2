# Propagacion de restricciones
from collections import deque

def Compatibles(Variable_x, Valor_x, Variable_y, Dominio_y, Restriccion_binaria):
    # revisar si Valor_x tiene alguna combinacion valida con Variable_y
    for Valor_y in Dominio_y:
        if Restriccion_binaria(Variable_x, Valor_x, Variable_y, Valor_y):
            return True

    return False

def Revisar_arco(Variable_x, Variable_y, Dominios, Restriccion_binaria):
    # limpiar dominio de Variable_x usando Variable_y
    Dominio_x = Dominios[Variable_x]
    Dominio_y = Dominios[Variable_y]

    Quitar = []

    for Valor_x in Dominio_x:
        if not Compatibles(
            Variable_x,
            Valor_x,
            Variable_y,
            Dominio_y,
            Restriccion_binaria
        ):
            Quitar.append(Valor_x)

    # quitar valores no validos
    if Quitar:
        for Valor in Quitar:
            Dominio_x.remove(Valor)

        return True

    return False

def AC3(Variables, Dominios, Vecinos, Restriccion_binaria):
    # crear cola con arcos
    Cola = deque()

    for Variable_x in Variables:
        for Variable_y in Vecinos[Variable_x]:
            Cola.append((Variable_x, Variable_y))

    # procesar cola
    while Cola:
        Variable_x, Variable_y = Cola.popleft()

        Cambio = Revisar_arco(
            Variable_x,
            Variable_y,
            Dominios,
            Restriccion_binaria
        )

        if Cambio:
            # si un dominio queda vacio, no hay solucion
            if len(Dominios[Variable_x]) == 0:
                return False

            # revisar vecinos afectados
            for Variable_z in Vecinos[Variable_x]:
                if Variable_z != Variable_y:
                    Cola.append((Variable_z, Variable_x))

    return True

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

    # vecinos segun conexiones del CSV
    Vecinos = {
        "Autolavado": ["Tacon"],
        "Estetica": ["Garaje"],
        "Garaje": ["Estetica"],
        "Tacon": ["Autolavado", "Ammu_Nation", "Paintspray", "Hospital"],
        "Ammu_Nation": ["Tacon", "Concesionario", "Cine"],
        "Paintspray": ["Tacon"],
        "Hospital": ["Tacon"],
        "Concesionario": ["Ammu_Nation"],
        "Cine": ["Ammu_Nation"]
    }

    # restriccion:
    # nodos conectados no pueden tener la misma zona
    def Restriccion_binaria(Variable_x, Valor_x, Variable_y, Valor_y):
        if Variable_y in Vecinos.get(Variable_x, []):
            return Valor_x != Valor_y

        return True

    # ejecutar AC3
    Consistente = AC3(
        Variables,
        Dominios,
        Vecinos,
        Restriccion_binaria
    )

    print("¿Es consistente?:", Consistente)

    print("\nDominios despues de AC3:")
    for Variable in Variables:
        print(Variable, "->", Dominios[Variable])