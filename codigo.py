import cv2
import numpy as np

import time


# Función para detectar frutas no maduras
def detect_unripe_fruit(frame):
    # Convertir la imagen a espacio de color HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Definir los rangos de color para detectar frutas no maduras
    lower_green = np.array([25, 50, 50])
    upper_green = np.array([75, 255, 255])
    
    # Crear una máscara para detectar los píxeles verdes
    mask = cv2.inRange(hsv, lower_green, upper_green)
    
    # Encontrar los contornos de la fruta no madura
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # Si se encuentra al menos una fruta no madura, preder el led
    if len(contours) > 0:
        
        
        print("deteccion")
        
    return mask

# Capturar video de la cámara
cap = cv2.VideoCapture(0)

while True:
    # Leer un fotograma del video
    ret, frame = cap.read()
    
    # Detectar frutas no maduras y mover el brazo robótico
    mask = detect_unripe_fruit(frame)
    
    # Mostrar la imagen original y la máscara
    cv2.imshow('Original', frame)
    cv2.imshow('Mask', mask)
    
    # Salir del bucle al presionar 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Limpiar y cerrar
cap.release()
cv2.destroyAllWindows()
