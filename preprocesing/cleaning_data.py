
import numpy as np
import pandas as pd


def preprocess(json_data):

    df = pd.DataFrame(json_data, index=[0])

    df['zip_code'] = df['zip_code'].astype(str).str[:-2].astype(np.int64)
    mapping = {73: 1, 64: 2, 60: 3, 76: 4, 71: 5, 56: 6, 79: 7, 55: 8, 41: 9, 61: 10, 44: 11, 62: 12, 70: 13, 65: 14, 48: 15, 40: 16, 45: 17, 68: 18, 77: 19, 43: 20, 50: 21, 95: 22,
               75: 23, 66: 24, 69: 25, 53: 26, 42: 27, 46: 28, 89: 29, 88: 30, 78: 31, 21: 32, 49: 33, 84: 34, 51: 35, 38: 36, 34: 37, 37: 38, 96: 39, 93: 40, 36: 41, 91: 42, 67: 43,
               97: 44, 86: 45, 92: 46, 99: 47, 87: 48, 94: 49, 33: 50, 85: 51, 39: 52, 24: 53, 28: 54, 22: 55, 23: 56, 26: 57, 47: 58, 32: 59, 80: 60, 35: 61, 15: 62, 98: 63, 25: 64,
               17: 65, 14: 66, 82: 67, 10: 68, 18: 69, 90: 70, 20: 71, 13: 72, 31: 73, 16: 74, 12: 75, 29: 76, 30: 77, 11: 78, 83: 79, 19: 80}
    df['zip_code'].replace(mapping, inplace=True)

    mapping_type = {'HOUSE': 1, 'APARTMENT': 0}
    df['property_type'].replace(mapping_type, inplace=True)

    mapping_kitchen = {False: 0, True: 1}
    df['equipped_kitchen'].replace(mapping_kitchen, inplace=True)

    mapping_pool = {False: 0, True: 1}
    df['swimming_pool'].replace(mapping_pool, inplace=True)

    mapping_state = {'NEW': 5, 'JUST RENOVATED': 4,
                     'GOOD': 3, 'TO RENOVATE': 2, 'TO REBUILD': 1}
    df['building_state'].replace(mapping_state, inplace=True)

    df['equipped_kitchen'].fillna(0, inplace=True)

    df['land_area'].fillna(0, inplace=True)

    df['terrace_area'].fillna(0, inplace=True)

    df['facades_number'].fillna(1, inplace=True)

    dictionary = df.to_dict(orient='records')

    return dictionary[0]



