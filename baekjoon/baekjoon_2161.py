import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

queue = deque()
ans = []

for i in range(1, N + 1):
    queue.append(i)

while len(queue) > 1:
    ans.append(queue.popleft())
    queue.append(queue.popleft())

ans.append(queue[0])
print(*ans)