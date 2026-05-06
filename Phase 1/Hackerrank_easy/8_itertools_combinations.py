#https://www.hackerrank.com/challenges/itertools-combinations/problem

from itertools import combinations

SK = input().split(" ")

s,k = SK[0], int(SK[1])

s = sorted(s)

for i in range(1, k+1):
    print(*("".join(combination) for combination in combinations(s, i)), sep="\n")
