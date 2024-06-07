"""Practica de streams y lectura de archivos"""

# Lectura de archivos
from pathlib import Path
import os
import time
import functools


def menu_msg(func):
    """Añadir header y footer a menu de aplicacions"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        header = "---Menu---".center(100, "*")
        footer = "---files_reading.py---".center(100, "*")
        print(header)
        result = func()
        print(footer)
        return result
    return wrapper


def flush_example():
    """Ejemplo de uso de parametro flush dentro de funcion print"""
    print("Downloading", end="")
    for n in range(20):
        print(".", end="", flush=True)
        time.sleep(0.4)
    print("\nDownload Complete")


def select_function(user_input):
    """Seleccion de funcion"""

    if user_input == 4:
        flag_aux = False
        out_msg = "Saliendo de programa".center(100, "-")
        print(out_msg)
    else:
        flag_aux = True
    return flag_aux


def run_main():
    """Funcion principal"""
    user_req = int(input("Ingrese Numero de funcion de funcion: "))
    flag_final = select_function(user_req)
    return flag_final


@menu_msg
def print_menu():
    """Funcion para imprimir menu de opciones"""
    name = "functions_menu.txt"
    path = "./data_files/"
    file_path = Path(path + name)

    with open(file_path) as menu_file:
        menu_list = menu_file.read().splitlines()
        for i, line in enumerate(menu_list):
            print(f"{i+1} -> {line}")
    return None


if __name__ == "__main__":
    run_flag = True
    while run_flag:
        print_menu()
        run_flag = run_main()
