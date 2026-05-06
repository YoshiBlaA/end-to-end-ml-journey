#Write a Python program to filter a list of integers using Lambda.

int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

filter_function_condition = (lambda x: x % 2)    

even_list = [x for x in int_list if  filter_function_condition(x) == 0]
odd_list = [x for x in int_list if filter_function_condition(x) != 0]

print(even_list)
print(odd_list)