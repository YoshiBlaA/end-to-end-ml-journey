"""
TASK>
The provided code stub reads two integers from STDIN, 'a' and 'b' Add code to print three lines where:

1. The first line contains the sum of the two numbers.
2. The second line contains the difference of the two numbers (first - second).
3. The third line contains the product of the two numbers.

Example:
    a = 3
    b = 5

Print the following
8
-2
15

INPUT FORMAT>
The first line contains the first integer 'a'
The second line contains the second integer 'b'

CONSTRAINTS>
1<=a<=10^10
1<=b<=10^10 

OUTPUT FORMAT>
Print the three lines as explained above
"""

a = int(input())
b = int(input())

print(a+b)
print(a-b)
print(a*b)