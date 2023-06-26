import sys
input = sys.stdin.readline

N, M = map(int, input().split())

nums = sorted(list(map(int, input().split())))
arr = []

def dfs():
    if len(arr) == M:
        if arr == sorted(arr):
            print(*arr)
        return
    for i in range(N):
        if nums[i] not in arr:
            arr.append(nums[i])
            dfs()
            arr.pop()

dfs()