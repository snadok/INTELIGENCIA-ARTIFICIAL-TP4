import cv2
import numpy as np

# Cargar la imagen

ruta_imagen = "D:/Siglo21/5-1 Inteligencia Artificial/TP4/programa/imagen_recta.png"
imagen = cv2.imread(ruta_imagen)
# Convertir la imagen a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Aplicar detección de bordes utilizando el operador Canny
bordes = cv2.Canny(gris, 50, 150)

# Aplicar la transformada de Hough para detectar líneas rectas
lineas = cv2.HoughLinesP(bordes, 1, np.pi/180, threshold=100, minLineLength=100, maxLineGap=10)

# Obtener las dimensiones de la imagen
alto, ancho, _ = imagen.shape

# Dibujar las líneas detectadas sobre la imagen original
if lineas is not None:
    for linea in lineas:
        x1, y1, x2, y2 = linea[0]
        cv2.line(imagen, (x1, y1), (x2, y2), (0, 255, 0), 2)


# Dibujar las dos líneas verdes cruzadas en el centro de la imagen
cv2.line(imagen, (0, alto // 2), (ancho, alto // 2), (0, 255, 0), 2)
cv2.line(imagen, (ancho // 2, 0), (ancho // 2, alto), (0, 255, 0), 2)


# Mostrar la imagen resultante
cv2.imshow('Imagen con líneas y centro', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
