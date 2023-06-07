import sys
input = sys.stdin.readline

cnts = [0] * 10001

N = int(input())

for _ in range(N):
    num = int(input())
    cnts[num] += 1

for i in range(10001):
    if cnts[i] != 0:
        for j in range(cnts[i]):
            print(i)