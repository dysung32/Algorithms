import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    scores = [[] * 2 for _ in range(N)]
    for i in range(N):
        scores[i] = list(map(int, input().split()))

    scores.sort()

    cnt = 1
    min = scores[0][1]

    for i in range(1, N):
        if scores[i][1] < min:
            min = scores[i][1]
            cnt += 1
    print(cnt)

