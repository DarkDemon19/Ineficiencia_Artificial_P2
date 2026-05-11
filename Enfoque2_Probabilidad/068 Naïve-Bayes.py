# Implementa un clasificador Naïve Bayes
# calculando probabilidades y parametros gaussianos manualmente

# Para calculos numericos
import numpy as np

# Para manejar datos en tabla
import pandas as pd

# datos de ejemplo
Datos = {
    "Caracteristica1": [
        1.0,
        2.0,
        1.5,
        1.2,
        2.5,
        1.8,
        2.2,
        1.0,
        1.4,
        2.0
    ],

    "Caracteristica2": [
        0.5,
        1.5,
        1.0,
        0.7,
        2.0,
        1.5,
        1.8,
        0.6,
        1.1,
        1.4
    ],

    "Clase": [
        "A",
        "B",
        "A",
        "A",
        "B",
        "B",
        "A",
        "A",
        "B",
        "B"
    ]
}

# crear dataframe
Df = pd.DataFrame(
    Datos
)

def Calcular_probabilidades(Df):
    # calcular probabilidad inicial por clase
    Probabilidades_clase = {}

    Total_clases = len(
        Df
    )

    for Clase in Df["Clase"].unique():
        Probabilidades_clase[Clase] = len(
            Df[Df["Clase"] == Clase]
        ) / Total_clases

    return Probabilidades_clase

def Calcular_parametros(Df, Clase):
    # obtener datos de una clase
    Subset = Df[
        Df["Clase"] == Clase
    ]

    # calcular media
    Media = Subset[
        [
            "Caracteristica1",
            "Caracteristica2"
        ]
    ].mean()

    # calcular desviacion
    Desviacion = Subset[
        [
            "Caracteristica1",
            "Caracteristica2"
        ]
    ].std()

    return Media, Desviacion

def Probabilidad_gaussiana(X, Media, Desviacion):
    # calcular probabilidad gaussiana
    Exponente = np.exp(
        -((X - Media) ** 2) /
        (2 * Desviacion ** 2)
    )

    return (
        1 /
        (np.sqrt(2 * np.pi) * Desviacion)
    ) * Exponente

def Predecir(Df, Entrada):
    # calcular probabilidades de clase
    Probabilidades_clase = Calcular_probabilidades(
        Df
    )

    Clases = Df["Clase"].unique()

    Probabilidades = {}

    # evaluar cada clase
    for Clase in Clases:
        Media, Desviacion = Calcular_parametros(
            Df,
            Clase
        )

        Prob_total = Probabilidades_clase[
            Clase
        ]

        for Indice in range(len(Entrada)):
            Prob_total *= Probabilidad_gaussiana(
                Entrada[Indice],
                Media.iloc[Indice],
                Desviacion.iloc[Indice]
            )

        Probabilidades[Clase] = Prob_total

    return max(
        Probabilidades,
        key=Probabilidades.get
    )

# nueva entrada
Nueva_entrada = [
    1.5,
    1.0
]

# predecir clase
Clase_predicha = Predecir(
    Df,
    Nueva_entrada
)

# mostrar resultado
print(
    "La clase predicha para la entrada",
    Nueva_entrada,
    "es:",
    Clase_predicha
)