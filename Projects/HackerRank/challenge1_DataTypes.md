# Objective
Today, we're discussing data types. 

# Task
Complete the code in the editor below. The variables **i, d, and s** are already declared and initialized for you. You must:

1. Declare  variables: one of type int, one of type double, and one of type String.
2. Read  lines of input from stdin (according to the sequence given in the Input Format section below) and initialize your  variables.
3. Use the  operator to perform the following operations:
   - Print the sum of **i** plus your int variable on a new line.
   - Print the sum of  **d** plus your double variable to a scale of one decimal place on a new line.
   - Concatenate **s** with the string you read as input and print the result on a new line.

## Input Format

The first line contains an integer that you must sum with **i**.
The second line contains a double that you must sum with **d**.
The third line contains a string that you must concatenate with **s**.

## Output Format

Print the sum of both integers on the first line, the sum of both doubles (scaled to  decimal place) on the second line, and then the two concatenated strings on the third line.

## Sample Input
```
12
4.0
is the best place to learn and practice coding!
```
## Sample Output

```
16
8.0
HackerRank is the best place to learn and practice coding!
```
# Explanation

When we sum the integers  and , we get the integer .
When we sum the floating-point numbers  and , we get .
When we concatenate HackerRank with is the best place to learn and practice coding!, we get HackerRank is the best place to learn and practice coding!.

You will not pass this challenge if you attempt to assign the Sample Case values to your variables instead of following the instructions above and reading input from stdin.