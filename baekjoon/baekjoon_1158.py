# 요세푸스
# N: 사람 수
# 순서대로 K번째 사람을 제거

import sys

N, K = map(int, sys.stdin.readline().split())
arr = [i for i in range(1, N + 1)]

answer = []
num = 0

for j in range(N):
    num += K - 1
    if num >= len(arr):
        num = num % len(arr)
    answer.append(str(arr.pop(num)))

print("<", ", ".join(answer), ">", sep='')