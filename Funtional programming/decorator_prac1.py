"""Practica de decoradores"""
import functools
import typing

# declaracion de variables globales
message_1 = "Hola, primer mensaje"
message_2 = "Hola ultimo mensaje"


def decorator_1(func):
    """Fisrt decorator"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(message_1)
        result = func()
        print(message_2)
        return result
    return wrapper


def auxMessages(func):
    """Mensaje auxiliares para funcion"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("\nSe comenzara con la recoleccion de los numeros\n")
        result = func(*args, **kwargs)
        print(f"\n{args[0]}")
        return result

    return wrapper


@decorator_1
def printHolaMundo():
    """Funcion para imprimir hola mundo"""
    # variable annotation

    print("Hola mundo")


@auxMessages
def printSum(action: str) -> str:
    """Funcion que solicita dos numeros y devulve la sumatoria"""
    action: str = "Sumar,Restar"
    num1 = input("Ingrese numero 1: ")
    num2 = input("Ingrese numero 2: ")

    print(f"\nResultado -> {num1 + num2}")

# for type hinting


def func_with_optionals(var2: typing.Optional[int] = None, var1: int = 0):
    print(f"funcion_opcionales {var2}, {var1}")


string_function = printSum("Sumar los numeros arre!!!").__doc__
doc_holamundo = printHolaMundo.__doc__
print(doc_holamundo)
func_with_optionals()
