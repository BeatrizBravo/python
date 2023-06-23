i = 4
d = 4.0
s = 'HackerRank '
# Declare second integer, double, and String variables.
d = 0.0
s = ""

# Read and save an integer, double, and String to your variables.
i = int(input())
d = float(input())
s = input()

# Print the sum of both integer variables on a new line.
sum_i = i + 4
print(sum_i)
# Print the sum of the double variables on a new line.
sum_d = d + 4.0
print("{:.1f}".format(sum_d)) 


'''
string format specifier= {} placeholders for values that will be substituted into the string later.
:.1f = specifies a floating-point value = one digit after the decimal point. 
'''


# Concatenate and print the String variables on a new line
concat_s = "HackerRank " + s
# The 's' variable above should be printed first.
print(concat_s)