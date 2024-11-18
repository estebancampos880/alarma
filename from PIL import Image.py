from PIL import Image

ruta_imagen = "C:/Users/joser_6jgidsl/Desktop/alarma/imagen_alarma.png"

try:
    img = Image.open(ruta_imagen)
    img.show()  # Abre la imagen con el visor predeterminado
    print("Imagen cargada correctamente.")
except FileNotFoundError:
    print(f"Error: No se encuentra el archivo en {ruta_imagen}")
except Exception as e:
    print(f"Error al cargar la imagen: {e}")
