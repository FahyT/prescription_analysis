import pandas as pd
import * from import_data

#global variables
FILEPATH_IN = "Data/raw_data"
FILEPATH_OUT = "Data/processed_data"

data_dict = create_data_dict(FILEPATH_IN)

same_cols = test_cols_same("July",data_dict)

if len(same_cols) > 0:
    raise Exception as ValueError(same_cols)

full_data = join_datasets(data_dict)

full_data.to_csv(FILEPATH_OUT + "/" + "joined_data.csv")