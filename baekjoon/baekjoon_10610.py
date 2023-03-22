import sys
input = sys.stdin.readline

nums = list(input().strip())

def calc_sum(nums):
    sum = 0
    for num in nums:
        sum += int(num)
    return sum

if '0' in nums:
    nums.sort(reverse=True)
    if calc_sum(nums) % 3 != 0:
        print(-1)
    else:
        print(''.join(nums))

else:
    print(-1)