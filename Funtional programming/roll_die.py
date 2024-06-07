"""A simple function to roll a die
    para exceder el limite de recursion 
    import sys
    sys.setrecursionlimit(2000)
"""

import random as rd


def roll_die():
    """Rando return of integer number"""
    randomNumber = rd.randint(1, 10)
    return randomNumber


def comp_rollDice(sides, dice):
    return tuple(rd.randint(1, sides) for n in range(dice))


def playrollDice():

    player1, player2 = rollDiceRecursive(6, 2)

    if player1 > player2:
        print(f"Player 1 goes first (rolled {player1} and player 2 {player2})")
    elif player1 < player2:
        print(f"Player 2 goes first (rolled {player2} and player 1 {player1})")
    else:
        print("Lets roll again, players match")
        playrollDice()

# recursion


def rollDiceRecursive(sides, dice):
    """Funcion recursiva para generar tupla de vaores aleatorios"""
    if dice < 1:
        return ()
    roll = rd.randint(1, sides)
    return (roll,) + rollDiceRecursive(sides, dice-1)

# variadic parameter with recursion


def buildRandomList(*pars):

    if pars:
        num = rd.randint(1, pars[0])
        return


def onlyKeyArgs(*, name="NoName", age="NoAge"):
    """Colocando el * restringe la funcion a que el caller
        solo contenga keyword arguments"""

    print(f"Your {name} and your {age}")


print(roll_die())
playrollDice()
rollDiceRecursive(10, 10)

# Caller, con argunemtos posicionales surge TypeError exception
# onlyKeyArgs("Luis")
