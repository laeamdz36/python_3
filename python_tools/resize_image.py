"""Pequeño programa para convertir imagenes mas peuqeño tamaño"""

from pathlib import Path
from PIL import Image

filePath = Path("./imagen.jpg")

imagen = Image.open("imagen.jpg")

imagen.thumbnail((1200, 600))
imagen.save("new_image.jpg")
