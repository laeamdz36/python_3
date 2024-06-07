"""Funciones auxiliares de crew analyze"""


def paht_create():
    """Funcion para la aceptacion de la ruta del archivo"""
    while True:
        path_input = input("Ingrese la ruta del archivo -> ")
        print("Ingrese si/no")
        flag_ok = input(f"El registro ->'{path_input}'<- es correcto? ->")
        if flag_ok.lower() == "si":
            break
        else:
            print(f"Captura no valida -->'{flag_ok}',intente de nuevo")
            continue
    return path_input
