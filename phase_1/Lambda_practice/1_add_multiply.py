"""
Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, 
                     also create a lambda function that multiplies argument x with argument y and prints the result.

Sample Output:
25
48
"""

add = lambda x: 15 + x
multiply = lambda x, y: x*y

x = int(input(""))

print(add(1))
print(multiply(234,10))