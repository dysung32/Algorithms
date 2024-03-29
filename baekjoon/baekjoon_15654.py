import sys
input = sys.stdin.readline

N, M = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()

stack = []

def dfs():
    if len(stack) == M:
        print(*stack)
        return
    for i in range(N):
        if nums[i] not in stack:
            stack.append(nums[i])
            dfs()
            stack.pop()

dfs()