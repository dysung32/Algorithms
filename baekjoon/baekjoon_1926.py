import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

pic = [[] * m for _ in range(n)]

for i in range(n):
    line = list(map(int, input().split()))
    pic[i] = line

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c, pic):
    queue = deque()
    queue.append((r, c))
    cnt = 1
    pic[r][c] = 0

    while queue:
        rr, cc = queue.popleft()
        for i in range(4):
            nr = rr + dr[i]
            nc = cc + dc[i]
            if nr < 0 or nc < 0 or nr >= n or nc >= m:
                continue
            if pic[nr][nc] == 1:
                queue.append((nr, nc))
                pic[nr][nc] = 0
                cnt += 1

    return cnt

pic_list = [0]

for r in range(n):
    for c in range(m):
        if pic[r][c] == 1:
            pic_list.append(bfs(r, c, pic))

# 도화지에 1이 아예 없었을 경우 고려
if max(pic_list) == 0:
    print(0)
    print(0)
else:
    print(len(pic_list) - 1)
    print(max(pic_list))