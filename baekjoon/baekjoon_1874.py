# 스택 수열
import sys

n = int(sys.stdin.readline())
cnt = 1
stack = []
oper = []
result = True

for i in range(n):
    num = int(sys.stdin.readline())
    while cnt <= num:
        stack.append(cnt)
        oper.append('+')
        cnt += 1
    if stack[-1] == num:
        stack.pop()
        oper.append('-')
    else:
        result = False

if result == False:
    print('NO')
else:
    for i in oper:
        print(i)
