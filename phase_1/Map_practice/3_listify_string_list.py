#Write a Python program to listify the list of given strings individually using Python map

color = ['Red', 'Blue', 'Black', 'White', 'Pink']

listify = map(list, color)

print(list(listify))