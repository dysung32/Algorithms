import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    foods = sum(list(map(int, input().split())))

    day = 1

    while N >= foods:
        day += 1
        foods *= 4
    print(day)