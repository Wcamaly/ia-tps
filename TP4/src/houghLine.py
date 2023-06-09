import cv2
import numpy as np

# Leer la imagen
img = cv2.imread('./assets/lineas.jpg')

# Convertir la imagen a escala de grises
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Aplicar detección de bordes con Canny
edges = cv2.Canny(gray, 50, 150, apertureSize = 3)

# Aplicar la Transformada de Hough
lines = cv2.HoughLines(edges, 1, np.pi/180, 200)

# Dibujar las líneas
for rho,theta in lines[0]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))

    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
