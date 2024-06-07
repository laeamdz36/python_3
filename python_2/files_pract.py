"""Practica de modulo de os"""
import os
import tempfile
import pathlib as pl
import datetime as dt


def pc_dir(dir_list):
    """List all current directory
        dir_list -> LIST of directory
    """
    for i, directory in enumerate(dir_list):
        print(f"{i} -> {directory}")
    print("\nFinished dir list___\n")


def pr_file_name():
    """Print file name"""
    print(__file__)
    print(type(__file__))
    print(os.path.dirname(os.path.realpath(__file__)))

# Tenmprorary files


def prac_temp_files():
    """Practica de archivos temporales"""
    return


def cr_file_data():
    """
        Practica de creacion de archivo con nombre de asignado por usuario
        Dentro escribir hora, nombre, fecha de nacimiento, calcular edad
    """

    # Mensaje de bienvenida al sistema
    welcome = "\nBienvenido al sistema\n"
    print(welcome.center(len(welcome) + 50, "*"))

    name = input("Ingrese su Nombre -> ").capitalize()
    conf_name = "\nNombre ingresado -> " + name + "\n"
    print(conf_name.center(len(conf_name) + 50, "-"))

    in_file_msg = "Ingrese nombre de archivo: "
    date_aux = dt.datetime.today().strftime("%Y%m%d__%H%M%S%f")[:-3]
    file_name = input(in_file_msg) + date_aux + ".txt"

    with open(file_name, "w", encoding="UTF-8") as f:
        try:
            f.write(f"{name} - {date_aux}\n")
            d_w = str(dt.datetime.today())
            f.write(f"Hola Mundo {d_w}\n")
            f.write(__file__)

            for i, directory in enumerate(os.listdir()):
                f.write(f"{i} -> {directory}\n")

        except Exception as err:
            print(f"Unspected {err=}, {type(err)=}")


if __name__ == "__main__":
    dir_list_aux = os.listdir()
    # pc_dir(dir_list_aux)
    cr_file_data()
