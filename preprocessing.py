import pandas as pd
import glob
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler

# List all CSV files
all_files = glob.glob("C:\\Users\\willg\\OneDrive\\CSCI\\summer-2024-work\\will-grayson-ML\\train\\*.csv")

# Initialize an empty list to hold DataFrames
df_list = []

# Loop over all CSV files and append DataFrames to the list
for file in all_files:
    df = pd.read_csv(file)
    df_list.append(df)

# Concatenate all DataFrames into one
final_df = pd.concat(df_list, ignore_index=True)

# Now you can use `final_df` to train your model
#print(final_df.head())
#print(final_df.columns)
#print(final_df.shape)


# Create a scaler object
scaler = MinMaxScaler()

# Fit the scaler to the features and transform
scaled_features = scaler.fit_transform(final_df)

# Convert the scaled features to a DataFrame
scaled_df = pd.DataFrame(scaled_features, columns=final_df.columns)

print(scaled_df.head())