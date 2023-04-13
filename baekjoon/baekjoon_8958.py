import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    ox = input()
    n = len(ox)
    cnt = 0
    cnt_sum = 0
    for i in range(n):
        if ox[i] == 'O':
            cnt += 1
            cnt_sum += cnt
        else:
            cnt = 0
    print(cnt_sum)