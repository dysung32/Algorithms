import sys
input = sys.stdin.readline

N, M = map(int, input().split())

nums = sorted(list(map(int, input().split())))
arr = []

def dfs():
    if len(arr) == M:
        print(*arr)
        return
    for i in range(N):
        arr.append(nums[i])
        dfs()
        arr.pop()

dfs()