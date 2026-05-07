#Write a Python function that filters out even numbers from a list of integers using the filter function.

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_nums = filter(lambda x: x % 2 != 0, nums)

print(list(odd_nums))