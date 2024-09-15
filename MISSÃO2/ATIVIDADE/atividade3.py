import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

image_folder_path = 'C:/Users/ketur/OneDrive/Documentos/ATIVIDADE'

image_files = [f for f in os.listdir(image_folder_path) if f.lower().endswith('.jpg')]
image_files.sort() 

current_index = 0


def show_image(index):
    image_path = os.path.join(image_folder_path, image_files[index])
    image = cv2.imread(image_path)
    
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
    edges = cv2.Canny(blurred_image, 50, 150)
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    output_image = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR)
    cv2.drawContours(output_image, contours, -1, (0, 255, 0), 1)

    plt.subplot(1, 2, 1)
    plt.title('Original')
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.title('Detectadas')
    plt.imshow(cv2.cvtColor(output_image, cv2.COLOR_BGR2RGB))
    plt.axis('off')

    plt.suptitle(f'Imagem {index + 1} de {len(image_files)}')
    plt.draw()

def on_key(event):
    global current_index
    if event.key == 'm':
        current_index = (current_index + 1) % len(image_files)
        plt.clf()
        show_image(current_index)

plt.figure(figsize=(8, 4))  
show_image(current_index)

plt.gcf().canvas.mpl_connect('key_press_event', on_key)

plt.show()
