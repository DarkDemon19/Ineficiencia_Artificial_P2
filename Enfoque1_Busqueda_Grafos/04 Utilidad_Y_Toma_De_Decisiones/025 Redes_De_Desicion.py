# Redes de decision

def Utilidad_resultado(Resultado):
    # utilidad de cada resultado
    Tabla = {
        "cine_rapido_barato": 100,
        "cine_rapido_caro": 60,
        "cine_lento_caro": -20,

        "hospital_rapido_barato": 90,
        "hospital_lento_barato": 50,
        "hospital_lento_caro": -30,

        "garaje_rapido_barato": 80,
        "garaje_lento_barato": 40,
        "garaje_lento_caro": -40
    }

    return Tabla[Resultado]

def Utilidad_esperada_accion(Accion, Tabla_prob):
    # calcular utilidad esperada de una accion
    Total = 0

    for Resultado, Probabilidad in Tabla_prob[Accion]:
        Utilidad = Utilidad_resultado(Resultado)
        Total += Probabilidad * Utilidad

    return Total

def Mejor_decision(Acciones, Tabla_prob):
    # elegir accion con mayor utilidad esperada
    Mejor_accion = None
    Mejor_valor = None

    for Accion in Acciones:
        UE = Utilidad_esperada_accion(Accion, Tabla_prob)

        print("Utilidad esperada de", Accion, "=", UE)

        if Mejor_accion is None or UE > Mejor_valor:
            Mejor_accion = Accion
            Mejor_valor = UE

    return Mejor_accion, Mejor_valor

if __name__ == "__main__":

    # acciones posibles
    Acciones = [
        "ir_a_Cine",
        "ir_a_Hospital",
        "ir_a_Garaje"
    ]

    # probabilidades segun cada decision
    Probabilidades = {
        "ir_a_Cine": [
            ("cine_rapido_barato", 0.2),
            ("cine_rapido_caro", 0.5),
            ("cine_lento_caro", 0.3)
        ],
        "ir_a_Hospital": [
            ("hospital_rapido_barato", 0.7),
            ("hospital_lento_barato", 0.2),
            ("hospital_lento_caro", 0.1)
        ],
        "ir_a_Garaje": [
            ("garaje_rapido_barato", 0.4),
            ("garaje_lento_barato", 0.4),
            ("garaje_lento_caro", 0.2)
        ]
    }

    # ejecutar red de decision
    Mejor, Valor = Mejor_decision(
        Acciones,
        Probabilidades
    )

    print("\nMejor decision segun la red de decision:", Mejor)
    print("Utilidad esperada:", Valor)