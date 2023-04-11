import sys
input = sys.stdin.readline


N, M = map(int, input().split())
names = []
powers = []
for _ in range(N):
    name, power = input().split()
    power = int(power)
    if powers[-1] == power:
        continue
    names.append(name)
    powers.append(power)
def search(power):
    left = 0
    right = len(powers) - 1
    while left <= right:
        mid = (left + right) // 2
        if power > powers[mid]:
            left = mid + 1
        else:
            right = mid - 1
    print(names[right + 1])

for _ in range(M):
    power = int(input())
    search(power)
