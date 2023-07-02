import sys
input = sys.stdin.readline

N, M = map(int, input().split())

nums = list(map(int, input().split()))
nums = list(set(nums))
nums.sort()

arr = []

def dfs():
    if len(arr) == M:
        if arr == sorted(arr):
            print(*arr)
        return

    for i in range(len(nums)):
        arr.append(nums[i])
        dfs()
        arr.pop()

dfs()