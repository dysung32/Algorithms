import sys
input = sys.stdin.readline

N, K = map(int, input().split())
H = list(map(int, input().split()))

diffs = [0] * N
for i in range(1, N):
    diffs[i] = H[i] - H[i-1]

diffs.sort(reverse=True)
print(sum(diffs[K-1:]))