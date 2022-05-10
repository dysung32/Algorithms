# 2071. 평균값 구하기

T = int(input())
for test_case in range(1, T+1):
    nums = map(int, input().split())
    sum = 0
    avg = 0
    for num in nums:
        sum += num
        avg = round(sum / 10)
    print('#' + str(test_case), avg)