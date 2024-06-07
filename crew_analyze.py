"""Modulo para lectura y procesamiento de informacion de electronicos"""

import json

from pathlib import Path
import crew_module as cm


# 1. Creacion del path para abrir el archivo
# 2. read file and print
# 3. Crear directorio de usuarios
#   Name:, PLC, Troubleshooting, Leadership, Acomplishment, Maint Skill
# direcotry_master = {name:{PLC:value,Troubleshooting:value,Leadership:value,Acomplishment:value}}

file_test = Path("text_files/crew_electronic.txt")
# path_file = Path(cm.paht_create())

row_1st_order = []
directory_master = {}
names = []
dir_test = {}

# try:
#    read_txt = path_file.read_text(encoding="utf-8")
# except FileNotFoundError:
#    print(f"File not found -> {path_file}")


def create_dir(list_items, headers_aux):
    """Funcion para la creacion del master directory"""
    # Creacion de direcotry user data
    dir_aux = {}
    dir_aux["first_name"] = list_items[0]
    dir_aux["last_name"] = list_items[1]
    # Key PLC
    dir_aux[headers_aux[1]] = list_items[2]
    # Key troubleshooting
    dir_aux[headers_aux[2]] = list_items[3]
    # Key leadership
    dir_aux[headers_aux[3]] = list_items[4]
    # key acomplishment
    dir_aux[headers_aux[4]] = list_items[5]
    # Key Maint Skill
    dir_aux[f"{headers_aux[5]} {headers_aux[6]}"] = list_items[6]
    directory_master[f"{list_items[0]} {list_items[1]}"] = dir_aux
    # dir_aux.clear()


# Leer contenido y almacenarlo en memoria
content_test = file_test.read_text()
# Dividir las lineas de texto del archivo
text_split_test = content_test.splitlines()
# print(f"{text_split_test}")
for row in text_split_test:
    row_1st_order.append(row.split())
headers = row_1st_order[0]
del row_1st_order[0]
# print(headers)
# print(row_1st_order)
for item in row_1st_order:
    create_dir(item, headers)

print(directory_master)
# print(row_1st_order)
