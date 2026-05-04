# Valor de la informacion

def Utilidad_final(Resultado):
    # utilidad de cada resultado final
    Tabla = {
        "llego_cine_rapido": 100,
        "llego_cine_lento": 40,
        "llego_hospital_rapido": 90,
        "llego_hospital_lento": 50,
        "no_ir": 0
    }

    return Tabla[Resultado]

def Utilidad_esperada_sin_info(Prob_rapido, Prob_lento):
    # decision directa sin revisar trafico

    # opcion:
    # ir al Cine
    UE_cine = (
        Prob_rapido * Utilidad_final("llego_cine_rapido") +
        Prob_lento * Utilidad_final("llego_cine_lento")
    )

    # opcion:
    # ir al Hospital
    UE_hospital = (
        Prob_rapido * Utilidad_final("llego_hospital_rapido") +
        Prob_lento * Utilidad_final("llego_hospital_lento")
    )

    # opcion:
    # no salir
    UE_no_ir = Utilidad_final("no_ir")

    # elegir mejor opcion
    Mejor_accion = "no_ir"
    Mejor_utilidad = UE_no_ir

    if UE_cine > Mejor_utilidad:
        Mejor_accion = "ir_Cine"
        Mejor_utilidad = UE_cine

    if UE_hospital > Mejor_utilidad:
        Mejor_accion = "ir_Hospital"
        Mejor_utilidad = UE_hospital

    return Mejor_accion, Mejor_utilidad

def Utilidad_esperada_con_info(
    Prob_rapido,
    Prob_lento,
    Costo_revision,
    Calidad_revision
):
    # revisar trafico antes de salir

    # probabilidad de que el sistema diga "rapido"
    Prob_sistema_dice_rapido = (
        Prob_rapido * Calidad_revision +
        Prob_lento * (1 - Calidad_revision)
    )

    # probabilidad de que diga "lento"
    Prob_sistema_dice_lento = 1 - Prob_sistema_dice_rapido

    # si dice rapido
    if Prob_sistema_dice_rapido > 0:
        Prob_real_rapido = (
            Prob_rapido * Calidad_revision
        ) / Prob_sistema_dice_rapido
    else:
        Prob_real_rapido = 0

    if Prob_sistema_dice_rapido > 0:
        Prob_real_lento = (
            Prob_lento * (1 - Calidad_revision)
        ) / Prob_sistema_dice_rapido
    else:
        Prob_real_lento = 0

    # decision:
    # si sistema dice rapido -> ir al Cine
    UE_si_dice_rapido = (
        Prob_real_rapido * Utilidad_final("llego_cine_rapido") +
        Prob_real_lento * Utilidad_final("llego_cine_lento")
    )

    # si sistema dice lento -> ir al Hospital
    UE_si_dice_lento = (
        Utilidad_final("llego_hospital_lento")
    )

    # utilidad total con informacion
    UE_total = (
        Prob_sistema_dice_rapido * UE_si_dice_rapido +
        Prob_sistema_dice_lento * UE_si_dice_lento
    )

    # restar costo de revisar
    UE_total -= Costo_revision

    return UE_total

if __name__ == "__main__":

    # probabilidad general de trafico
    Prob_rapido = 0.6
    Prob_lento = 0.4

    # sin informacion
    Mejor_sin_info, Utilidad_sin_info = Utilidad_esperada_sin_info(
        Prob_rapido,
        Prob_lento
    )

    print("Sin informacion extra:")
    print("  Mejor decision:", Mejor_sin_info)
    print("  Utilidad esperada:", Utilidad_sin_info)

    # con informacion
    Costo_revision = 5
    Calidad_revision = 0.9

    Utilidad_con_info = Utilidad_esperada_con_info(
        Prob_rapido,
        Prob_lento,
        Costo_revision,
        Calidad_revision
    )

    print("\nCon informacion extra:")
    print("  Utilidad esperada:", Utilidad_con_info)

    # valor final de la informacion
    Valor_info = Utilidad_con_info - Utilidad_sin_info

    print("\nValor de la informacion:", Valor_info)

    # si Valor_info > 0
    # conviene revisar trafico antes de decidir