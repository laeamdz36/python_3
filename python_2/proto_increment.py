"""Prototipo de funcion para incremento en realtime de contadores de unidades producidas"""

import time as tm
import datetime as dt


def main_p1(condition, main_condition):
    """Main funcion for looping"""
    print("Executing main loop")
    while condition < main_condition:
        tm.sleep(0.2)
        print(f"Watchdog active -> {condition}")
        condition += 1
        if condition >= main_condition:
            print(f"Exit music value -> {condition}")


condition = 0
main_condition = 100

if __name__ == "__main__":

    main_p1(condition, main_condition)
