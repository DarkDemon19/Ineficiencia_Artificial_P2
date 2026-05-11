# Detecta bordes en una imagen en escala de grises
# usando el metodo Canny

# Para procesar imagenes
import cv2
from matplotlib import pyplot as plt

# cargar imagen en escala de grises
Imagen = cv2.imread(
    "Soldaditos.JPG",
    cv2.IMREAD_GRAYSCALE
)

# validar carga
if Imagen is None:

    print(
        "No se pudo cargar la imagen. Verifica la ruta."
    )

else:
    # aplicar detector Canny
    Bordes = cv2.Canny(
        Imagen,
        100,
        200
    )

    # crear figura
    plt.figure(
        figsize=(10, 5)
    )

    # mostrar imagen original
    plt.subplot(
        1,
        2,
        1
    )

    plt.imshow(
        Imagen,
        cmap="gray"
    )

    plt.title(
        "Imagen Original"
    )

    plt.axis("off")

    # mostrar bordes detectados
    plt.subplot(
        1,
        2,
        2
    )

    plt.imshow(
        Bordes,
        cmap="gray"
    )

    plt.title(
        "Deteccion de Bordes"
    )

    plt.axis("off")

    # mostrar resultado final
    plt.show()