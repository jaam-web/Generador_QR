# Primero, asegúrate de tener instaladas las librerías necesarias.
# Puedes instalarlas usando pip. Abre tu terminal y ejecuta:
# pip install qrcode[pil] pillow

import qrcode  # Importar la librería para generar códigos QR
from PIL import Image  # Importar la librería para manipular imágenes

def generar_qr_ascii(enlace):
    # Generar el código QR
    qr = qrcode.QRCode(version=1, box_size=2, border=1)  # Tamaño reducido
    qr.add_data(enlace)  # Agregar los datos al QR
    qr.make(fit=True)  # Ajustar el tamaño del QR

    # Crear la imagen del QR
    img = qr.make_image(fill='black', back_color='white')

    # Convertir la imagen a escala de grises
    img = img.convert('L')

    # Definir los caracteres ASCII que se usarán
    caracteres_ascii = [' ', '█']  # Usar espacio en blanco y un bloque

    # Obtener los píxeles de la imagen
    pixeles = img.getdata()
    ancho, alto = img.size

    # Crear una lista para almacenar las líneas de arte ASCII
    arte_ascii = []

    # Convertir cada píxel a un carácter ASCII
    for y in range(alto):
        linea = ''.join(caracteres_ascii[1 if pixeles[x + y * ancho] < 128 else 0] for x in range(ancho))
        arte_ascii.append(linea)

    # Imprimir el arte ASCII
    for linea in arte_ascii:
        print(linea)

# Ejemplo de uso
enlace = "http://192.168.1.29:8080/"  # Cambia este enlace por el que desees
generar_qr_ascii(enlace)
