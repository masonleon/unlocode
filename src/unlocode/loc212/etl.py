import pandas as pd
import numpy as np
import glob
import re

from .constants import DELIMITER, ENCODING

def load_codelist(dir_path):
    all_files = glob.glob(dir_path + "/*UNLOCODE CodeListPart*.csv")

    li = []

    header_col_names=[
        'Change',
        'Country',
        'Location',
        'Name',
        'NameWoDiacritics',
        'Subdivision',
        'Function',
        'Status',
        'Date',
        'IATA',
        'Coordinates',
        'Remarks'
    ]

    for filename in all_files:
        df = pd.read_csv(
            filename,
            header=None,
            encoding=ENCODING,
            names=header_col_names,
            # dtype=object,
            dtype=str,
            keep_default_na=False,
            # need to modify na values to prevent converting NAMBIA Country code (NA) to NaN
            na_values=[
                '-1.#IND', 
                '1.#QNAN', 
                '1.#IND', 
                '-1.#QNAN', 
                '#N/A N/A', 
                '#N/A', 
                'N/A', 
                'n/a', 
                # 'NA', 
                '<NA>', 
                '#NA', 
                'NULL', 
                'null', 
                'NaN', 
                '-NaN', 
                'nan', 
                '-nan', 
                ''
            ]
            # converters={ "file name": str, "company name": str})
        )
        li.append(df)

    frame = pd.concat(li, axis=0, ignore_index=True)

    return frame
