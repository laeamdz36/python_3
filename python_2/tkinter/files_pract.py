import datetime as dt
import time as tm
import pathlib as pl
import re


file_path_str = "./"

print("Start execution")
today = dt.datetime.today()
date_str = str(today)
tm.sleep(1)
print(date_str)
date_object = dt.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")
print(f"{date_object.date()}")
print(f"{date_object.time()}")
print(f"Iso Week{date_object.isocalendar().week}")

tm.sleep(1)
hola = r"/bin/sh$"
print(type(hola))
