import env

from utilities import set_index_to_datetime

_winter = ["December", "January", "February"]
_spring = ["March", "April", "May"]
_summer = ["June", "July", "August"]
_fall = ["September", "October", "November"]

def prepare_sasebo_df(df):
    sasebo_df = df.copy()
    
    # Drop the row with the 2 NaN values
    sasebo_df.dropna(inplace=True)
    
    sasebo_df = set_index_to_datetime(sasebo_df, 'dt')
    
    # Convert celsius to fahrenheit
    sasebo_df.AverageTemperature = (sasebo_df.AverageTemperature * 1.8) + 32
    sasebo_df.rename(columns={'AverageTemperature' : 'avg_temp'}, inplace=True)
    sasebo_df.drop(columns=['AverageTemperatureUncertainty', 'City', 'Country', 'Latitude', 'Longitude'], inplace=True)
    
    return _add_features(sasebo_df)
    
def _add_features(df):
    sasebo_df = df.copy()
    
    sasebo_df['day_of_week'] = sasebo_df.index.day_name()
    sasebo_df['month'] = sasebo_df.index.month_name()
    sasebo_df['season'] = sasebo_df.month.apply(_determine_season)
    
    return sasebo_df

def _determine_season(month):
    if month in _winter:
        return "Winter"
    
    elif month in _spring:
        return "Spring"
    
    elif month in _summer:
        return "Summer"
    
    elif month in _fall:
        return "Fall"
    
    else:
        return ""