import sys
from collections import deque
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def start():
    time = 0
    while queue:
        time += 1
        while fire_queue and fire_queue[0][2] < time:
            r, c, t = fire_queue.popleft()

            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < h and 0 <= nc < w:
                    if building[nr][nc] == '.' or building[nr][nc] == 'J':
                        building[nr][nc] = 'F'
                        fire_queue.append((nr, nc, t + 1))
        while queue and queue[0][2] < time:
            r, c, t = queue.popleft()
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < h and 0 <= nc < w:
                    if building[nr][nc] == '.' and not visited[nr][nc]:
                        visited[nr][nc] = True
                        queue.append((nr, nc, t + 1))
                else:
                    return time

    return 'IMPOSSIBLE'

h, w = map(int, input().split())
building = []
queue, fire_queue = deque(), deque()
visited = [[False] * w for _ in range(h)]

for r in range(h):
    b = list(input().strip())
    building.append(b)
    for i in range(w):
        if b[i] == 'F':
           fire_queue.append((r, i, 0))
        elif b[i] == 'J':
            visited[r][i] = True
            queue.append((r, i, 0))

ans = start()

print(ans)