import sys
input = sys.stdin.readline

N = int(input())

numbers = []
for _ in range(N):
    serial_num = input().rstrip()
    numbers.append(serial_num)

def sum_num(num):
    result = 0
    for n in num:
        if n.isdigit():
            result += int(n)
    return result

numbers.sort(key=lambda x:(len(x), sum_num(x), x))

for num in numbers:
    print(num)