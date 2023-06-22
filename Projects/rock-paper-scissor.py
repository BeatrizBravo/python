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

#user's choice is not one of the three valid options in the game
if user_choice not in [1, 2, 3]:
    print("Invalid move. Please try again.")
else:
    computer_choice = rps()
    if user_choice == 1:
        print("You chose Rock.")
        if computer_choice == "rock":
            print("Computer also chose Rock. It's a tie!")
        elif computer_choice == "paper":
            print("Computer chose Paper. You lose!")
        elif computer_choice == "scissors":
            print("Computer chose Scissors. You win!")
    elif user_choice == 2:
        print("You chose Paper.")
        if computer_choice == "rock":
            print("Computer chose Rock. You win!")
        elif computer_choice == "paper":
            print("Computer also chose Paper. It's a tie!")
        elif computer_choice == "scissors":
            print("Computer chose Scissors. You lose!")
    elif user_choice == 3:
        print("You chose Scissors.")
        if computer_choice == "rock":
            print("Computer chose Rock. You lose!")
        elif computer_choice == "paper":
            print("Computer chose Paper. You win!")
        elif computer_choice == "scissors":
            print("Computer also chose Scissors. It's a tie!")
