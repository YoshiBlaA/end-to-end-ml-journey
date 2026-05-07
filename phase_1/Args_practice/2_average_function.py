"""
Modify previous sum function to calculate the average. Handle empty list case.

Examples:
mean(10, 20, 30) → 20.0
mean(1, 2, 3, 4, 5) → 3.0
"""

def flexible_sum(*args):
    if not args:
        return "No items in the list!"
    return sum(args) / len(args)

list_len = int(input())

int_list = []
for _ in range(list_len):
    usr_input = input().strip()
    int_list.append(int(usr_input) if usr_input else 0)

print(flexible_sum(*int_list))