# Calcula el manto de Markov
# usando padres, hijos y copadres de un nodo

# estructura de la red
Red = {
    "a": {
        "padres": [],
        "hijos": ["b"]
    },

    "b": {
        "padres": ["a", "c"],
        "hijos": ["d"]
    },

    "c": {
        "padres": [],
        "hijos": ["b"]
    },

    "d": {
        "padres": ["b"],
        "hijos": []
    }
}

def Padres_de(Nodo, Red_local):
    # obtener padres directos
    return Red_local[Nodo]["padres"]

def Hijos_de(Nodo, Red_local):
    # obtener hijos directos
    return Red_local[Nodo]["hijos"]

def Copadres_de(Nodo, Red_local):
    # obtener otros padres de los hijos
    Resultado = set()

    for Hijo in Hijos_de(Nodo, Red_local):

        for Padre in Padres_de(Hijo, Red_local):

            if Padre != Nodo:
                Resultado.add(Padre)

    return list(Resultado)

def Manto_de_markov(Nodo, Red_local):
    # obtener padres
    Lista_padres = Padres_de(
        Nodo,
        Red_local
    )

    # obtener hijos
    Lista_hijos = Hijos_de(
        Nodo,
        Red_local
    )

    # obtener copadres
    Lista_copadres = Copadres_de(
        Nodo,
        Red_local
    )

    # unir todo sin repetir
    Conjunto = set(
        Lista_padres +
        Lista_hijos +
        Lista_copadres
    )

    # evitar incluir el mismo nodo
    if Nodo in Conjunto:
        Conjunto.remove(Nodo)

    return list(Conjunto)

# mostrar resultado
print(
    "Manto de Markov de b:",
    Manto_de_markov(
        "b",
        Red
    )
)