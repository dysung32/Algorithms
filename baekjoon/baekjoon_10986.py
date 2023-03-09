import sys
input = sys.stdin.readline

N, M = map(int, input().split())

A = list(map(int, input().split()))
A_sum = [0] * N
same_idx = [0] * M

ans = 0
A_sum[0] = A[0]

for i in range(1, N):
    A_sum[i] = A_sum[i-1] + A[i]

for i in range(N):
    remainder = A_sum[i] % M
    if remainder == 0: # 0번째 인덱스에서 i 인덱스까지의 합이 M으로 나누어 떨어진다는 뜻!
        ans += 1
    same_idx[remainder] += 1

for i in range(M):
    if same_idx[i] > 1: # 적어도 같은 나머지 값을 갖는 애가 2개 이상 있으면!
        ans += (same_idx[i] * (same_idx[i] - 1) // 2) # 이 연산 수행한다!

print(ans)

