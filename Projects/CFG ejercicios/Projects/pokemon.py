import random
import requests


def random_pokemon():
    pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()
    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
    }


def run():
    my_pokemon = random_pokemon()

    print('You were given \"{}\"\n'.format(my_pokemon['name']),
            'id {}\n'.format(my_pokemon['id']),
            'height {}\n'.format(my_pokemon['height']),
            'weight {}\n'.format(my_pokemon['weight']))


    stat_choice_by_user = input('Which stat do you want to use? (id, height, weight) ')

    opponent_pokemon_computer = random_pokemon()

    print('The opponent chose {}\n'.format(opponent_pokemon_computer['name']),
          'id {}\n'.format(opponent_pokemon_computer['id']),
          'height {}\n'.format(opponent_pokemon_computer['height']),
          'weight {}\n'.format(opponent_pokemon_computer['weight']))

    my_stat = my_pokemon[stat_choice_by_user]
    opponent_stat = opponent_pokemon_computer[stat_choice_by_user]

    if my_stat > opponent_stat:
        print('You Win!')
    elif my_stat < opponent_stat:
        print('You Lose!')
    else:
        print('Draw!')
run()
