"""Practica con queues
    Proyecto inconcluso, todo por segir el tema de binary and serialization"""

import queue
import functools
import os
# Desplegar Menu , Agregar dato a la cola
# Obtener dato de la cola
# Numero de elementos en la cola
# Finalizar programa


# lista de menus
cmd_list = ["Opcion 1", "Opcion 2", "Mostrar menu", "Exit"]
cmd_dict = {(i+1): menu for i, menu in enumerate(cmd_list)}
cmd_control = {"menu": 1, "exit": 36,
               "Opcion Incorrecta": 99, "cls": 2, "help": 3}
ctl_flow = {"status": 0}


def finalizerAux(func):
    functools.wraps(func)

    def wrapper(*args, **kwargs):

        out_func = func(*args, **kwargs)
        kwargs["end"] = 0
        return out_func
    return wrapper


@finalizerAux
def finalizer(end: int = 0) -> int:
    """Funcion finalizadora"""

    return end


def application(option: str) -> int:
    """Programa para asignacion de proceso on status word"""

    return cmd_control.get(option.lower(), 99)

# decorador para menu


def disp_menu(func):
    """Funcion decoradora para impresion de menu"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        print("MENU PRINCIPAL".center(100, "-"))
        out_func = func(*args, **kwargs)
        print("".center(100, "-"))
        return out_func
    return wrapper


@disp_menu
def show_menu() -> None:
    """Funcion para impresion de menu"""
    for op, menu in cmd_dict.items():
        print(f"{op} - {menu}")
    return


def incorrectWarning():

    print("Opcion Incorrecta".center(100, "*"))
    print("".center(100, "-"))


def printHelper():

    print("No hay ayuda disponible!!")


def control_program(ctl_word: dict) -> int:
    """Programa de control de sesion, input """
    return_start = 0
    if ctl_word["status"] == cmd_control["exit"]:
        print("\nExit program successfully :V")
        return finalizer(36)
    if ctl_word["status"] == cmd_control["menu"]:
        show_menu()
        return finalizer(0)
    if ctl_word["status"] == cmd_control["Opcion Incorrecta"]:
        incorrectWarning()
        return finalizer(0)
    if ctl_word["status"] == cmd_control["cls"]:
        os.system("cls")
        return finalizer(0)
    if ctl_word["status"] == cmd_control["help"]:
        printHelper()
        return finalizer(0)


q1 = queue.Queue()
flag = True
start = True

# Main loop
while flag:

    # fisrt start
    if start:
        show_menu()
        start = False

    # select option
    op = input("-> ")

    ctl_flow["status"] = application(op)

    ctl_flow["status"] = control_program(ctl_flow)

    if ctl_flow["status"] == cmd_control["exit"]:
        flag = False
