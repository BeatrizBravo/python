n = int(input("write your number to check if weird of no weird:  "))

if n % 2 != 0:
    # n is odd
    print("Weird")
elif n >= 2 and n <= 5:
    # n is even and in the inclusive range of 2 to 5
    print("Not Weird")
elif n >= 6 and n <= 20:
    # n is even and in the inclusive range of 6 to 20
    print("Weird")
else:
    # n is even and greater than 20
    print("Not Weird")
