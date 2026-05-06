#Write a Python program to triple all numbers in a given list of integers. Use Python map.

list_length = int(input())
integer_list = [int(input()) for _ in range(list_length)]

triple_list = list(map(lambda x: x*3, integer_list))

print(triple_list)