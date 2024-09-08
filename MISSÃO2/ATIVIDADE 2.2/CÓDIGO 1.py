import cv2
import numpy as np
 
img1 = cv2.imread(r'C:\Users\ketur\Downloads\ATIVIDADE 2.2\street-00.jpg')
img2 = cv2.imread(r'C:\Users\ketur\Downloads\ATIVIDADE 2.2\street-01.jpg')


img1_gray= cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

dif_abs = cv2.absdiff(img1_gray, img2_gray) 

ret, thresh = cv2.threshold(dif_abs, 30, 255, cv2.THRESH_BINARY)
 
contornos, ret = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

result = img2.copy()
for contorno in contornos:
    if cv2.contourArea(contorno) > 300: 
        x, y, w, h = cv2.boundingRect(contorno)
        cv2.rectangle(result, (x, y), (w+x, h+y), (0, 255, 0), 2)

cv2.imshow('Carros Detectados', result)
cv2.waitKey(0)
cv2.destroyAllWindows()