# 스택
import sys

N = int(sys.stdin.readline())
stack = []

for i in range(N):
    cmd = sys.stdin.readline().split()
    # push 가 입력 되면
    if cmd[0] == 'push':
        stack.append(cmd[1])
    # pop 이 입력 되면
    elif cmd[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    # size 가 입력 되면
    elif cmd[0] == 'size':
        print(len(stack))
    # empty 가 입력 되면
    elif cmd[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    # top 이 입력 되면
    elif cmd[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])