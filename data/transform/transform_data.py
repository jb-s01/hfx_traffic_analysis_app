import pandas as pd
from sklearn.preprocessing import OneHotEncoder

def transform_data(file_path):
    # Load the dataset
    data = pd.read_csv(file_path)
    
    # Step 1: Handle missing values
    # For simplicity, drop columns with a high percentage of missing values and rows with any missing value
    # Customize this step based on your specific needs and knowledge about the dataset
    columns_with_too_many_nulls = ['ROAD_LOCATION_2', 'NON_FATAL_INJURY', 'FATAL_INJURY', 'UNUSUAL_ENVIRO_2']
    data.drop(columns=columns_with_too_many_nulls, inplace=True)
    #data.dropna(inplace=True)
    
    # Step 2: Encode categorical variables
    # Select categorical variables to be encoded
    categorical_columns = ['WEATHER_CONDITION', 'LIGHT_CONDITION', 'ROAD_CONDITION', 'ARTIFICIAL_LIGHT_CONDITION']
    data = pd.get_dummies(data, columns=categorical_columns)
    
    # Step 3: Extract date and time components from 'ACCIDENT_DATETIME'
    data['ACCIDENT_DATETIME'] = pd.to_datetime(data['ACCIDENT_DATETIME'])
    data['Year'] = data['ACCIDENT_DATETIME'].dt.year
    data['Month'] = data['ACCIDENT_DATETIME'].dt.month
    data['Day'] = data['ACCIDENT_DATETIME'].dt.day
    data['Hour'] = data['ACCIDENT_DATETIME'].dt.hour
    
    # Optional: Create additional time-based features like 'Weekday' if needed
    data['Weekday'] = data['ACCIDENT_DATETIME'].dt.weekday
    
    # Step 4: Drop columns not useful for the model
    # Customize this list based on your model's needs and the insights you've gathered from the data
    columns_to_drop = ['ACCIDENT_DATETIME', 'COLLISION_SK', 'CASE_FILE_NUMBER']
    data.drop(columns=columns_to_drop, inplace=True)
    
    return data

# Example usage
file_path = '/Users/jbslaunwhite01/projects/hfx_traffic_analysis_app/data/raw/Traffic_Collisions.csv'
data = transform_data(file_path)
print(data.value_counts)