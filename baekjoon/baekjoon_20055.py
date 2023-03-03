import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())

A = deque(list(map(int, input().split())))

# 0은 올리는 위치
# N-1은 내리는 위치
# idx 더 큰 로봇부터, 한 칸 이동할 수 있으면 이동함.
# 이동하려는 칸에 로봇이 없고, 그 칸의 내구도가 1 이상이어야 가능함.
# 로봇이 이동하면 그 이동한 칸의 내구도는 1 감소
# 올리는 위치의 칸 내구도가 0이 아니면 로봇을 올린다.
# 내구도가 0인 칸이 K개 이상이면 종료!
# 종료되었을 때 몇번째 단계가 진행중이었는지 구해보자.

robots = deque([0] * N)
ans = 0

while True:
    A.rotate(1) # 컨베이어 벨트 rotate
    robots.rotate(1) # 이에 따라 로봇 위치도 rotate됨
    robots[-1] = 0 # 내리는 위치에 도달 -> OUT
    if sum(robots):
        for i in range(N-2, -1, -1):
            if robots[i] == 1 and robots[i+1] == 0 and A[i+1] >= 1:
                robots[i+1] = 1
                robots[i] = 0
                A[i+1] -= 1
        robots[-1] = 0 # 내리는 위치에 도달 -> OUT
    if robots[0] == 0 and A[0] >= 1:
        robots[0] = 1
        A[0] -= 1
    ans += 1
    if A.count(0) >= K:
        break

print(ans)