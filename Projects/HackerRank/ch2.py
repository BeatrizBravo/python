# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#



def solve(meal_cost, tip_percent, tax_percent):
    # Calculate tip amount
    tip = meal_cost * (tip_percent / 100)

    # Calculate tax amount
    tax = meal_cost * (tax_percent / 100)

    # Calculate total cost
    total_cost = meal_cost + tip + tax

    # Round total cost to nearest integer
    rounded_cost = round(total_cost)

    # Print rounded cost
    print(rounded_cost)


# Read input values
meal_cost = float(input("write the price of the meal: "))
tip_percent = int(input("Write the tip percent for the meal: "))
tax_percent = int(input("Write the tax percent for the meal: "))

# Call solve function with input values
solve(meal_cost, tip_percent, tax_percent)
