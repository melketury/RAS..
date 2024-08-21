import cv2
import os

webcam = cv2.VideoCapture(0)  

if webcam.isOpened():  
    validacao, frame = webcam.read()  

    while validacao:
        validacao, frame = webcam.read()  
        cv2.imshow("Vídeo", frame)  
        key = cv2.waitKey(5) 
        if key == 27:
            break

    # Salvar a imagem capturada
    cv2.imshow("Imagem Capturada", frame) 
    cv2.waitKey(0) 
    cv2.destroyWindow("Imagem Capturada")  

    # Usar um nome de arquivo padrão
    filename = "imagem.png"
    save_dir = "C:\\Users\\ketur\\OneDrive\\Documentos\\ATIVIDADE 1"  # Caminho absoluto
    print(f"Caminho de salvamento: {save_dir}")  # Imprimir o caminho de salvamento

    # Criar o caminho completo para o arquivo
    filepath = os.path.join(save_dir, filename)
    cv2.imwrite(filepath, frame)  # Salvar a imagem no caminho especificado
    print(f"Imagem salva em: {filepath}")  # Confirmação de salvamento

# Liberar a webcam e fechar todas as janelas
webcam.release()
cv2.destroyAllWindows()