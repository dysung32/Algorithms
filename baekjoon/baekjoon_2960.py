import sys
input = sys.stdin.readline

N, K = map(int, input().split())

nums = [True] * (N + 1)

cnt = 0
for i in range(2, len(nums) + 1):
    for j in range(i, N+1, i):
        if nums[j] == True:
            nums[j] = False
            cnt += 1
            if cnt == K:
                print(j)
                break
