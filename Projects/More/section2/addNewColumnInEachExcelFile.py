import os
import pandas as pd

# Specify the folder path where the Excel files are located
folder_path = 'excel_files'

# Get all the file names in the folder
file_names = os.listdir(folder_path)

# Iterate over each file in the folder
for file_name in file_names:
    # Check if the file is an Excel file
    if file_name.endswith('.xlsx') or file_name.endswith('.xls'):
        # Get the full path of the file
        file_path = os.path.join(folder_path, file_name)

        # Read the Excel file into a DataFrame
        df = pd.read_excel(file_path)

        # Calculate the annual salary
        df['annual salary'] = df['monthly salary'] * 12

        # Save the updated DataFrame back to the Excel file
        df.to_excel(file_path, index=False)

print('Annual salary column added to each Excel file successfully!')
