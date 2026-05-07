""" 
Create a function that receives any quantity of numbers and returns their sum.
It has to run with 0, 1 or more arguments.

Examples:
flexible_sum(1, 2, 3) → 6
flexible_sum(10) → 10
flexible_sum() → 0
"""

def flexible_sum(*args):
    return sum(args)

list_len = int(input())

int_list = [int(input()) for _ in range(list_len)]

print(flexible_sum(*int_list))