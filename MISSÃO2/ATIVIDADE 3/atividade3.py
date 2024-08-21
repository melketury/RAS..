import cv2

caminho_imagem = 'C:/Users/ketur/OneDrive/Documentos/ATIVIDADE 3/jordan.jpeg'  
imagem = cv2.imread(caminho_imagem)
cv2.imshow('Imagem Original', imagem)

altura = 900
largura = 1600

tamanho_maior = (int(largura * 1.5), int(altura * 1.5))
ampliada = cv2.resize(imagem, tamanho_maior, interpolation=cv2.INTER_LINEAR)
cv2.imshow('Imagem Ampliada', ampliada)

tamanho_menor = (int(largura * 0.5), int(altura * 0.5))
reduzida = cv2.resize(imagem, tamanho_menor, interpolation=cv2.INTER_LINEAR)
cv2.imshow('Imagem Reduzida', reduzida)

# b. Ajuste de brilho usando HSUV
imagem_hsuv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(imagem_hsuv)

# Aumentar o brilho
claro = cv2.add(v, 50)  # Adiciona 50 ao canal V, aumentando o brilho
cv2.imshow('Imagem Mais Clara (HSUV)',claro)

# Diminuir o brilho
escuro = cv2.subtract(v, 50)  # Subtrai 50 do canal V, diminuindo o brilho
cv2.imshow('Imagem Mais Escura (HSUV)', escuro)

# Limitar os valores entre 0 e 255
claro = cv2.min(claro, 255)
escuro = cv2.max(escuro, 0)

# Recompor a imagem com os novos valores de V
imagem_clara_hsuv = cv2.merge([h, s, claro])
imagem_escura_hsuv = cv2.merge([h, s, escuro])

# Converter de volta para BGR
imagem_mais_clara = cv2.cvtColor(imagem_clara_hsuv, cv2.COLOR_HSV2BGR)
imagem_mais_escura = cv2.cvtColor(imagem_escura_hsuv, cv2.COLOR_HSV2BGR)

# c. Desfoque (Blurring)
tamanho_kernel = 9

# i. Convolução
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (tamanho_kernel, tamanho_kernel))
convolução = cv2.filter2D(imagem, -1, kernel)
cv2.imshow('Desfoque por Convolução', convolução)

# ii. Desfoque Regular (Média)
regular = cv2.blur(imagem, (tamanho_kernel, tamanho_kernel))
cv2.imshow('Desfoque Regular', regular)

# iii. Desfoque Gaussiano
gaussiano = cv2.GaussianBlur(imagem, (tamanho_kernel, tamanho_kernel), 0)
cv2.imshow('Desfoque Gaussiano', gaussiano)

# d. Binarização (Thresholding)
cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
cv2.imshow('Thresholding Regular', cinza)

# Thresholding Regular
_, imagem_binaria_regular = cv2.threshold(cinza, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('Thresholding Regular', imagem_binaria_regular)

# Thresholding Adaptativo
imagem_binaria_adaptativa = cv2.adaptiveThreshold(cinza, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
cv2.imshow('Thresholding Adaptativo', imagem_binaria_adaptativa)



cv2.waitKey(0)
cv2.destroyAllWindows()