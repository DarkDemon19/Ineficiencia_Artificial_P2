# Teoria de la utilidad: funcion de utilidad

def Utilidad_resultado(Resultado):
    # utilidad de cada resultado
    Tabla_utilidad = {
        "ruta_rapida_y_barata": 100,
        "ruta_rapida_y_cara": 60,
        "ruta_lenta_y_barata": 50,
        "ruta_lenta_y_cara": -20
    }

    return Tabla_utilidad[Resultado]

def Utilidad_esperada(Accion, Probabilidades):
    # calcular utilidad esperada
    Total = 0

    for Resultado, Probabilidad in Probabilidades[Accion]:
        Utilidad = Utilidad_resultado(Resultado)
        Total += Probabilidad * Utilidad

    return Total

def Elegir_mejor_accion(Acciones, Probabilidades):
    # elegir accion con mayor utilidad
    Mejor_accion = None
    Mejor_valor = None

    for Accion in Acciones:
        UE = Utilidad_esperada(Accion, Probabilidades)

        print("Utilidad esperada de", Accion, "=", UE)

        if Mejor_accion is None or UE > Mejor_valor:
            Mejor_accion = Accion
            Mejor_valor = UE

    return Mejor_accion, Mejor_valor

if __name__ == "__main__":

    # acciones posibles
    Acciones_posibles = [
        "ir_a_Cine",
        "ir_a_Hospital",
        "ir_a_Garaje"
    ]

    # probabilidades segun cada accion
    Probabilidades = {
        "ir_a_Cine": [
            ("ruta_rapida_y_cara", 0.7),
            ("ruta_lenta_y_cara", 0.3)
        ],
        "ir_a_Hospital": [
            ("ruta_rapida_y_barata", 0.8),
            ("ruta_lenta_y_barata", 0.2)
        ],
        "ir_a_Garaje": [
            ("ruta_lenta_y_barata", 0.6),
            ("ruta_lenta_y_cara", 0.4)
        ]
    }

    # elegir mejor accion
    Accion, Valor = Elegir_mejor_accion(
        Acciones_posibles,
        Probabilidades
    )

    print("\nMejor decision segun utilidad:", Accion)
    print("Utilidad esperada:", Valor)