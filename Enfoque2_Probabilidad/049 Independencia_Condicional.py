# Calcula probabilidad de llegar tarde
# dependiendo de si existe trafico o no

def Probabilidad_llegar_tarde(Hay_trafico):
    # evaluar probabilidad segun trafico

    if Hay_trafico:
        # trafico alto
        return 0.9

    else:
        # trafico bajo
        return 0.1

# calcular escenarios
Probabilidad_con_trafico = Probabilidad_llegar_tarde(
    True
)

Probabilidad_sin_trafico = Probabilidad_llegar_tarde(
    False
)

# mostrar resultados
print(
    "Probabilidad de llegar tarde si hay trafico =",
    Probabilidad_con_trafico
)

print(
    "Probabilidad de llegar tarde si NO hay trafico =",
    Probabilidad_sin_trafico
)