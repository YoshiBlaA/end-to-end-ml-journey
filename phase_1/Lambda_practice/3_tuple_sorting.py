# Write a Python program to sort a list of tuples using Lambda

tuple_list = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

tuple_list_sorted = sorted(tuple_list, key=lambda x: x[1])

print(tuple_list_sorted)