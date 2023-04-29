import sys
input = sys.stdin.readline

N = int(input())

for i in range(N, 0, -1):
    stars = ''
    for j in range(i):
        stars += '*'
    print(stars)