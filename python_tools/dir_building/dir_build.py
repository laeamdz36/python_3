"""Modulo par ala creacion de estructuras de directorios personalizados"""

import os
import re
import datetime as dt
import json as js
import time as tm

# check if directory exist
current_dir = os.getcwd().split("\\")
current_dir = current_dir[-1]
print(current_dir)


def opselection(opSelected):

    if opSelected.lower() == "exit":
        state = 100
    elif opSelected.lower == "create":
        state = 10
    else:
        print("Ingrese una comando valido")
        return
    return state


fileOk = True
while fileOk:

    flag = opselection(input("->."))

    if flag == 10:
        main_name = input("Input the main folder name: ")
        tm.sleep(0.5)
        try:
            os.mkdir(main_name)
            print(f"'{main_name}' file created successfully!!")
            fileOk = False
            break
        except FileExistsError:
            print(f"'{main_name}' directory already exist, try another names...")
            continue
