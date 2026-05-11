# Calcula probabilidad condicionada
# y normaliza valores para que sumen 1

# probabilidades iniciales
P_gato = 0.6
P_viento = 0.4

# valores con evidencia nueva
P_gato_dado_ventana = 0.9
P_viento_dado_ventana = 0.2

# sumar valores crudos
Suma_cruda = P_gato_dado_ventana + P_viento_dado_ventana

# normalizar probabilidades
P_gato_normalizado = P_gato_dado_ventana / Suma_cruda
P_viento_normalizado = P_viento_dado_ventana / Suma_cruda

# mostrar probabilidades
print(
    "Probabilidad de gato dado ventana cerrada =",
    P_gato_normalizado
)

print(
    "Probabilidad de viento dado ventana cerrada =",
    P_viento_normalizado
)

# mostrar porcentajes
print(
    "Gato con ventana cerrada en porcentaje =",
    P_gato_normalizado * 100,
    "%"
)

print(
    "Viento con ventana cerrada en porcentaje =",
    P_viento_normalizado * 100,
    "%"
)