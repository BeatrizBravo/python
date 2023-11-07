import os
import zipfile

# Specify the directory path where the text files are located
directory = 'dataTextFile'

# Get all the file names in the directory
file_names = os.listdir(directory)

# Sort the file names in ascending order
file_names.sort()

# Specify the range for each ZIP file
start_range = 1
end_range = 10
zip_count = 1

# Iterate over the file names and create separate ZIP files
for file_name in file_names:
    # Check if the file is a text file
    if file_name.endswith('.txt'):
        # Get the file ID from the file name
        file_id = int(file_name.split('STAID')[-1].split('.')[0])

        # Check if the file ID is within the range
        if file_id >= start_range and file_id <= end_range:
            # Create a new ZIP file for the range
            zip_file_name = f'files_{start_range:06d}_{end_range:06d}.zip'
            with zipfile.ZipFile(zip_file_name, 'a', compression=zipfile.ZIP_DEFLATED) as zip_file:
                # Add the current file to the ZIP file
                zip_file.write(os.path.join(directory, file_name), file_name)

        # Check if the file ID exceeds the end range
        if file_id > end_range:
            # Update the range for the next ZIP file
            start_range = end_range + 1
            end_range += 10
            zip_count += 1

print(f'{zip_count} ZIP files created successfully')
