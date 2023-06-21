chairs = '15'
nails = 4
total_nails = chairs * nails
message = 'I need to buy {} nails'.format(total_nails)
print('You need to buy {} nails'.format(message))


#############

my_name = "Penelope"
my_age = 29
message = 'My name is {} and I am {} years old'.format(my_name, my_age)
print(message)

#########
# Number of eggs in each box
eggs_per_box = 6

# Number of eggs needed for each omelette
eggs_per_omelette = 4

# Number of boxes of eggs
boxes_of_eggs = 6

# Calculate the total number of eggs
total_eggs = boxes_of_eggs * eggs_per_box

# Calculate the number of omelettes that can be made
omelettes = total_eggs // eggs_per_omelette  #integer division

# Print the result
print(f"You can make {omelettes} omelettes with {boxes_of_eggs} boxes of eggs.")
