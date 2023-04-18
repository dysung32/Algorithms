import sys
input = sys.stdin.readline

N = int(input())

problems = []
for i in range(N):
    problems.append(input().split())

problems.sort(key=lambda x:x[1])

print(problems[0][0])