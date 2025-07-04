# Primero, asegúrate de tener instaladas las librerías necesarias.
# Puedes instalarlas usando pip. Abre tu terminal y ejecuta:
# pip install qrcode[pil] pillow
import qrcode
from PIL import Image

def generate_ascii_qr(link):
    # Generar el código QR
    qr = qrcode.QRCode(version=1, box_size=2, border=1)  # Tamaño reducido
    qr.add_data(link)
    qr.make(fit=True)
    
    # Crear la imagen del QR
    img = qr.make_image(fill='black', back_color='white')
    
    # Convertir la imagen a escala de grises
    img = img.convert('L')
    
    # Definir los caracteres ASCII que se usarán
    ascii_chars = [' ', '█']  # Usar solo dos caracteres para simplificar
    
    # Obtener los píxeles de la imagen
    pixels = img.getdata()
    width, height = img.size
    
    # Crear una lista para almacenar las líneas de arte ASCII
    ascii_art = []
    
    # Ajustar la altura para que se vea más cuadrado
    aspect_ratio_adjusted_height = int(width * (height / width) * 0.5)  # Ajustar la altura

    # Convertir cada píxel a un carácter ASCII
    for y in range(aspect_ratio_adjusted_height):
        line = ''.join(ascii_chars[1 if pixels[x + (y * (height // aspect_ratio_adjusted_height)) * width] < 128 else 0] for x in range(width))
        ascii_art.append(line)
    
    # Imprimir el arte ASCII
    for line in ascii_art:
        print(line)

# Ejemplo de uso
link = "http://192.168.1.29:8080/"
generate_ascii_qr(link)
