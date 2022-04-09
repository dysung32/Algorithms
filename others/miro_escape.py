# 미로 탈출
# N X M 크기의 직사각형 미로
# 동빈이의 위치: (1, 1)
# 미로의 출구: (N, M)
# 괴물 있는 부분: 0
# 괴물 없는 부분: 1
# 이동 최단 거리 구하기

# BFS로 해결

from collections import deque

N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input())))

# 이동할 4가지 방향 정의 (상,하,좌,우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향으로 위치 확인
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            # 공간 벗어난 경우 무시
            if next_x < 0 or next_x >= N or next_y < 0 or next_y >= M:
                continue
            # 벽인 경우 무시
            if graph[next_x][next_y] == 0:
                continue
            # 해당 노드 처음 방문했다면
            if graph[next_x][next_y] == 1:
                graph[next_x][next_y] = graph[x][y] + 1
                queue.append((next_x, next_y))

    return graph[N - 1][M - 1]

print(bfs(0, 0))