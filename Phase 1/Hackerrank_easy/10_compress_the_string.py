#https://www.hackerrank.com/challenges/compress-the-string/problem

import itertools

data = list(input())

for character_key, group in itertools.groupby(data):
    print(f"({len(list(group))}, {character_key})", end=" ")