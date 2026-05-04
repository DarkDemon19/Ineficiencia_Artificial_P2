# Iteracion de valores

def Iteracion_de_valores(
    Estados,
    Acciones_por_estado,
    Transicion,
    Recompensa,
    Descuento,
    Pasos_max
):
    # inicializar valores
    Valores = {}

    for Estado in Estados:
        Valores[Estado] = 0

    # actualizar varias veces
    for _ in range(Pasos_max):
        Nuevos_valores = {}

        for Estado in Estados:
            Acciones = Acciones_por_estado[Estado]

            # si no hay acciones
            if len(Acciones) == 0:
                Nuevos_valores[Estado] = 0

            else:
                Estimaciones = []

                # evaluar cada accion
                for Accion in Acciones:
                    Siguiente = Transicion(Estado, Accion)
                    Ganancia = Recompensa(Estado, Accion)

                    Estimado = (
                        Ganancia +
                        Descuento * Valores[Siguiente]
                    )

                    Estimaciones.append(Estimado)

                # guardar mejor opcion
                Nuevos_valores[Estado] = max(Estimaciones)

        # actualizar valores
        Valores = Nuevos_valores

    return Valores

def Politica_greedy(
    Estados,
    Acciones_por_estado,
    Transicion,
    Recompensa,
    Valores,
    Descuento
):
    # mejor accion por estado
    Politica = {}

    for Estado in Estados:
        Acciones = Acciones_por_estado[Estado]

        if len(Acciones) == 0:
            Politica[Estado] = None

        else:
            Mejor_accion = None
            Mejor_score = None

            for Accion in Acciones:
                Siguiente = Transicion(Estado, Accion)
                Ganancia = Recompensa(Estado, Accion)

                Score = (
                    Ganancia +
                    Descuento * Valores[Siguiente]
                )

                if Mejor_accion is None or Score > Mejor_score:
                    Mejor_accion = Accion
                    Mejor_score = Score

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

    def Transicion(Estado, Accion):
        # transiciones del mapa
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

    def Recompensa(Estado, Accion):
        # recompensa basada en menor costo
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
    Pasos_max = 15

    Valores_finales = Iteracion_de_valores(
        Estados,
        Acciones_por_estado,
        Transicion,
        Recompensa,
        Descuento,
        Pasos_max
    )

    print("Valores estimados:")
    for Estado in Estados:
        print(Estado, "->", Valores_finales[Estado])

    Politica = Politica_greedy(
        Estados,
        Acciones_por_estado,
        Transicion,
        Recompensa,
        Valores_finales,
        Descuento
    )

    print("\nPolitica recomendada:")
    for Estado in Estados:
        print(Estado, "->", Politica[Estado])