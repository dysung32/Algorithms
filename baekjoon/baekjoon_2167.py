import sys
input = sys.stdin.readline

N, M = map(int, input().split())

A = [[0] * (M + 1)]
A_sum = [[0] * (M+1) for _ in range(N+1)]

for _ in range(N):
    A_row = [0] + list(map(int, input().split()))
    A.append(A_row)

for r in range(1, N+1):
    for c in range(1, M+1):
        A_sum[r][c] = A_sum[r-1][c] + A_sum[r][c-1] + A[r][c] - A_sum[r-1][c-1]

K = int(input())
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    ans = A_sum[x2][y2] - A_sum[x1 - 1][y2] - A_sum[x2][y1 - 1] + A_sum[x1 - 1][y1 - 1]
    print(ans)