# 제로
import sys

K = int(sys.stdin.readline())
stack = []
sum = 0

for _ in range(K):
    num = int(sys.stdin.readline())
    if num != 0:
        stack.append(num)
    else:
        stack.pop()

for i in range(len(stack)):
    sum += stack[i]

print(sum)