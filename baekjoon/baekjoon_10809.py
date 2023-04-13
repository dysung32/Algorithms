import sys
from string import ascii_lowercase
input = sys.stdin.readline


S = input()

alphas = list(ascii_lowercase)
indexes = [-1] * len(alphas)

for i in range(len(S)):
    for j in range(len(alphas)):
        if S[i] == alphas[j] and indexes[j] == -1:
            indexes[j] = i
            break

print(*indexes)