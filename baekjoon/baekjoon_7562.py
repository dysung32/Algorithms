import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

dr = [-2, -2, -1, -1, 1, 1, 2, 2]
dc = [-1, 1, -2, 2, -2, 2, -1, 1]

def bfs(cur_r, cur_c, dest_r, dest_c):
    queue = deque()
    queue.append((cur_r, cur_c))
    board[cur_r][cur_c] = 1

    while queue:
        r, c = queue.popleft()

        if r == dest_r and c == dest_c:
            print(board[r][c] - 1)
            return

        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < l and 0 <= nc < l and board[nr][nc] == 0:
                queue.append((nr, nc))
                board[nr][nc] = board[r][c] + 1


for _ in range(T):
    l = int(input())
    cur_r, cur_c = map(int, input().split())
    dest_r, dest_c = map(int, input().split())

    board = [[0] * l for _ in range(l)]

    bfs(cur_r, cur_c, dest_r, dest_c)

