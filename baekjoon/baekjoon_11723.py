import sys
input = sys.stdin.readline

M = int(input())

S = set()
new_S = [i for i in range(1, 21)]

for _ in range(M):
    cmd = list(input().split())

    if len(cmd) == 1:
        if cmd[0] == 'all':
            S.update(new_S)
        elif cmd[0] == 'empty':
            S = set()
        continue

    num = int(cmd[1])

    if cmd[0] == 'add':
        S.add(num)
    elif cmd[0] == 'remove':
        if num in S:
            S.discard(num)
    elif cmd[0] == 'check':
        if num in S:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'toggle':
        if num in S:
            S.discard(num)
        else:
            S.add(num)