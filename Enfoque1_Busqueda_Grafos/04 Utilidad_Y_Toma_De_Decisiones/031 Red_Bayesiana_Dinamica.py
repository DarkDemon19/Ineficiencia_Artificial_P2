# Red bayesiana dinamica

def Prob_siguiente(Creencia_actual, Transicion):
    # calcular creencia del siguiente momento

    Prob_libre = Creencia_actual["ruta_libre"]
    Prob_trafico = Creencia_actual["trafico"]

    Prob_siguiente_libre = (
        Prob_libre * Transicion["ruta_libre"]["ruta_libre"] +
        Prob_trafico * Transicion["trafico"]["ruta_libre"]
    )

    Prob_siguiente_trafico = (
        Prob_libre * Transicion["ruta_libre"]["trafico"] +
        Prob_trafico * Transicion["trafico"]["trafico"]
    )

    return {
        "ruta_libre": Prob_siguiente_libre,
        "trafico": Prob_siguiente_trafico
    }

if __name__ == "__main__":

    # creencia actual
    Creencia_actual = {
        "ruta_libre": 0.6,
        "trafico": 0.4
    }

    # tabla de transicion
    Transicion = {
        "ruta_libre": {
            "ruta_libre": 0.75,
            "trafico": 0.25
        },
        "trafico": {
            "ruta_libre": 0.35,
            "trafico": 0.65
        }
    }

    print("Creencia actual:")
    print(Creencia_actual)

    # calcular siguiente creencia
    Creencia_siguiente = Prob_siguiente(
        Creencia_actual,
        Transicion
    )

    print("\nCreencia siguiente:")
    print(Creencia_siguiente)

    # calcular otra actualizacion
    Creencia_despues = Prob_siguiente(
        Creencia_siguiente,
        Transicion
    )

    print("\nCreencia despues de otro paso:")
    print(Creencia_despues)