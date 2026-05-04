# Busqueda de la politica
import random

def Simular_con_politica(
    Politica,
    Transicion,
    Recompensa_final,
    Estado_inicial,
    Episodios
):
    # calcular score promedio
    Total = 0

    for _ in range(Episodios):
        Estado_actual = Estado_inicial

        # seguir politica
        while Estado_actual in Politica:
            Accion = Politica[Estado_actual]

            Estado_actual = Transicion(
                Estado_actual,
                Accion
            )

        # recompensa final
        Recompensa = Recompensa_final(
            Estado_actual
        )

        Total += Recompensa

    return Total / Episodios

def Mutar_politica(Politica, Acciones_disponibles):
    # copiar politica
    Nueva_politica = Politica.copy()

    # elegir estado aleatorio
    Estado_cambiar = random.choice(
        list(Politica.keys())
    )

    # opciones posibles
    Opciones = Acciones_disponibles[
        Estado_cambiar
    ]

    # cambiar accion
    if len(Opciones) > 1:
        Nueva_politica[Estado_cambiar] = random.choice(
            Opciones
        )

    else:
        Nueva_politica[Estado_cambiar] = Opciones[0]

    return Nueva_politica

if __name__ == "__main__":

    # acciones disponibles
    Acciones_disponibles = {
        "Casa": [
            "ir_Autolavado",
            "ir_Estetica",
            "ir_Hospital",
            "ir_Garaje",
            "ir_Tacon",
            "ir_Paintspray",
            "ir_Ammu_Nation",
            "ir_Concesionario",
            "ir_Cine"
        ],

        "Autolavado": [
            "ir_Tacon"
        ],

        "Estetica": [
            "ir_Garaje"
        ],

        "Tacon": [
            "ir_Ammu_Nation",
            "ir_Paintspray",
            "ir_Hospital"
        ],

        "Ammu_Nation": [
            "ir_Concesionario",
            "ir_Cine"
        ]
    }

    def Transicion(Estado, Accion):
        # transiciones
        if Estado == "Casa" and Accion == "ir_Autolavado":
            return "Autolavado"

        if Estado == "Casa" and Accion == "ir_Estetica":
            return "Estetica"

        if Estado == "Casa" and Accion == "ir_Hospital":
            return "Hospital"

        if Estado == "Casa" and Accion == "ir_Garaje":
            return "Garaje"

        if Estado == "Casa" and Accion == "ir_Tacon":
            return "Tacon"

        if Estado == "Casa" and Accion == "ir_Paintspray":
            return "Paintspray"

        if Estado == "Casa" and Accion == "ir_Ammu_Nation":
            return "Ammu_Nation"

        if Estado == "Casa" and Accion == "ir_Concesionario":
            return "Concesionario"

        if Estado == "Casa" and Accion == "ir_Cine":
            return "Cine"

        if Estado == "Autolavado" and Accion == "ir_Tacon":
            return "Tacon"

        if Estado == "Estetica" and Accion == "ir_Garaje":
            return "Garaje"

        if Estado == "Tacon" and Accion == "ir_Ammu_Nation":
            return "Ammu_Nation"

        if Estado == "Tacon" and Accion == "ir_Paintspray":
            return "Paintspray"

        if Estado == "Tacon" and Accion == "ir_Hospital":
            return "Hospital"

        if Estado == "Ammu_Nation" and Accion == "ir_Concesionario":
            return "Concesionario"

        if Estado == "Ammu_Nation" and Accion == "ir_Cine":
            return "Cine"

        return Estado

    def Recompensa_final(Estado_final):
        # recompensas por destino
        if Estado_final == "Autolavado":
            return 35

        if Estado_final == "Estetica":
            return 25

        if Estado_final == "Tacon":
            return 55

        if Estado_final == "Ammu_Nation":
            return 75

        if Estado_final == "Hospital":
            return 65

        if Estado_final == "Garaje":
            return 50

        if Estado_final == "Paintspray":
            return 45

        if Estado_final == "Concesionario":
            return 90

        if Estado_final == "Cine":
            return 100

        return 0

    # politica inicial
    Politica_actual = {
        "Casa": "ir_Estetica",
        "Autolavado": "ir_Tacon",
        "Estetica": "ir_Garaje",
        "Tacon": "ir_Paintspray",
        "Ammu_Nation": "ir_Concesionario"
    }

    print("Politica inicial:")
    print(Politica_actual)

    # score inicial
    Score_actual = Simular_con_politica(
        Politica_actual,
        Transicion,
        Recompensa_final,
        Estado_inicial="Casa",
        Episodios=20
    )

    print("Score promedio inicial:", Score_actual)

    # mejorar politica
    for Intento in range(10):

        Politica_nueva = Mutar_politica(
            Politica_actual,
            Acciones_disponibles
        )

        Score_nuevo = Simular_con_politica(
            Politica_nueva,
            Transicion,
            Recompensa_final,
            Estado_inicial="Casa",
            Episodios=20
        )

        print("\nIntento", Intento)
        print("Politica candidata:", Politica_nueva)
        print("Score candidato:", Score_nuevo)

        if Score_nuevo > Score_actual:
            Politica_actual = Politica_nueva
            Score_actual = Score_nuevo

            print("-> mejora aceptada")

        else:
            print("-> no mejora")

    print("\nPolitica final:")
    print(Politica_actual)

    print("Score final:", Score_actual)