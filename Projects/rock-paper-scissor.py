import random

def rps():
    random_number = random.randint(1, 3)
    if random_number == 1:
        choice = "rock"
    elif random_number == 2:
        choice = "paper"
    else:
        choice = "scissors"
    return choice

print('''
    Welcome to Rock Paper Scissors Game!
    Choose your move:
    1 - Rock
    2 - Paper
    3 - Scissors
''')

user_choice = int(input("Enter your move: "))

