"""Modulo para lectura de base de datos"""
import pandas as pd
from pathlib import Path
import os


def build_path() -> Path:
    """Build path from static variables"""

    # Static Variables
    DB_FOLDER = "./data/"
    FILE_NAME = "eq_data.csv"

    file_path = Path(DB_FOLDER + FILE_NAME)

    if file_path.is_file():
        return file_path
    else:
        print("Folder o nombre de arhivo invalido")
    return None


def build_dataframe(file_path: Path) -> pd.DataFrame:
    """Function para contrsuccion de dataframe"""

    df = pd.read_csv(file_path)
    print(df.head())
    return df


def get_unique_values(df: pd.DataFrame) -> None:
    """Funcion para impresion de valores unicos de columnas"""

    col_linea = "Linea"
    col_equipo = "Panel"

    all_lines = [str(line) for line in df[col_linea].unique()]
    all_equipment = [str(equip) for equip in df[col_equipo].unique()]

    return


if __name__ == "__main__":

    data_frame = build_path()
    df_data = build_dataframe(data_frame)
