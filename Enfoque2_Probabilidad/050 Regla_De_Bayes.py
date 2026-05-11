# Aplica la regla de Bayes
# para actualizar probabilidades con nueva evidencia

def Probabilidad_bayes(Prior_enfermo, Sensibilidad_prueba, Falso_positivo):
    # probabilidad inicial
    P_a = Prior_enfermo

    # probabilidad de no estar enfermo
    P_no_a = 1 - P_a

    # probabilidad de positivo si esta enfermo
    P_b_dado_a = Sensibilidad_prueba

    # probabilidad de positivo si esta sano
    P_b_dado_no_a = Falso_positivo

    # calcular numerador
    Numerador = P_b_dado_a * P_a

    # calcular denominador
    Denominador = (
        (P_b_dado_a * P_a) +
        (P_b_dado_no_a * P_no_a)
    )

    # resultado final
    return Numerador / Denominador

# ejecutar ejemplo
Resultado = Probabilidad_bayes(
    Prior_enfermo=0.01,
    Sensibilidad_prueba=0.90,
    Falso_positivo=0.05
)

# mostrar resultados
print(
    "Probabilidad real de estar enfermo si la prueba fue positiva =",
    Resultado
)

print(
    "En porcentaje eso es =",
    Resultado * 100,
    "%"
)