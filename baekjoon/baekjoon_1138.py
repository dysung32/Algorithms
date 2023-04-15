import sys
input = sys.stdin.readline

N = int(input())

H = list(map(int, input().split()))
ans = [0] * N

for i in range(N):
    h = H[i] # h: 왼쪽에 위치하고 나보다 큰 사람들의 수
    cnt = 0
    for j in range(N):
        if ans[j] == 0 and cnt == h:
            ans[j] = i + 1
            break
        elif ans[j] == 0:
            cnt += 1
print(*ans)
