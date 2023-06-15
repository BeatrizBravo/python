'''
Your friend works for an antique book shop that sells books
between 1800 and 1950 and
wants to quickly categorise books
by the century and
decade that they were written.
Write a program that takes:
 a year (e.g. 1872) and
outputs the century and decade (e.g. "Nineteenth Century, Seventies")
'''

# categorize a year into a century and decade
def categorize_year(year):
    '''
    the function  takes a year as input,
    calculates the century and decade that it falls into,
    and maps those values to a string representing the century and decade.
    :param year: int
    :return: str
    '''
    # Calculate the century
    century = (year // 100) + 1

    # Calculate the decade
    decade = year % 100 #get reminder only
    decade = decade//10 # divide and round decade down to the nearest integer

    # Map the century and decade to a string value
    century_str = ""
    decade_str = ""

    if century == 18:
        century_str = "Eighteenth Century"
    elif century == 19:
        century_str = "Nineteenth Century"
    elif century == 20:
        century_str = "Twentieth Century"
    elif century == 21:
        century_str = "Twentieth one Century"

    else:
        century_str = "Unknown Century"

    if decade == 0:
        decade_str = "Zeroes"
    elif decade == 1:
        decade_str = "Tens"
    elif decade == 2:
        decade_str = "Twenties"
    elif decade == 3:
        decade_str = "Thirties"
    elif decade == 4:
        decade_str = "Forties"
    elif decade == 5:
        decade_str = "Fifties"
    elif decade == 6:
        decade_str = "Sixties"
    elif decade == 7:
        decade_str = "Seventies"
    elif decade == 8:
        decade_str = "Eighties"
    elif decade == 9:
        decade_str = "Nineties"
    else:
        decade_str = "Unknown Decade"

    # Return the century and decade string
    return f"{century_str} , {decade_str}"

# Ask the user for a year to categorize
year = int(input("Enter a year between 1800 and 2099: "))

# Call the categorize_year function with the user's input and print the result
print(categorize_year(year))

