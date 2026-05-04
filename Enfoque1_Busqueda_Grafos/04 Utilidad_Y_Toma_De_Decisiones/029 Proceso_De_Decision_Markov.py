# MDP proceso de decision de Markov

def Iteracion_de_valores_mdp(
    Estados,
    Acciones_por_estado,
    Transicion_prob,
    Recompensa,
    Descuento,
    Pasos_max
):
    # iniciar valores
    Valores = {}

    for Estado in Estados:
        Valores[Estado] = 0

    # actualizar valores
    for _ in range(Pasos_max):
        Nuevos_valores = {}

        for Estado in Estados:
            Acciones = Acciones_por_estado[Estado]

            if len(Acciones) == 0:
                Nuevos_valores[Estado] = 0

            else:
                Estimaciones = []

                for Accion in Acciones:
                    Ganancia = Recompensa(Estado, Accion)

                    Valor_futuro = 0

                    for Siguiente, Probabilidad in Transicion_prob(Estado, Accion):
                        Valor_futuro += Probabilidad * Valores[Siguiente]

                    Q_valor = (
                        Ganancia +
                        Descuento * Valor_futuro
                    )

                    Estimaciones.append(Q_valor)

                Nuevos_valores[Estado] = max(Estimaciones)

        Valores = Nuevos_valores

    return Valores

def Politica_optima_mdp(
    Estados,
    Acciones_por_estado,
    Transicion_prob,
    Recompensa,
    Descuento,
    Valores
):
    # obtener mejor accion
    Politica = {}

    for Estado in Estados:
        Acciones = Acciones_por_estado[Estado]

        if len(Acciones) == 0:
            Politica[Estado] = None

        else:
            Mejor_accion = None
            Mejor_q = None

            for Accion in Acciones:
                Ganancia = Recompensa(Estado, Accion)

                Valor_futuro = 0

                for Siguiente, Probabilidad in Transicion_prob(Estado, Accion):
                    Valor_futuro += Probabilidad * Valores[Siguiente]

                Q_valor = (
                    Ganancia +
                    Descuento * Valor_futuro
                )

                if Mejor_accion is None or Q_valor > Mejor_q:
                    Mejor_accion = Accion
                    Mejor_q = Q_valor

            Politica[Estado] = Mejor_accion

    return Politica

if __name__ == "__main__":

    # estados basados en rutas principales
    Estados = [
        "Casa",
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

    # acciones posibles
    Acciones_por_estado = {
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
        "Autolavado": ["ir_Tacon"],
        "Estetica": ["ir_Garaje"],
        "Garaje": [],
        "Tacon": [
            "ir_Ammu_Nation",
            "ir_Paintspray",
            "ir_Hospital"
        ],
        "Ammu_Nation": [
            "ir_Concesionario",
            "ir_Cine"
        ],
        "Paintspray": [],
        "Hospital": [],
        "Concesionario": [],
        "Cine": []
    }

    def Transicion_prob(Estado, Accion):
        # transiciones con probabilidad
        if Estado == "Casa" and Accion == "ir_Autolavado":
            return [("Autolavado", 0.9), ("Estetica", 0.1)]

        if Estado == "Casa" and Accion == "ir_Estetica":
            return [("Estetica", 0.9), ("Autolavado", 0.1)]

        if Estado == "Casa" and Accion == "ir_Hospital":
            return [("Hospital", 0.85), ("Tacon", 0.15)]

        if Estado == "Casa" and Accion == "ir_Garaje":
            return [("Garaje", 0.85), ("Estetica", 0.15)]

        if Estado == "Casa" and Accion == "ir_Tacon":
            return [("Tacon", 0.9), ("Autolavado", 0.1)]

        if Estado == "Casa" and Accion == "ir_Paintspray":
            return [("Paintspray", 0.85), ("Tacon", 0.15)]

        if Estado == "Casa" and Accion == "ir_Ammu_Nation":
            return [("Ammu_Nation", 0.85), ("Tacon", 0.15)]

        if Estado == "Casa" and Accion == "ir_Concesionario":
            return [("Concesionario", 0.85), ("Ammu_Nation", 0.15)]

        if Estado == "Casa" and Accion == "ir_Cine":
            return [("Cine", 0.85), ("Ammu_Nation", 0.15)]

        if Estado == "Autolavado" and Accion == "ir_Tacon":
            return [("Tacon", 1.0)]

        if Estado == "Estetica" and Accion == "ir_Garaje":
            return [("Garaje", 1.0)]

        if Estado == "Tacon" and Accion == "ir_Ammu_Nation":
            return [("Ammu_Nation", 0.9), ("Hospital", 0.1)]

        if Estado == "Tacon" and Accion == "ir_Paintspray":
            return [("Paintspray", 0.9), ("Hospital", 0.1)]

        if Estado == "Tacon" and Accion == "ir_Hospital":
            return [("Hospital", 1.0)]

        if Estado == "Ammu_Nation" and Accion == "ir_Concesionario":
            return [("Concesionario", 1.0)]

        if Estado == "Ammu_Nation" and Accion == "ir_Cine":
            return [("Cine", 1.0)]

        return [(Estado, 1.0)]

    def Recompensa(Estado, Accion):
        # recompensa basada en costo
        Tabla_costos = {
            ("Casa", "ir_Autolavado"): -100,
            ("Casa", "ir_Estetica"): -550,
            ("Casa", "ir_Hospital"): -450,
            ("Casa", "ir_Garaje"): -650,
            ("Casa", "ir_Tacon"): -450,
            ("Casa", "ir_Paintspray"): -1650,
            ("Casa", "ir_Ammu_Nation"): -700,
            ("Casa", "ir_Concesionario"): -750,
            ("Casa", "ir_Cine"): -1600,

            ("Autolavado", "ir_Tacon"): -150,
            ("Estetica", "ir_Garaje"): -400,

            ("Tacon", "ir_Ammu_Nation"): -250,
            ("Tacon", "ir_Paintspray"): -950,
            ("Tacon", "ir_Hospital"): -250,

            ("Ammu_Nation", "ir_Concesionario"): -100,
            ("Ammu_Nation", "ir_Cine"): -600
        }

        return Tabla_costos.get((Estado, Accion), 0)

    Descuento = 0.9

    Valores = Iteracion_de_valores_mdp(
        Estados,
        Acciones_por_estado,
        Transicion_prob,
        Recompensa,
        Descuento,
        Pasos_max=15
    )

    print("Valores estimados de cada estado:")
    for Estado in Estados:
        print(Estado, "->", Valores[Estado])

    Politica = Politica_optima_mdp(
        Estados,
        Acciones_por_estado,
        Transicion_prob,
        Recompensa,
        Descuento,
        Valores
    )

    print("\nPolitica optima:")
    for Estado in Estados:
        print(Estado, "->", Politica[Estado])