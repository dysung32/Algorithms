import sys
input = sys.stdin.readline

N = int(input())
heights = list(map(int, input().split()))

ans = [0] * N
stack = []

for i in range(N):
    while stack:
        if heights[stack[-1]] < heights[i]:
            stack.pop()
        else:
            ans[i] = stack[-1] + 1
            break
    stack.append(i)

print(*ans)