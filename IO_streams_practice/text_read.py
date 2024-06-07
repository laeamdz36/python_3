import datetime as dt
from pathlib import Path


def buildNameFile():
    """Create file name based to time stamp"""
    ext = ".txt"
    date = str(dt.date.today())
    timeStamp = str(dt.datetime.timestamp(
        dt.datetime.today()))[:10] + ext
    return date + timeStamp + ext


def writeFile(file):

    root = Path("./" + file)
    with open(root, mode="+w") as fileWork:
        fileWork.write("Hola_mundo")


fileName = buildNameFile()
writeFile(fileName)
