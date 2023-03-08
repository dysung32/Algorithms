import sys
input = sys.stdin.readline

N1, N2 = map(int, input().split())
group1 = list(input().rstrip("\n"))
group2 = list(input().rstrip("\n"))
T = int(input())

group1.reverse()
order = group1 + group2 # 초기 순서

for t in range(1, T + 1):
    for i in range(N1 + N2 - 1):
        if order[i] in group1 and order[i+1] in group2:
            order[i], order[i+1] = order[i+1], order[i]
            if order[i+1] == group1[-1]:
                break

print(''.join(order))