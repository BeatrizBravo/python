import os
import random

# List of pet names
pet_names = ['Max', 'Bella', 'Charlie', 'Luna', 'Lucy', 'Cooper', 'Max', 'Bailey', 'Daisy', 'Sadie', 'Molly', 'Buddy', 'Lola', 'Rocky', 'Stella', 'Milo', 'Tucker', 'Bear', 'Oliver', 'Zoe']

# Create a directory to store the text files
directory = 'pet_names'
os.makedirs(directory, exist_ok=True)

# Generate and save text files with pet names
for i in range(100):
    file_name = f'{directory}/pet{i+1}.txt'
    pet_name = random.choice(pet_names)
    with open(file_name, 'w') as file:
        file.write(pet_name)
    print(f'File {file_name} created with pet name: {pet_name}')
