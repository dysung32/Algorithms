import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

miro = [[] * M for _ in range(N)]

for i in range(N):
    miro[i] = list(map(int, input().strip()))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c):
    queue = deque()
    queue.append((r, c))

    while queue:
        rr, cc = queue.popleft()
        for i in range(4):
            nr = rr + dr[i]
            nc = cc + dc[i]

            if nr < 0 or nc < 0 or nr >= N or nc >= M:
                continue

            if miro[nr][nc] == 0:
                continue

            if miro[nr][nc] == 1:
                miro[nr][nc] = miro[rr][cc] + 1
                queue.append((nr, nc))

    return miro[N - 1][M - 1]

print(bfs(0, 0))

