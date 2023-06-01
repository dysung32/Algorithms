import sys
input = sys.stdin.readline

n = int(input())

stack = []
ans = []
cnt = 1
flag = True
for _ in range(n):
    num = int(input())

    while cnt <= num:
        stack.append(cnt)
        ans.append('+')
        cnt += 1

    if stack[-1] == num:
        stack.pop()
        ans.append('-')

    else:
        flag = False

if flag:
    for a in ans:
        print(a)
else:
    print('NO')