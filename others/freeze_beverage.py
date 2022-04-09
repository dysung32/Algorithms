# 음료수 얼려 먹기
# N x M 크기의 얼음 틀
# 구명이 뚫려 있는 부분은 0
# 칸막이가 존재하는 부분은 1
# 얼음 틀 모양이 주어졌을 때 생성되는 총 아이스크림 개수 구하기

# ex) 4 X 5 얼음틀은 3개의 아이스크림이 생성됨
# 00110
# 00011
# 11111
# 00000

# DFS 활용할 것

def dfs(x, y):
    # 주어진 범위를 벗어나면 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0: # 현재 노드를 방문하지 않았다면
        graph[x][y] = 1 # 방문 처리
        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input())))

result = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            result += 1

print(result)


