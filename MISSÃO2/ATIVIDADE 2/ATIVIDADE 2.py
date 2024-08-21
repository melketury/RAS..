import cv2
import os


caminho_base = os.path.expanduser("~/OneDrive/Documentos/ATIVIDADE 2")

nome_arquivo = input(" o nome do arquivo da imagem, 'imagem.jpg'): ")

caminho_imagem = os.path.join(caminho_base, nome_arquivo)
image = cv2.imread(caminho_imagem)

image = cv2.resize(image, (900, 1600))
print(f"Dimensões da imagem redimensionada: {image.shape}")


cv2.imshow("Imagem Redimensionada", image)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print(f"Dimensões da imagem em escala de cinza: {gray_image.shape}")


cv2.imshow("Imagem em Escala de Cinza", gray_image)

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

cv2.imshow("Imagem HSV", hsv_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
