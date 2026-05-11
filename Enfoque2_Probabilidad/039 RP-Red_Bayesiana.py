# Guarda y consulta probabilidades condicionales
# usando una red bayesiana simple

# Para crear Red Bayesiana
from collections import defaultdict

class Red_bayesiana:
    def __init__(self):
        # guardar probabilidades
        self.Probabilidades = defaultdict(dict)

    def Agregar_probabilidad(self, Evento, Dado_evento, Probabilidad):
        # agregar probabilidad condicional
        self.Probabilidades[Evento][Dado_evento] = Probabilidad

    def Calcular_probabilidad(self, Evento, Dado_evento):
        # consultar probabilidad
        return self.Probabilidades[Evento].get(
            Dado_evento,
            "Probabilidad no definida en la red."
        )

    def Mostrar_probabilidades(self):
        # mostrar probabilidades guardadas
        for Evento, Condicionadas in self.Probabilidades.items():
            for Dado_evento, Probabilidad in Condicionadas.items():
                print(f"P({Evento} | {Dado_evento}) = {Probabilidad}")

# crear red bayesiana
Red = Red_bayesiana()

# agregar probabilidades
Red.Agregar_probabilidad("Emmanuel", "Fernanda", 0.7)
Red.Agregar_probabilidad("Emiliano", "Fernanda", 0.6)
Red.Agregar_probabilidad("Fernanda", "Emiliano", 0.8)

# consultar probabilidades
Prob_emmanuel_dado_fernanda = Red.Calcular_probabilidad(
    "Emmanuel",
    "Fernanda"
)

Prob_emiliano_dado_fernanda = Red.Calcular_probabilidad(
    "Emiliano",
    "Fernanda"
)

# mostrar resultados
print("\nResultados de la Red Bayesiana:")
print("Probabilidad de Emmanuel dado Fernanda:", Prob_emmanuel_dado_fernanda)
print("Probabilidad de Emiliano dado Fernanda:", Prob_emiliano_dado_fernanda)

# mostrar tabla de probabilidades
print("\nProbabilidades en la Red:")
Red.Mostrar_probabilidades()