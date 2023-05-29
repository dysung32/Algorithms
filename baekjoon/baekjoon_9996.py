import sys
input = sys.stdin.readline

N = int(input())
front, back = map(str, input().split('*'))

for _ in range(N):
    name = input()

    if len(name) < len(front) + len(back):
        print('NE')
        continue

    if name[0:len(front)] != front:
        print('NE')
        continue

    if name[len(name) - len(back):] != back:
        print('NE')
        continue

    print('DA')