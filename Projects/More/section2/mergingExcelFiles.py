import os
import pandas as pd

# Specify the folder path where the Excel files are located
folder_path = 'excel_files'

# Get all the file names in the folder
file_names = os.listdir(folder_path)

# Create an empty list to store the DataFrames
dfs = []

# Iterate over each file in the folder
for file_name in file_names:
    # Check if the file is an Excel file
    if file_name.endswith('.xlsx') or file_name.endswith('.xls'):
        # Get the full path of the file
        file_path = os.path.join(folder_path, file_name)

        # Read the Excel file into a DataFrame
        df = pd.read_excel(file_path)

        # Append the DataFrame to the list
        dfs.append(df)

# Concatenate the DataFrames into a single DataFrame
merged_data = pd.concat(dfs, ignore_index=True)

# Specify the output file name for the merged data
output_file = 'merged_data.xlsx'

# Save the merged data to a new Excel file
merged_data.to_excel(output_file, index=False)

print('Excel files merged successfully into', output_file)
