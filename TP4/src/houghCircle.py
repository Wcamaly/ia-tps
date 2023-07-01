import cv2
import numpy as np

# Cargar imagen
img = cv2.imread('./assets/circle.png',0)

# Suavizar la imagen con un filtro gaussiano
img = cv2.medianBlur(img,5)

# Aplicar la transformada de Hough para círculos
circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)

circles = np.uint16(np.around(circles))

# Convertir la imagen a color
cimg = cv2.cvtColor(img,cv2.BORDER_CONSTANT)

for i in circles[0,:]:
    # dibujar el círculo exterior en rojo
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,0,255),2)
    # dibujar el centro del círculo en rojo
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow('circles detected', cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
