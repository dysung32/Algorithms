import sys
input = sys.stdin.readline

n = int(input())
lens = sorted(list(map(int, input().split())))

total = sum(lens)
res = 0

for len in lens:
    res += len * (total - len)
    total -= len

print(res)