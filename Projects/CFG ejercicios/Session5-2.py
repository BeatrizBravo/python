import requests # send HTTP requests to the PokeAPI.

# List of Pokemon IDs to retrieve data for
pokemon_ids = [1, 25, 133, 150, 151, 248]

# Open a new file called 'pokemon.txt' for writing
with open('pokemon.txt', 'w') as file:

    # Loop through the list of Pokemon IDs
    for id in pokemon_ids:

        # Send a GET request to the PokeAPI using the ID
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{id}')

        # If the response was successful, get the data and write to the file
        if response.status_code == 200:
            pokemon_data = response.json()
            name = pokemon_data['name']
            moves = [move['move']['name'] for move in pokemon_data['moves']]
            file.write(f'Pokemon Name: {name}\n')
            file.write(f'Moves: {", ".join(moves)}\n\n')
