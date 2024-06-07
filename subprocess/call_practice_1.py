"""Call to file print name"""
from subprocess import call
import os

def call_printName():
    """Call print name function"""

    call(["python","print_name.py"])

    return

call_printName()
os.environ["Hola_mundo"] = "Luis"