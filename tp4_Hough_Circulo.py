import cv2
import numpy as np

# Cargar la imagen
image = cv2.imread('imagen_hough.png')

# Convertir la imagen a escala de grises
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplicar umbralización para resaltar el color gris
_, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

# Aplicar desenfoque para reducir el ruido
blurred = cv2.GaussianBlur(thresh, (5, 5), 0)

# Detectar círculos utilizando la transformada de Hough
circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=10, maxRadius=50)

# Verificar si se detectaron círculos
if circles is not None:
    # Redondear los parámetros y convertirlos a enteros
    circles = np.round(circles[0, :]).astype(int)

    # Dibujar los círculos detectados
    for (x, y, r) in circles:
        cv2.circle(image, (x, y), r, (0, 255, 0), 2)
        cv2.circle(image, (x, y), 2, (0, 0, 255), 3)

# Mostrar la imagen original y la imagen con los círculos
cv2.imshow('Original', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
