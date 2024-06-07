"""Pracrica de funciones lambdas"""
import random as rd


health = 100
xp = 0

# funcion para rodar dado


def rollDice():

    diceFaces = 6
    diceminimum = 1
    diceResult = rd.randint(diceminimum, diceFaces)

    print(f"Dado obtenido -> {diceResult}")
    return diceResult


def rollGame():

    userGuess = str(input("Ingrese su numero -> "))
    currentNum = rollDice()
    if userGuess == currentNum:
        print("Acertaste el numero")
    else:
        print("Seleccion equivocada")


def outCome(dice):

    if dice >= 4:
        return (10, 20)
    return (5, 10)


def attempt(action, min_roll, outcome):

    global health, xp

    roll = rd.randint(1, 20)
    if roll >= min_roll:
        print(f"{action} Succeeded")
        result = True
    else:
        print(f"{action} Failde!!")
        result = False

    scores = outcome(result)
    health = health + scores[0]

    print(f"Health is now {health}")
    print(f"Experience is now {xp}")


attempt("Primera accion", 10, lambda success: (
    10, 20) if success else (-10, -20))
attempt("Segunda accion", 5, outCome)
attempt("tercera accion", 5, outCome)
