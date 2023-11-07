import os

# Directory path containing the text files
directory = 'data'

# Get the list of text files in the directory
file_list = [file for file in os.listdir(directory) if file.endswith('.txt')]

# Process each text file
for file_name in file_list:
    file_path = os.path.join(directory, file_name)

    # Read the contents of the text file
    with open(file_path, 'r') as file:
        content = file.read()

    # Split the content into sentences
    sentences = content.split('. ')

    # Capitalize the first letter of each sentence
    capitalized_sentences = [sentence.capitalize() for sentence in sentences]

    # Join the capitalized sentences back into a single string
    new_content = '. '.join(capitalized_sentences)

    # Write the updated content back to the text file
    with open(file_path, 'w') as file:
        file.write(new_content)

print('First letter of each sentence converted to uppercase successfully.')
