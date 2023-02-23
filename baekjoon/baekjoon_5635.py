import sys

N = int(sys.stdin.readline())

list = []

for _ in range(N):
    name, day, month, year = input().split()
    list.append([name, int(day), int(month), int(year)])

list.sort(key=lambda x:(x[3], x[2], x[1]))
print(list[-1][0]) # 가장 나이 적은 사람 (year로는 가장 큼)
print(list[0][0]) # 가장 나이 많은 사람