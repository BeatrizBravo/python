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

