import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

board = []
visited = [[False] * m for _ in range(n)]
ans = [[-1] * m for _ in range(n)]

final_r, final_c = 0, 0

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for r in range(n):
    line = list(map(int, input().split()))
    for c in range(m):
        if line[c] == 2:
            final_r = r
            final_c = c
        elif line[c] == 0:
            ans[r][c] = 0
    board.append(line)

def go(r, c):
    queue = deque()
    queue.append((r, c))
    ans[r][c] = 0
    visited[r][c] = True

    while queue:
        rr, cc = queue.popleft()

        for i in range(4):
            nr = rr + dr[i]
            nc = cc + dc[i]

            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and board[nr][nc] == 1:
                visited[nr][nc] = True
                ans[nr][nc] = ans[rr][cc] + 1
                queue.append((nr, nc))

go(final_r, final_c)

for r in range(n):
    for c in range(m):
        if ans[r][c] == 1 and not visited[r][c]:
            ans[r][c] = -1

for a in ans:
    print(*a)