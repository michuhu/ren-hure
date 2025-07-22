import os
import shutil
from pathlib import Path

import pandas as pd
from pandas import DataFrame


def read_excel(filepath:str ) -> DataFrame:
    return pd.read_excel(filepath)

def read_csv(filepath: str)-> DataFrame:
    return pd.read_csv(filepath)

def view_parts(data: DataFrame):
    return data["Element"].unique()

def save_photos_from_csv(filepath: str):

    work_csv = pd.read_csv(filepath)

    filepaths = work_csv["ImagePath"]
    workdir = Path("work_dataset/photos")
    workdir.mkdir(parents=True, exist_ok=True)

    for f in filepaths.values:
        src = Path(f)

        src_fldr = src.parts[-2]
        dest = workdir.joinpath(f"{src_fldr}_{src.name}")

        try: 
            shutil.copy(src, dest)
        except Exception as e:
            print(e)
            continue

if __name__ == "__main__":
    # data = read_excel("Dataset/work.xlsx")
    # parts = view_parts(data)
    # print(parts)
    save_photos_from_csv("work_dataset/one_class.csv")

