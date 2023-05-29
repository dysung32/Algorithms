import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())
nums = [i for i in range(1, N + 1)]

for i in permutations(nums, N):
    cur_perm = list(i)
    bool = True
    for j in range(1, N - 1):
        if abs(cur_perm[j] - cur_perm[j-1]) <= abs(cur_perm[j+1] - cur_perm[j]):
            bool = False
            break
    if bool == True:
        print(cur_perm)
        break
