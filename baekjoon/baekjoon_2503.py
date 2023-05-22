import itertools
import sys
input = sys.stdin.readline

N = int(input())

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
num_list = list(itertools.permutations(data, 3))

for _ in range(N):
    three_num_list, strike, ball = map(int, input().split())
    three_nums = list(map(int, str(three_num_list).strip()))
    remove_cnt = 0

    for i in range(len(num_list)):
        s = 0
        b = 0
        i -= remove_cnt
        for j in range(3):
            if three_nums[j] == num_list[i][j]:
                s += 1
            elif three_nums[j] in num_list[i]:
                b += 1

        if s != strike or b != ball:
            num_list.remove(num_list[i])
            remove_cnt += 1

print(len(num_list))
