import sys

n = int(input())
numbers = list(map(int, input().split()))
x = int(input())
cnt = 0

numbers.sort()
left = 0
right = n - 1

while left < right:
    num = numbers[left] + numbers[right]
    if num == x:
        cnt += 1
    if num < x:
        left += 1
        continue
    right -= 1

print(cnt)