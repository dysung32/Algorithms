import sys
input = sys.stdin.readline

n = int(input())

one = 0
two = 0
three = 0
four = 0
axis = 0
for _ in range(n):
    x, y = map(int, input().split())
    if x == 0 or y == 0:
        axis += 1
    elif x > 0:
        if y > 0:
            one += 1
        elif y < 0:
            four += 1
    elif x < 0:
        if y > 0:
            two += 1
        elif y < 0:
            three += 1

print('Q1:', one)
print('Q2:', two)
print('Q3:', three)
print('Q4:', four)
print('AXIS:', axis)

