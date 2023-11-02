# want to create 10 text files. Each file should have as name the current date. Write me a Python script for that.
# import os
# import datetime
#
# # Create a directory to store the text files
# directory = 'text_files'
# os.makedirs(directory, exist_ok=True)
#
# # Get the current date
# current_date = datetime.date.today()
#
# # Generate and save text files with current date as the file name
# for i in range(10):
#     file_name = f'{current_date}_{i+1}.txt'
#     file_path = os.path.join(directory, file_name)
#     with open(file_path, 'w') as file:
#         file.write('This is a sample text.')
#     print(f'File {file_name} created.')
#
# print('All files created successfully.')

#I want the files to be in the format YYYY.MM.DD-n. Rewrite the script.
import os
import datetime

# Create a directory to store the text files
directory = 'text_files'
os.makedirs(directory, exist_ok=True)

# Get the current date
current_date = datetime.date.today()

# Generate and save text files with formatted names
for i in range(10):
    file_name = f'{current_date.strftime("%Y.%m.%d")}-{i+1}.txt'
    file_path = os.path.join(directory, file_name)
    with open(file_path, 'w') as file:
        file.write('This is a sample text.')
    print(f'File {file_name} created.')

print('All files created successfully.')
