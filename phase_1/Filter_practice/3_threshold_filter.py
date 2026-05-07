#Write a Python function that filters out all elements less than or equal than a specified value from a list of numbers 
#using the filter function

number_list = [1,2,3,4,5,6,7,8,9,10]

filter_condition = int(input())

apply_filter = filter(lambda x: x <= filter_condition, number_list)

print(list(apply_filter))