# Implementa extraccion de informacion en texto
# identificando nombres y fechas con expresiones regulares

# Para expresiones regulares
import re

class Extraccion_informacion:
    def __init__(self, Texto):
        # guardar texto
        self.Texto = Texto

    def Extraer_nombres(self):
        # patron para Nombre Apellido
        Patron = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"

        # buscar nombres
        Nombres = re.findall(
            Patron,
            self.Texto
        )

        # eliminar repetidos
        return list(
            set(Nombres)
        )

    def Extraer_fechas(self):
        # patron para fechas
        Patron = r"\b\d{1,2}[-/]\d{1,2}[-/]\d{4}\b"

        # buscar fechas
        Fechas = re.findall(
            Patron,
            self.Texto
        )

        # eliminar repetidos
        return list(
            set(Fechas)
        )

# texto de ejemplo
Texto = """
El cumpleaños de Juan Pérez es el 12/03/1995.
La reunión con María González será el 15-04-2023.
José López no puede asistir el 12/03/2023.
"""

# crear instancia
Extraccion = Extraccion_informacion(
    Texto
)

# extraer nombres
Nombres_extraidos = Extraccion.Extraer_nombres()

# extraer fechas
Fechas_extraidas = Extraccion.Extraer_fechas()

# mostrar nombres
print(
    "Nombres extraidos:",
    Nombres_extraidos
)

# mostrar fechas
print(
    "Fechas extraidas:",
    Fechas_extraidas
)