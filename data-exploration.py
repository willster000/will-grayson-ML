import os 
import pandas as pd


# List to store the names of CSV files that meet the condition
csv_files_with_high_syn_flag = {}

folder_path = "C:\\Users\\willg\\OneDrive\\CSCI\\summer-2024-work\\will-grayson-ML\\unlabeled\\data\\test"

# Iterate over all files in the current working directory
for filename in os.listdir(folder_path):
    # Check if the file is a CSV file
    if filename.endswith('.csv'):
        # Load the CSV file
        df = pd.read_csv(os.path.join(folder_path, filename))
        # Check if 'syn_flag_number' column exists in the DataFrame
        if 'syn_flag_number' in df.columns:
            # Get the count of values in the 'syn_flag_number' column that are above 0.5
            count = df[df['syn_flag_number'] > 0.9].shape[0]
            if count > 0:
                # If the count is greater than 0, add the filename and count to the dictionary
                csv_files_with_high_syn_flag[filename] = count

# Print the counts for each CSV file
for filename, count in csv_files_with_high_syn_flag.items():
    print(f'{filename}: {count}')
