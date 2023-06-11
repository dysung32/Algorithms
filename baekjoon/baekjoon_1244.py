import sys
input = sys.stdin.readline

N = int(input())

switch = [-1] + list(map(int, input().split()))

student_num = int(input())

def change(n):
    if switch[n] == 0:
        switch[n] = 1
    else:
        switch[n] = 0
    return

for _ in range(student_num):
    gender, num = map(int, input().split())

    if gender == 1:
        for i in range(num, N + 1, num):
            change(i)
    elif gender == 2:
        change(num)

        for i in range(N // 2):
            if num + i > N or num - i < 1:
                break

            if switch[num - i] == switch[num + i]:
                change(num - i)
                change(num + i)
            else:
                break

for s in range(1, N + 1):
    print(switch[s], end=' ')
    if s % 20 == 0:
        print()