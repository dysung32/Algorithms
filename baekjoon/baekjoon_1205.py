import sys
input = sys.stdin.readline

N, new, P = map(int, input().split())
scores = []
if N > 0:
    scores = list(map(int, input().split()))

if N == P and scores[-1] >= new:
    print(-1)
else:
    rank = 1
    flag = False
    for score in scores:
        if score < new:
            flag = True
            print(rank)
            break
        elif score > new:
            rank += 1
    if not flag:
        print(rank)