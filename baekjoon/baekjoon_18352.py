import sys
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    while queue:
        cur = queue.popleft()
        for g in graph[cur]:
            if visited[g] == -1:
                visited[g] = visited[cur] + 1
                queue.append(g)

input = sys.stdin.readline
N, M, K, X = map(int, input().split())
visited = [-1] * (N+1)
graph = [[] for c in range(N + 1)]
for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)

visited[X] = 0
bfs(graph, X, visited)

if visited.count(K):
    for i in range(1, N + 1):
        if visited[i] == K:
            print(i)
else:
    print("-1")