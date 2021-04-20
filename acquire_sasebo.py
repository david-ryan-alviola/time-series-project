import env
import pandas as pd

def acquire_sasebo_df():
    """
    This function reads the GlobalLandTerperaturesByCity.csv file and returns a dataframe\
    only containing the data from Sasebo, Japan.
    """
    temp_df = pd.read_csv(env.data_path + "GlobalLandTemperaturesByCity.csv")
    
    return temp_df[temp_df.City == "Sasebo"]