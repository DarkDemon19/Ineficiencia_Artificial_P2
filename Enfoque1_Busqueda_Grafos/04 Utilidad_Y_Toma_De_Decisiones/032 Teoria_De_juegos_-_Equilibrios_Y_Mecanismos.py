# Teoria de juegos: equilibrios y mecanismos

def Mejor_respuesta_para_a(Eleccion_b, Estrategias, Pagos):
    # buscar mejor respuesta de A
    Mejor = None
    Mejor_utilidad = None

    for Opcion_a in Estrategias:
        Utilidad_a, _ = Pagos[Opcion_a][Eleccion_b]

        if Mejor is None or Utilidad_a > Mejor_utilidad:
            Mejor = Opcion_a
            Mejor_utilidad = Utilidad_a

    return Mejor

def Mejor_respuesta_para_b(Eleccion_a, Estrategias, Pagos):
    # buscar mejor respuesta de B
    Mejor = None
    Mejor_utilidad = None

    for Opcion_b in Estrategias:
        _, Utilidad_b = Pagos[Eleccion_a][Opcion_b]

        if Mejor is None or Utilidad_b > Mejor_utilidad:
            Mejor = Opcion_b
            Mejor_utilidad = Utilidad_b

    return Mejor

def Es_equilibrio_de_nash(A_juega, B_juega, Estrategias, Pagos):
    # revisar si ambos estan en su mejor respuesta
    Mejor_para_a = Mejor_respuesta_para_a(
        B_juega,
        Estrategias,
        Pagos
    )

    Mejor_para_b = Mejor_respuesta_para_b(
        A_juega,
        Estrategias,
        Pagos
    )

    return A_juega == Mejor_para_a and B_juega == Mejor_para_b

if __name__ == "__main__":

    # estrategias posibles
    Estrategias = [
        "ruta_barata",
        "ruta_rapida"
    ]

    # pagos:
    # Pagos[A][B] = (utilidad_A, utilidad_B)
    Pagos = {
        "ruta_barata": {
            "ruta_barata": (70, 70),
            "ruta_rapida": (40, 90)
        },
        "ruta_rapida": {
            "ruta_barata": (90, 40),
            "ruta_rapida": (50, 50)
        }
    }

    # probar combinaciones
    for A_juega in Estrategias:
        for B_juega in Estrategias:

            Utilidad_a, Utilidad_b = Pagos[A_juega][B_juega]

            Equilibrio = Es_equilibrio_de_nash(
                A_juega,
                B_juega,
                Estrategias,
                Pagos
            )

            print(
                "A juega:", A_juega,
                ", B juega:", B_juega,
                "=> utilidad A:", Utilidad_a,
                ", utilidad B:", Utilidad_b,
                ", equilibrio_nash?:", Equilibrio
            )