# 2072. 홀수만 더하기

t = int(input())

for test_case in range(1, t+1):
    nums = map(int, input().split())
    sum = 0
    for num in nums:
        if num % 2 == 1:
            sum += num
    print('#' + str(test_case), str(sum))