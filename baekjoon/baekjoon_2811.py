import sys
input = sys.stdin.readline

N = int(input())
emotions = list(map(int, input().split()))
flowers = [False] * N

# 기분 좋은 날: 양수
# 우울한 날: 음수

# 우울 기간이 T일 때, 구간 시작으로부터 2T일 전부터 구간 시작 전날까지 꽃을 선물해야함
# 가장 긴 우울 구간의 경우는 3T일 전부터 꽃을 선물해줘야 함.
# T_f: 우울 기간
# 최장 우울 기간이 여러 개인 경우 한 구간만 3T일 전부터 주면 됨.

cnt = 0
period = 0 # 우울 기간
max_period = 0 # 최장 우울 기간
ans = 0

for i in range(N-1, -1, -1):
    if emotions[i] < 0:
        period += 1
        continue

    if max_period < period:
        max_period = period

    for j in range(i + 1 - period * 2, i + 1):
        if j < 0 or flowers[j]:
            continue
        flowers[j] = True
        cnt += 1

    period = 0

# 최장 우울 구간 1군데 찾아서 +1 처리
period = 0
tmp_cnt = 0
for i in range(N-1, -1, -1):
    if emotions[i] < 0:
        period += 1
        continue

    if period == max_period:
        for j in range(i + 1 - period * 3, i + 1):
            if j < 0 or flowers[j]:
                continue
            tmp_cnt += 1

    if ans < cnt + tmp_cnt:
        ans = cnt + tmp_cnt

    tmp_cnt = 0
    period = 0

print(ans)