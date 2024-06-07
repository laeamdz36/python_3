"""Modulo para creacion de calses"""
import datetime as dt
from .comm import comm_load

def load_module():
    """Message when module is loaded"""

    print(__name__,"loaded")

    return None

class Person(object):
    """Clase para creacion de objetos persona"""

    specie = "Homo Sapiens"

    def __init__(self,name):

        self.name = name

    def __str__(self):
        """Return the string name of the class"""
        return self.name
    
    def rename(self,renamed):
        """Class fuinction to rename name class"""

        self.name = renamed
        print(f"Now my name is{self.name}")

def importage():
    """Message for loading module"""
    date = str(dt.datetime.today())
    date = date.center(100,"-")
    print(f"{date[:-6]}")

def get_comm():
    """Execution function from comm package"""

    comm_load.print_loading()
