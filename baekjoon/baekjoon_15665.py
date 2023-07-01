import sys
input = sys.stdin.readline

N, M = map(int, input().split())

nums = sorted(list(map(int, input().split())))
visited = [False] * N

arr = []

def dfs():
    if len(arr) == M:
        print(*arr)
        return
    last_one = 0
    for i in range(N):
        if last_one != nums[i]:
            arr.append(nums[i])
            last_one = nums[i]
            dfs()
            arr.pop()

dfs()