import pandas as pd
import os

#global variables
FILEPATH = "Data/raw_data"

#create dictionary of all month's data

def create_data_dict(filepath):
    data_dict = {}

    for folder in os.listdir(filepath):
        for filename in os.listdir(filepath + '/' +folder):
            data_dict[folder[:folder.find('_')]] = pd.read(filepath + '/' +folder+ '/' +filename)
    
    return data_dict


#check data has consistent columns

def test_cols_same(default_month, data_dict):

    july_col = list(pd.read_csv(data_dict['July']).columns)

    columns_dict = {}

    for key, values in data_dict.items():
        month_col = list(pd.read_csv(values).columns)
        incon_col =[col for col in month_col if col not in july_col]
        if len(incon_col) > 0:
            columns_dict[key] = incon_col
            
    return columns_dict
    
## TO DO: insert error here if columns_dict len > 1

#join datasets together

def join_datasets(data_dict):
    datasets = []

    for key, values in data_dict.items():
        my_data = pd.read_csv(values, index_col=None, header=0)
        my_data['Month'] = key
        datasets.append(my_data)
    
    full_dataset = pd.concat(datasets, axis=0, ignore_index=True)
    return full_dataset