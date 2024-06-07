"""Preactica de recursividad
    Definir cantidad total de numeros aleatorios en la lista
    
"""

import random


def get_new_random() -> None:
    """Funcion para obtener nuevo numero random si 
        y agregar si no esta en la lista
    """

    new_random = random.randint(1, 10)
    if new_random in listNumbers:
        print(f"{new_random} - ya en la lista, se volvera a seleccionar nuevo numero")
        get_new_random()
    else:
        listNumbers.append(new_random)

    return


def define_max_length() -> int:
    """Funcion para definir longitud maxima de la lista"""

    max_len = input("Ingresa longitud maxima de la lista: ")
    return int(max_len)


listNumbers = []
flag = True
max_length = 0
while flag:

    if max_length == 0:
        max_length = define_max_length()

    if len(listNumbers) >= max_length:
        flag = False
        print(listNumbers)
        break
    get_new_random()
