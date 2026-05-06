#https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem

from itertools import combinations_with_replacement

SK = input().split(" ")

s,k = SK[0], int(SK[1])

s = sorted(s)

print(*("".join(combination) for combination in combinations_with_replacement(s, k)), sep="\n")
