import sys
input = sys.stdin.readline

from queue import PriorityQueue

V, E = map(int, input().split()) # V: 노드 개수, E: 엣지 개수
K = int(input()) # K: 출발 노드
distance = [sys.maxsize] * (V + 1)
visited = [False] * (V + 1)
myList = [[] for _ in range(V+1)]

queue = PriorityQueue()

for _ in range(E):
    u, v, w = map(int, input().split())
    myList[u].append((v, w)) # v: 인접 노드, w: 가중치

queue.put((0, K)) # (가중치, 노드)
distance[K] = 0

while queue.qsize() > 0:
    cur = queue.get()
    c_v = cur[1]
    if visited[c_v]: # 방문한 노드라면 continue
        continue
    visited[c_v] = True
    for tmp in myList[c_v]:
        next = tmp[0] # 다음 노드
        value = tmp[1] # 가중치
        if distance[next] > distance[c_v] + value:
            distance[next] = distance[c_v] + value
            queue.put((distance[next], next))

for i in range(1, V + 1):
    if distance[i] != sys.maxsize:
        print(distance[i])
    else:
        print("INF")
