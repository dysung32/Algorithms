import sys
input = sys.stdin.readline

N, M = map(int, input().split())

nums = sorted(list(map(int, input().split())))
visited = [False] * N

arr = []

def dfs():
    if len(arr) == M:
        if arr == sorted(arr):
            print(*arr)
        return
    last_one = 0
    for i in range(N):
        if not visited[i] and last_one != nums[i]:
            visited[i] = True
            arr.append(nums[i])
            last_one = nums[i]
            dfs()
            visited[i] = False
            arr.pop()

dfs()