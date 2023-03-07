import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# N: 표의 크기
# M: 합을 구해야 하는 횟수

A = [[0] * (N + 1)]
sum_A = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(N):
    A_row = [0] + [int(x) for x in input().split()]
    A.append(A_row)

for r in range(1, N + 1):
    for c in range(1, N + 1):
        sum_A[r][c] = sum_A[r][c-1] + sum_A[r-1][c] - sum_A[r-1][c-1] + A[r][c]


for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    ans = sum_A[x2][y2] - sum_A[x1-1][y2] - sum_A[x2][y1-1] + sum_A[x1-1][y1-1]
    print(ans)