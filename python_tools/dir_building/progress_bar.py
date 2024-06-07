import time as tm
import datetime as dt


print("Downloading")

for n in range(20):
    print("-", end="", flush=True)
    tm.sleep(0.1)
print("\nDownload complete")


def printName(name):
    """Impresion de string creativa utilizando flush"""

    for letter in name:
        print(letter, end="", flush=True)
        tm.sleep(0.1)
    print("")


def printtable(dictData):
    """Fincion para impresion en formato tabla"""

    for key, value in dictData.items():
        for apellido, color in value.items():
            print(key, apellido, color, sep="\t|\t|\t")


name = "Bienvenido Jose Luis Peña"
# printName(name)
# printName("Digite el siguiente comando pofavor!!!!!!")

dictAuxiliar = {"Luis": {"Apellido": "Peña,", "Color": "Verde"},
                "Lorena": {"Apellido": "Alanis", "Color": "Blanco"}}
printtable(dictAuxiliar)

for n in range(100):
    date = str(dt.datetime.today())
    print(date, end="\r", flush=True)
    tm.sleep(0.1)
