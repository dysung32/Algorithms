import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
ans = [-1] * N

myStack = []

for i in range(N):
    while myStack and A[myStack[-1]] < A[i]: # 오큰수 조건
        ans[myStack.pop()] = A[i] # 정답 리스트에 오큰 수 저장
    myStack.append(i)

print(*ans)
