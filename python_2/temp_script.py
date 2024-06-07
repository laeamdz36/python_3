"""Modulo impresion de temperatura"""

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

file_route = "csv_files_2/data/temp_data.csv"
file_path = Path(file_route)

df_temperature = pd.read_csv(file_path)
df_temp = df_temperature[" Temperatura_Celsius"]
df_temp.plot(title="Temperature", grid=1)
plt.show()
