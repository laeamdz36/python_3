"""Modulo para empaquetamiento de folders de backup"""

import shutil
import os
import datetime as dt


def custom_date_string() -> str:
    """Custom date string for archiving name files"""

    # Custom format 20240101_012435.zip
    actual = dt.datetime.today()
    date = f"{actual.year}{actual.month:02d}{actual.day:02d}"
    time = f"{actual.hour:02d}{actual.minute:02d}{actual.second:02d}"
    print(date+"_"+time)
    return date+"_"+time


def archive_file(file_name, file_path):
    """Function to archive file"""

    shutil.make_archive(file_name, "zip", "./2024")


def run_program() -> None:
    """Main link run program"""
    out_file_name = custom_date_string()
    archive_file(out_file_name, target_file)

    return


current_path = os.getcwd()
dir_lis = os.listdir()

target_file = "2024"
out_file_name = ""

if __name__ == "__main__":

    run_program()
