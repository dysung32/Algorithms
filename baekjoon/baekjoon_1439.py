import sys
input = sys.stdin.readline

S = input()

zero_cnt = 0
one_cnt = 0
pre = S[0]
for i in range(1, len(S)):
    cur = S[i]
    if cur == pre:
        continue

    if pre != cur:
        if pre == '0':
            zero_cnt += 1
        else:
            one_cnt += 1
    pre = cur

if zero_cnt == 0 or one_cnt == 0:
    print(0)
else:
    print(min(zero_cnt, one_cnt))