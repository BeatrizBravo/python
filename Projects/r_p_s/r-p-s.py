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


choice = rps()
user_choice = input("Rock, Paper, Scissor: ")
user_choice = user_choice.lower()
if user_choice == "rock" and choice == "paper":
    print(f"Computer picked {choice} so you lose! ")
elif user_choice == "rock" and choice == "scissors":
    print(f"Computer picked {choice} so you win! ")
elif user_choice == "rock" and choice == "rock":
    print(f"Computer picked {choice} so you draw! ")

if user_choice == "paper" and choice == "paper":
    print(f"Computer picked {choice} so you draw! ")
elif user_choice == "paper" and choice == "scissors":
    print(f"Computer picked {choice} so you lose! ")
elif user_choice == "paper" and choice == "rock":
    print(f"Computer picked {choice} so you win! ")

elif user_choice == "scissors" and choice == "paper":
    print(f"Computer picked {choice} so you win! ")
elif user_choice == "scissors" and choice == "scissors":
    print(f"Computer picked {choice} so you draw! ")
elif user_choice == "scissors" and choice == "rock":
    print(f"Computer picked {choice} so you lose! ")