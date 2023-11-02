#I want to create 100 empty folder. The folders should be name like 1a, 2a, 3a up to 100a.  All thosose folders should be inside a folder named "all". Write me a python script for that.
import os

# Create the main folder
main_folder = 'all'
os.makedirs(main_folder, exist_ok=True)

# Generate and create the empty folders
for i in range(1, 101):
    folder_name = f'{i}a'
    folder_path = os.path.join(main_folder, folder_name)
    os.makedirs(folder_path, exist_ok=True)
    print(f'Folder {folder_name} created.')

print('All folders created successfully.')
