#Write a Python program to add three given lists using Python map and lambda.

integer_list_1 = [1,2,3,4,5,8,7]
integer_list_2 = [7,2,4,4,5,1,7]
integer_list_3 = [1,2,4,3,5,4,3]

result = map(lambda x, y, z : x + y + z, integer_list_1, integer_list_2, integer_list_3)

print(list(result))
