# Q-learning
import random

def Elegir_accion(Q, Estado, Acciones_disponibles, Prob_explorar):
    # elegir accion con exploracion
    if len(Acciones_disponibles[Estado]) == 0:
        return None

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

def Max_q(Q, Estado, Acciones_disponibles):
    # obtener mejor valor Q
    if len(Acciones_disponibles[Estado]) == 0:
        return 0.0

    Mejor = None

    for Accion in Acciones_disponibles[Estado]:
        Valor = Q[Estado][Accion]

        if Mejor is None or Valor > Mejor:
            Mejor = Valor

    return Mejor

def Correr_q_learning(
    Estados,
    Acciones_disponibles,
    Transicion,
    Recompensa_step,
    Estado_inicial,
    Alpha,
    Gamma,
    Prob_explorar,
    Episodios_max
):
    # inicializar Q
    Q = {}

    for Estado in Estados:
        Q[Estado] = {}

        for Accion in Acciones_disponibles[Estado]:
            Q[Estado][Accion] = 0.0

    # entrenar episodios
    for _ in range(Episodios_max):
        Estado_actual = Estado_inicial

        while True:
            Accion = Elegir_accion(
                Q,
                Estado_actual,
                Acciones_disponibles,
                Prob_explorar
            )

            if Accion is None:
                break

            Estado_siguiente = Transicion(
                Estado_actual,
                Accion
            )

            Recompensa = Recompensa_step(
                Estado_actual,
                Accion,
                Estado_siguiente
            )

            Mejor_futuro = Max_q(
                Q,
                Estado_siguiente,
                Acciones_disponibles
            )

            Valor_viejo = Q[Estado_actual][Accion]

            # formula Q-learning
            Q[Estado_actual][Accion] = Valor_viejo + Alpha * (
                Recompensa + Gamma * Mejor_futuro - Valor_viejo
            )

            Estado_actual = Estado_siguiente

    return Q

def Politica_desde_Q(Q, Acciones_disponibles):
    # obtener politica final
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

    def Recompensa_step(Estado, Accion, Estado_siguiente):
        # recompensa segun llegada
        if Estado_siguiente == "Hospital":
            return random.randint(40, 60)

        if Estado_siguiente == "Garaje":
            return random.randint(55, 75)

        if Estado_siguiente == "Concesionario":
            return random.randint(80, 95)

        if Estado_siguiente == "Cine":
            return random.randint(95, 120)

        # penalizacion por costo de ruta
        if Estado == "Casa" and Accion == "ir_Autolavado":
            return -100

        if Estado == "Casa" and Accion == "ir_Estetica":
            return -550

        if Estado == "Casa" and Accion == "ir_Hospital":
            return -450

        if Estado == "Autolavado" and Accion == "ir_Tacon":
            return -150

        if Estado == "Estetica" and Accion == "ir_Garaje":
            return -400

        if Estado == "Tacon" and Accion == "ir_Ammu_Nation":
            return -250

        if Estado == "Tacon" and Accion == "ir_Hospital":
            return -250

        if Estado == "Ammu_Nation" and Accion == "ir_Concesionario":
            return -100

        if Estado == "Ammu_Nation" and Accion == "ir_Cine":
            return -600

        return 0

    # parametros
    Alpha = 0.5
    Gamma = 0.9
    Prob_explorar = 0.3
    Episodios_max = 50

    Q_aprendido = Correr_q_learning(
        Estados,
        Acciones_disponibles,
        Transicion,
        Recompensa_step,
        Estado_inicial="Casa",
        Alpha=Alpha,
        Gamma=Gamma,
        Prob_explorar=Prob_explorar,
        Episodios_max=Episodios_max
    )

    print("Tabla Q aprendida:")

    for Estado in Q_aprendido:
        for Accion in Q_aprendido[Estado]:
            print(
                Estado,
                ",",
                Accion,
                "->",
                Q_aprendido[Estado][Accion]
            )

    Politica = Politica_desde_Q(
        Q_aprendido,
        Acciones_disponibles
    )

    print("\nPolitica sugerida:")

    for Estado in Politica:
        print(
            Estado,
            "->",
            Politica[Estado]
        )