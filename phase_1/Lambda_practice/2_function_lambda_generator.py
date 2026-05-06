"""
# Define a function 'func_compute' that takes a parameter 'n' and returns a lambda function
# The returned lambda function multiplies its argument 'x' by 'n'
"""

def multiply(y):
    return lambda x: x * y

x = int(input())
y = int(input())

lambda_multiply = multiply(x)

print(lambda_multiply(y))