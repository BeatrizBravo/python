# El módulo random se utiliza para generar números aleatorios
# El módulo requests se utiliza para hacer solicitudes HTTP
import random
import requests

# La función random_pokemon genera un número de Pokemon aleatorio, hace una solicitud a la API de Pokemon y devuelve un diccionario con algunas estadísticas del Pokemon.
def random_pokemon():
    # Selecciona un número al azar entre 1 y 151 para el Pokemon
    pokemon_number = random.randint(1, 151)
    # Construye la URL para la API de Pokemon usando el número de Pokemon seleccionado
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    # Hace una solicitud a la API de Pokemon usando la URL y devuelve la respuesta en formato JSON
    response = requests.get(url)
    pokemon = response.json()
    # Devuelve un diccionario con algunas estadísticas del Pokemon seleccionado
    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
    }

# La función run llama a la función random_pokemon dos veces, una vez para elegir el Pokemon del jugador y otra vez para elegir el Pokemon de la computadora. Luego, solicita al usuario que seleccione una estadística con la que desea jugar.
def run():
    # Llama a la función random_pokemon para elegir el Pokemon del jugador
    my_pokemon = random_pokemon()

    # Muestra el nombre, ID, altura y peso del Pokemon del jugador.
    print('You were given \"{}\"\n'.format(my_pokemon['name']),
          'id {}\n'.format(my_pokemon['id']),
          'height {}\n'.format(my_pokemon['height']),
          'weight {}\n'.format(my_pokemon['weight']))

    #Preguntamos al usuario que categoria quiere jugar para comparar con el oponente
    stat_choice_by_user = input('Which stat do you want to use? (id, height, weight) ::')

    #la computadora toma una carta al azar
    opponent_pokemon_computer = random_pokemon()

    print('The opponent chose {}\n'.format(opponent_pokemon_computer['name']),
          'id {}\n'.format(opponent_pokemon_computer['id']),
          'height {}\n'.format(opponent_pokemon_computer['height']),
          'weight {}\n'.format(opponent_pokemon_computer['weight']))

    #De la categoria que el usuario eligio , la buscamos dentro de las cartas del usuario
    my_stat = my_pokemon[stat_choice_by_user]

    #De la categoria que el usuario eligio , la buscamos dentro de las cartas del ordenador
    opponent_stat = opponent_pokemon_computer[stat_choice_by_user]

    #mostramos los stat de cada uno
    print("====================================")
    print(f'your stat was: {my_stat}')
    print(f'computer  stat was: {opponent_stat}')
    print("====================================")

    #comparamos categorias entre los 2 oponenetes.
    if my_stat > opponent_stat:
        print('You Win!')
    elif my_stat < opponent_stat:
        print('You Lose!')
    else:
        print('Draw!')
run()
