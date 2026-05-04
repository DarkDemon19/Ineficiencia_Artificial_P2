# Exploracion vs explotacion
import random

def Elegir_accion(Q_estado, Acciones, Prob_explorar):
    # explorar
    if random.random() < Prob_explorar:
        Accion = random.choice(Acciones)
        return Accion, "explorar"

    # explotar
    Mejor_accion = None
    Mejor_valor = None

    for Accion in Acciones:
        Valor_q = Q_estado[Accion]

        if Mejor_accion is None or Valor_q > Mejor_valor:
            Mejor_accion = Accion
            Mejor_valor = Valor_q

    return Mejor_accion, "explotar"

if __name__ == "__main__":

    # acciones disponibles desde Casa
    Acciones = [
        "ir_Autolavado",
        "ir_Estetica",
        "ir_Hospital",
        "ir_Garaje",
        "ir_Tacon",
        "ir_Paintspray",
        "ir_Ammu_Nation",
        "ir_Concesionario",
        "ir_Cine"
    ]

    # valores Q basados en costos
    # menor costo es mejor, por eso se usan valores negativos
    Q_estado = {
        "ir_Autolavado": -100,
        "ir_Estetica": -550,
        "ir_Hospital": -450,
        "ir_Garaje": -650,
        "ir_Tacon": -450,
        "ir_Paintspray": -1650,
        "ir_Ammu_Nation": -700,
        "ir_Concesionario": -750,
        "ir_Cine": -1600
    }

    Prob_explorar = 0.3

    Conteo_explorar = 0
    Conteo_explotar = 0

    print("Simulacion de decisiones:")

    for Paso in range(20):
        Accion_elegida, Modo = Elegir_accion(
            Q_estado,
            Acciones,
            Prob_explorar
        )

        if Modo == "explorar":
            Conteo_explorar += 1
        else:
            Conteo_explotar += 1

        print(
            "Paso",
            Paso,
            "-> accion:",
            Accion_elegida,
            "modo:",
            Modo
        )

    print("\nResumen final:")
    print("Veces que exploro:", Conteo_explorar)
    print("Veces que exploto:", Conteo_explotar)