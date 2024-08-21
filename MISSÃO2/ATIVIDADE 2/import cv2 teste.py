import cv2
import numpy as np

webcam = cv2.VideoCapture(0)

while True:
    ret, frame = webcam.read()
    

    # Realiza o recorte da imagem
    frame = frame[0:350, 15:540]
    gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

    # Mostra o frame na janela
    cv2.imshow("frame", frame)
    cv2.imshow("gray", gray)
    cv2.imshow ("threshold", threshold)
    # Captura a tecla pressionada
    key = cv2.waitKey(1)
    if key == 27:  # ESC key
        break

webcam.release()
cv2.destroyAllWindows()
