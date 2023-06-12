import sys
from collections import deque
input = sys.stdin.readline

# 폭탄 -> 3초 후 폭발, 인접한 4칸 폭발 -> 빈칸
R, C, N = map(int, input().split())

grid = []
bomb_time = [[-1] * C for _ in range(R)]

for r in range(R):
    g = list(input().strip())
    grid.append(g)
    for c in range(C):
        if g[c] == 'O':
            bomb_time[r][c] = 3

time = 0

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

while time <= N:
    if time != 0 and time % 2 == 0:
        for rr in range(R):
            for cc in range(C):
                if grid[rr][cc] == '.':
                    grid[rr][cc] = 'O'
                    bomb_time[rr][cc] = time + 3

    bomb_queue = deque()
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 'O':
                if bomb_time[i][j] == time:
                    bomb_queue.append((i, j))

    while bomb_queue:
        ii, jj = bomb_queue.popleft()
        grid[ii][jj] = '.'
        bomb_time[ii][jj] = -1
        for k in range(4):
            ni = ii + dr[k]
            nj = jj + dc[k]

            if 0 <= ni < R and 0 <= nj < C and grid[ni][nj] == 'O':
                grid[ni][nj] = '.'
                bomb_time[ni][nj] = -1

    time += 1

for r in range(R):
    for c in range(C):
        print(grid[r][c], end='')
    print()


