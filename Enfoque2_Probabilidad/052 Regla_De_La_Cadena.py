# Calcula probabilidad conjunta
# usando la regla de la cadena

def Probabilidad_conjunta(P_a, P_b_dado_a, P_c_dado_a_y_b):
    # aplicar formula de la regla de la cadena
    Resultado = P_a * P_b_dado_a * P_c_dado_a_y_b

    return Resultado

# calcular ejemplo
Probabilidad_total = Probabilidad_conjunta(
    P_a=0.5,
    P_b_dado_a=0.4,
    P_c_dado_a_y_b=0.8
)

# mostrar resultados
print(
    "Probabilidad conjunta P(a, b, c) =",
    Probabilidad_total
)

print(
    "En porcentaje eso es =",
    Probabilidad_total * 100,
    "%"
)