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
    print(f"Sorry, we do not sell", '{item}', "chocolate.")
