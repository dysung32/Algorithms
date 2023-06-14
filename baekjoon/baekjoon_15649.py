import sys
input = sys.stdin.readline

N, M = map(int, input().split())

nums = []

def dfs():
    if len(nums) == M:
        print(*nums)
        return
    for i in range(1, N + 1):
        if i not in nums:
            nums.append(i)
            dfs()
            nums.pop()

dfs()