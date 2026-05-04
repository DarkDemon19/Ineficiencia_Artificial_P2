# Aprendizaje por refuerzo pasivo
import random

def Simular_episodio(Politica, Transicion, Recompensa, Estado_inicial):
    # correr un episodio con politica fija
    Estado_actual = Estado_inicial
    Recorrido = []

    while True:
        Recorrido.append(Estado_actual)

        # si ya no hay accion
        if Politica.get(Estado_actual) is None:
            break

        Accion = Politica[Estado_actual]
        Estado_siguiente = Transicion(Estado_actual, Accion)

        Estado_actual = Estado_siguiente

    # recompensa final
    Recompensa_final = Recompensa(Estado_actual)

    # guardar retorno para cada estado
    Retorno_por_estado = []

    for Estado in Recorrido:
        Retorno_por_estado.append((Estado, Recompensa_final))

    return Retorno_por_estado

def Aprender_valores_pasivo(
    Episodios,
    Politica,
    Transicion,
    Recompensa,
    Estado_inicial
):
    # guardar retornos
    Retornos = {}

    for _ in range(Episodios):
        Datos_ep = Simular_episodio(
            Politica,
            Transicion,
            Recompensa,
            Estado_inicial
        )

        for Estado, Retorno in Datos_ep:
            if Estado not in Retornos:
                Retornos[Estado] = []

            Retornos[Estado].append(Retorno)

    # calcular promedios
    Valores_estimados = {}

    for Estado in Retornos:
        Lista = Retornos[Estado]
        Promedio = sum(Lista) / len(Lista)
        Valores_estimados[Estado] = Promedio

    return Valores_estimados

if __name__ == "__main__":

    # estados
    Estados = [
        "Casa",
        "Autolavado",
        "Tacon",
        "Ammu_Nation",
        "Cine"
    ]

    # politica fija
    Politica = {
        "Casa": "ir_Autolavado",
        "Autolavado": "ir_Tacon",
        "Tacon": "ir_Ammu_Nation",
        "Ammu_Nation": "ir_Cine",
        "Cine": None
    }

    def Transicion(Estado, Accion):
        # transiciones de la politica
        if Estado == "Casa" and Accion == "ir_Autolavado":
            return "Autolavado"

        if Estado == "Autolavado" and Accion == "ir_Tacon":
            return "Tacon"

        if Estado == "Tacon" and Accion == "ir_Ammu_Nation":
            return "Ammu_Nation"

        if Estado == "Ammu_Nation" and Accion == "ir_Cine":
            return "Cine"

        return Estado

    def Recompensa(Estado):
        # recompensa al llegar al objetivo
        if Estado == "Cine":
            return random.randint(90, 110)

        return 0

    # aprender valores siguiendo politica fija
    Valores = Aprender_valores_pasivo(
        Episodios=20,
        Politica=Politica,
        Transicion=Transicion,
        Recompensa=Recompensa,
        Estado_inicial="Casa"
    )

    print("Valores aprendidos:")
    for Estado in Valores:
        print(Estado, "->", Valores[Estado])