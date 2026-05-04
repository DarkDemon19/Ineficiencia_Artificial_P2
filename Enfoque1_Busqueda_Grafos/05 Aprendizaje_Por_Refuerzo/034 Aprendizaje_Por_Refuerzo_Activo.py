# Aprendizaje por refuerzo activo
import random

def Elegir_accion(Q, Estado, Acciones_disponibles, Prob_explorar):
    # elegir accion
    if random.random() < Prob_explorar:
        return random.choice(Acciones_disponibles[Estado])

    Mejor_accion = None
    Mejor_valor = None

    for Accion in Acciones_disponibles[Estado]:
        Valor_q = Q[Estado][Accion]

        if Mejor_accion is None or Valor_q > Mejor_valor:
            Mejor_accion = Accion
            Mejor_valor = Valor_q

    return Mejor_accion

def Correr_un_episodio(
    Q,
    Acciones_disponibles,
    Transicion,
    Recompensa_final,
    Estado_inicial,
    Prob_explorar,
    Tasa_aprendizaje
):
    # iniciar episodio
    Estado_actual = Estado_inicial
    Historial = []

    while True:

        # si ya no hay acciones
        if len(Acciones_disponibles[Estado_actual]) == 0:
            break

        # elegir accion
        Accion = Elegir_accion(
            Q,
            Estado_actual,
            Acciones_disponibles,
            Prob_explorar
        )

        # guardar paso
        Historial.append((Estado_actual, Accion))

        # avanzar
        Estado_siguiente = Transicion(
            Estado_actual,
            Accion
        )

        Estado_actual = Estado_siguiente

    # recompensa final
    Recompensa = Recompensa_final(Estado_actual)

    # actualizar Q
    for Estado_visitado, Accion_tomada in Historial:
        Valor_anterior = Q[Estado_visitado][Accion_tomada]

        Q[Estado_visitado][Accion_tomada] = (
            Valor_anterior +
            Tasa_aprendizaje *
            (Recompensa - Valor_anterior)
        )

    return Recompensa

def Politica_aprendida(Q, Acciones_disponibles):
    # obtener mejor accion
    Politica = {}

    for Estado in Acciones_disponibles:

        if len(Acciones_disponibles[Estado]) == 0:
            Politica[Estado] = None

        else:
            Mejor_accion = None
            Mejor_valor = None

            for Accion in Acciones_disponibles[Estado]:
                Valor_q = Q[Estado][Accion]

                if Mejor_accion is None or Valor_q > Mejor_valor:
                    Mejor_accion = Accion
                    Mejor_valor = Valor_q

            Politica[Estado] = Mejor_accion

    return Politica

if __name__ == "__main__":

    # estados
    Estados = [
        "Casa",
        "Autolavado",
        "Estetica",
        "Tacon",
        "Ammu_Nation",
        "Hospital",
        "Garaje",
        "Concesionario",
        "Cine"
    ]

    # acciones disponibles
    Acciones_disponibles = {
        "Casa": [
            "ir_Autolavado",
            "ir_Estetica",
            "ir_Hospital"
        ],

        "Autolavado": [
            "ir_Tacon"
        ],

        "Estetica": [
            "ir_Garaje"
        ],

        "Tacon": [
            "ir_Ammu_Nation",
            "ir_Hospital"
        ],

        "Ammu_Nation": [
            "ir_Concesionario",
            "ir_Cine"
        ],

        "Hospital": [],
        "Garaje": [],
        "Concesionario": [],
        "Cine": []
    }

    def Transicion(Estado, Accion):
        # transiciones
        if Estado == "Casa" and Accion == "ir_Autolavado":
            return "Autolavado"

        if Estado == "Casa" and Accion == "ir_Estetica":
            return "Estetica"

        if Estado == "Casa" and Accion == "ir_Hospital":
            return "Hospital"

        if Estado == "Autolavado" and Accion == "ir_Tacon":
            return "Tacon"

        if Estado == "Estetica" and Accion == "ir_Garaje":
            return "Garaje"

        if Estado == "Tacon" and Accion == "ir_Ammu_Nation":
            return "Ammu_Nation"

        if Estado == "Tacon" and Accion == "ir_Hospital":
            return "Hospital"

        if Estado == "Ammu_Nation" and Accion == "ir_Concesionario":
            return "Concesionario"

        if Estado == "Ammu_Nation" and Accion == "ir_Cine":
            return "Cine"

        return Estado

    def Recompensa_final(Estado):
        # recompensa distinta por destino final
        if Estado == "Hospital":
            return random.randint(40, 60)

        if Estado == "Garaje":
            return random.randint(55, 75)

        if Estado == "Concesionario":
            return random.randint(80, 95)

        if Estado == "Cine":
            return random.randint(95, 120)

        return 0

    # inicializar Q
    Q = {}

    for Estado in Acciones_disponibles:
        Q[Estado] = {}

        for Accion in Acciones_disponibles[Estado]:
            Q[Estado][Accion] = 0.0

    # parametros
    Prob_explorar = 0.3
    Tasa_aprendizaje = 0.5

    # entrenar
    Recompensas_obtenidas = []

    for _ in range(30):
        Recompensa_ep = Correr_un_episodio(
            Q,
            Acciones_disponibles,
            Transicion,
            Recompensa_final,
            Estado_inicial="Casa",
            Prob_explorar=Prob_explorar,
            Tasa_aprendizaje=Tasa_aprendizaje
        )

        Recompensas_obtenidas.append(Recompensa_ep)

    # mostrar Q
    print("Tabla Q aprendida:")

    for Estado in Q:
        for Accion in Q[Estado]:
            print(
                Estado,
                ",",
                Accion,
                "->",
                Q[Estado][Accion]
            )

    # politica final
    Politica = Politica_aprendida(
        Q,
        Acciones_disponibles
    )

    print("\nPolitica aprendida:")

    for Estado in Politica:
        print(
            Estado,
            "->",
            Politica[Estado]
        )

    print("\nRecompensas por episodio:")
    print(Recompensas_obtenidas)