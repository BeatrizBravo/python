shopping_list = [ 
"oranges", 
"cat food", 
"sponge cake", 
"long-grain rice", 
"cheese board", 
] 
print(shopping_list[0])

'''
I'm setting up my own market stall to sell chocolates. 
I need a basic till (caja registradora) to check the prices of different chocolates that I sell. 
I've started the program and included the chocolates and their prices. 

TODO:: Finish the program by asking the user to input an item and then *output* its price. 

chocolates = { 
'white': 1.50, 
'milk': 1.20, 
'dark': 1.80, 
'vegan': 2.00, 
} 

'''
chocolates = {
    'white': 1.50,
    'milk': 1.20,
    'dark': 1.80,
    'vegan': 2.00,
}

# Ask user for input
item = input("What chocolate would you like to buy? ")

# Check if item exists in dictionary
if item in chocolates:
    price = chocolates[item]
    print(f"The price of, {item}, chocolate is:, {price}")
else:
    print(f"Sorry, we do not sell, {item}, chocolate.\n")

'''
Write a program that simulates a lottery. 
The program should have a list of seven numbers that represent a lottery ticket. 
It should then generate seven random numbers. 
After comparing the two sets of numbers, the program should output a prize based on the number of matches: 
● £20 for three matching numbers 
● £40 for four matching numbers 
● £100 for five matching numbers 
● £10000 for six matching numbers 
● £1000000 for seven matching numbers 

'''
import random  # import the random module

# define the list of lottery ticket numbers
lotery_ticket_i_bought = [3, 7, 16, 22, 28, 35, 42]

# generate 7 random numbers in the range of 1 to 49
winning_numbers = random.sample(range(1, 50), 7)        #winning_numbers of the lottery.
print(f"The winning number was 🎉🎉🎉🎉🎉🎉🎉: {winning_numbers}")

# count the number of matching numbers **between** ticket and winning_numbers
matches = len(set(lotery_ticket_i_bought).intersection(set(winning_numbers)))
print(f"The number of matching numbers are: {matches}")


#first: converts both lists to sets using the set() function. This is done because sets are unordered collections of unique elements, and this makes it easier to compare the two sets and remove any duplicates.

#intersection() to find the common elements  between the two sets.

#Finally, the len() function is used to count the number of elements in the resulting set of matching numbers. It is stored in the matches variable.

# output the prize based on the number of matches
if matches == 3:
    print("\nCongratulations! You matched 3 numbers and won £20.")
elif matches == 4:
    print("\nCongratulations! You matched 4 numbers and won £40.")
elif matches == 5:
    print("\nCongratulations! You matched 5 numbers and won £100.")
elif matches == 6:
    print("\nWow! You matched 6 numbers and won £10000.")
elif matches == 7:
    print("\nOMG! You matched all 7 numbers and won £1000000!")
else:
    print("\nSorry! Try again next time!")
print(f"\nyour ticket was {lotery_ticket_i_bought}")