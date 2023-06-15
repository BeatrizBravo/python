name = input("what's your name? ")
contact = input("How can you be contacted? ")
theme = input("what topics do you like? ")
place = input("where would you like to go now? ")
time = input("what is the best time of day for you? ")
animal = input("write an animal :  ")
verb1 = input("write of a verb: ")
day = input("what day of the week do you like?")
body = input("write a part of the body: ")


madlib = f"\n\n{name} is having a {theme} party!!\n It's goig be at {place} on {day}.\n " \
         f"Please make sure to show up at {time}, or else you will be required to {verb1} a/an {animal} with" \
         f" your {body}. \n\n RSPV at {contact}."

print(madlib)