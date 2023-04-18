# A번 - 초코바

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

total = 100 * N

if total >= M:
    print('Yes')
else:
    print('No')