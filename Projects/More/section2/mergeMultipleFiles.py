import os

# Specify the folder path where the text files are located
folder_path = 'originalData'

# Specify the output file name
output_file = 'merged_multiple_file.txt'

# Get all the file names in the folder
file_names = os.listdir(folder_path)

# Open the output file in write mode
with open(output_file, 'w') as outfile:
    # Iterate over each file in the folder
    for file_name in file_names:
        # Check if the file is a text file
        if file_name.endswith('.txt'):
            # Get the full path of the file
            file_path = os.path.join(folder_path, file_name)

            # Open the file in read mode
            with open(file_path, 'r') as infile:
                # Read the contents of the file
                contents = infile.read()

                # Write the contents to the output file
                outfile.write(contents)
                outfile.write('\n')  # Add a newline after each file

print('Text files merged successfully!')
