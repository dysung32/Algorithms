import sys
input = sys.stdin.readline

N = int(input())
heights = []
stack = []
h_sum = 0

for _ in range(N):
    heights.append(int(input()))

for h in heights:
    cnt = 0
    while stack and stack[-1] <= h:
        stack.pop()
    stack.append(h)

    h_sum += len(stack) - 1

print(h_sum)