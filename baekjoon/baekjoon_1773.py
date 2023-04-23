import sys
input = sys.stdin.readline

N, C = map(int, input().split())

cnts = [0] * (C + 1)

firework = 0
for i in range(N):
    sec = int(input())
    for j in range(sec, C + 1, sec):
        if cnts[j] == 0:
            cnts[j] = 1
            firework += 1
print(firework)