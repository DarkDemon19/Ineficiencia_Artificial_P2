# Implementa un sistema de recuperacion de documentos
# buscando textos que contengan todas las palabras de una consulta

# Para calculos numericos
import numpy as np

class Document_retrieval:
    def __init__(self):
        # base de documentos
        self.Documentos = {
            1: "El perro juega en el parque.",
            2: "El gato duerme en la casa.",
            3: "Los pajaros cantan en la mañana.",
            4: "El perro y el gato son amigos.",
            5: "Los niños juegan en el parque."
        }

    def Buscar(self, Consulta):
        # separar palabras de consulta
        Consulta_palabras = Consulta.lower().split()

        # guardar resultados
        Resultados = []

        # buscar coincidencias
        for Id_doc, Documento in self.Documentos.items():

            if all(
                Palabra in Documento.lower()
                for Palabra in Consulta_palabras
            ):
                Resultados.append(
                    Id_doc
                )

        return Resultados

# crear sistema de recuperacion
Sistema_recuperacion = Document_retrieval()

# definir consulta
Consulta = "perro parque"

# realizar busqueda
Resultados = Sistema_recuperacion.Buscar(
    Consulta
)

# mostrar resultados
print(
    "Documentos encontrados para la consulta:",
    Consulta
)

for Doc_id in Resultados:
    print(
        f"Documento {Doc_id}: {Sistema_recuperacion.Documentos[Doc_id]}"
    )