# 1954. 달팽이 숫자

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    
    dx = [[-1, 0], [1, 0]] # 좌 우
    dy = [[0, -1], [0, 1]] # 상 하
    
    x, y = 0, 0 # 현재 위치