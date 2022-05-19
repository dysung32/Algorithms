stack = []

while True:
    n = int(input())
    if n == 0: # 0이 입력되면
        break # 종료
    stack.append(n) # 리스트에 숫자 추가

idx = int(input()) # 인덱스 입력
num = int(input()) # 기준 숫자 입력

if idx < 0 or idx >= len(stack): # 인덱스가 리스트 범위를 벗어나면
    print("Not in range")

else:
    for i in range(idx + 1): # 인덱스(idx)까지의 숫자들 중에
        if stack[i] > num: # 기준 숫자(num)보다 큰 숫자를 출력
            print(stack[i])