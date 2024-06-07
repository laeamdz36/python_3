""" Modulo para construccion de estructura de folders para guardar backups
    Estructura de anidacion de folders
    'Año: 2024'
        Linea: LN02
            Maquina: PG COSMA
                Mes: 01_Enero
                    Dia: 14_Ene_2024
                    Dia: 14_Ene_2024
                    Dia: 14_Ene_2024
                Mes: 02_Febrero
                    Dia: 14_Ene_2024
                    Dia: 15_Feb_2024
                    Dia: 16_Feb_2024
"""
from pathlib import Path
import os
import functools
import calendar
import pandas as pd


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
    """Dataframe building from db csv file"""

    df = pd.read_csv(file_path)
    return df


def get_unique_values(df: pd.DataFrame) -> dict:
    """Funcion para impresion de valores unicos de columnas"""

    col_linea = "Linea"
    col_equipo = "Panel"

    all_lines = [str(line) for line in df[col_linea].unique()]
    all_equipment = [str(equip) for equip in df[col_equipo].unique()]

    return {"lines": all_lines, "equips": all_equipment}


def notify_start_end(func):
    """Funcion decoradora para notificaion de inicio y fin de programa"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("INICIO DE PROGRAMA".center(100, "-"))
        ret_func = func(*args, **kwargs)
        print("FIN DE PROGRAMA".center(100, "-"))
        return ret_func
    return wrapper


def get_user_input(msg: str) -> int:
    """generic function to prompt to user input"""

    aux_text = " ->: "
    user_in = input(msg + aux_text)

    return int(user_in)


def folder_builder(date_dict: dict, df: pd.DataFrame) -> int:
    """Funcion para creacion de directorios para usos de backups basado en la especificaicon
        de año y nombres de carpetas hijas especificadas en el diccionario de control
        regresa un numero entero reportando la cantidad total de carpetas creadas.    
    """

    total_folders = 0
    parent_path = os.getcwd()
    parent_folder = str(date_dict.get("year"))
    parent_path = os.path.join(parent_path, parent_folder)

    # Creacion de carpeta parten, que es el numero del año
    os.makedirs(parent_folder, exist_ok=True)

    # Creacion de objeto calendario
    cal_aux = calendar.Calendar(firstweekday=0)
    for line in df["Linea"].unique():
        # Iteracion en rango de 1 a 12, que significa iteracion sobre meses del año
        line_folder = os.path.join(parent_path, str(line))
        os.makedirs(line_folder, exist_ok=True)

        for eq in df[df["Linea"] == line].loc[:, "Panel"]:
            equip_folder = os.path.join(line_folder, str(eq))
            os.makedirs(equip_folder, exist_ok=True)

            for month in range(1, 13):

                # Construccion de string para nombrar la carpeta del mes, formato 1.- Ene
                month_name = f"{month}.- {monthNames.get(month)}"
                month_folder = os.path.join(equip_folder, month_name)
                # Creacion del directorio del nombre del mes
                os.makedirs(month_folder, exist_ok=True)
                total_folders += 1

                # Iteracion sobre cada una de las fechas (2024-01-01), en el mes seleccionado, que viene del
                # ciclo for nivel arriba, en el rango 1 a 12
                for date in cal_aux.itermonthdates(2024, month):
                    if date.month == month:
                        date_folder = os.path.join(month_folder, str(date))
                        # Creacion de un folder para cada fecha, siempre y cuando el mes del calendario
                        # coincide bajo el mes dentro del rango del nivel superior del ciclo for,
                        # Esto debido a que el motodo iretmonthdates regresa las fechas abarnado semanas
                        # del siguiente mes, esto es puede contener dias del mes siguiente.
                        os.makedirs(date_folder, exist_ok=True)
                        total_folders += 1

                        # Iteracion sobre los elementos que seran carpetas hijas de cada folder fecha
                        # es controlado mediante el diccionario childsFolders
                        for key, value in childsFolders.items():
                            aux_path = f"{key}.- {value}"
                            child_folder = os.path.join(date_folder, aux_path)

                            os.makedirs(child_folder, exist_ok=True)

                            # variable locar que regresara el numero total de folders creados dentro
                            # del folder padres nombre del año.
                            total_folders += 1

    return total_folders


@notify_start_end
def run_program() -> None:
    """Ejecucion principal del programa"""

    work_date = {"year": 0, "month": 1}
    # seleccion del usuario
    work_date["year"] = get_user_input("Ingresar año")

    # construccion de dataframes
    file_path = build_path()
    df = build_dataframe(file_path)

    # construccion de fecha con año seleccionado
    result = folder_builder(work_date, df)
    print(f"Total folders creados -> {result}")


# Global variables
monthNames = {1: "Ene", 2: "Feb", 3: "Mar", 4: "Abr", 5: "May", 6: "Jun",
              7: "Jul", 8: "Ago", 9: "Sep", 10: "Oct", 11: "Nov", 12: "Dic"}
childsFolders = {1: "PLC", 2: "HMI",
                 3: "Scanner", 4: "Switch"}

if __name__ == "__main__":
    run_program()
