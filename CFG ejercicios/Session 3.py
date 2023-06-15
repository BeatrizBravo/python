# Create a program that tells you whether or not you need an umbrella when you leave the house.
# The program should:
# 1. Ask you if it is raining using input()
# 2. If the input is 'y', it should output 'Take an umbrella'
# 3. If the input is 'n', it should output 'You don't need an umbrella'

print("How is the whether like today!!")
print('''
type the right unswer:
"Y" for yes
"N" for no
''')
rain = input("It is raining?")
rain.lower()

if rain == "y":
    print('Take an umbrella') # return if true
else:
    print('You don\'t need an umbrella') # return if false