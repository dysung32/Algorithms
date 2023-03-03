import sys
input = sys.stdin.readline

nums = list(map(int, input().strip()))
nums.sort(reverse=True)

for i in range(len(nums)):
    print(nums[i], end='')