import sys
input = sys.stdin.readline

dc = [-1, 0, 1]

N, M = map(int, input().split())

arr = [[0] * M] * N

for r in range(N):
    arr[r] = list(map(int, input().split()))

# 지구 -> 달로 가는 경우 좌하, 하, 우하로 움직일 수 있음.
# 전에 움직인 방향으로 두번 연속 움직일 수 X

min = sys.maxsize

def go_to_moon(r, c, sum):
    if r == N - 1:
        global min
        if min > sum:
            min = sum
            return

    for i in range(3):
        nc = c + dc[i]
        if nc < 0 or nc >= M:
            continue
        sum += arr[r + 1][nc]
        go_to_moon(r + 1, nc, sum)


for c in range(M):
    go_to_moon(0, c, arr[0][c])

print(min)
