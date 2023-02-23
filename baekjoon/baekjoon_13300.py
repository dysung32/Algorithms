# 1학년 ~ 6학년
# 남학생끼리 여학생끼리
# 같은 방엔 같은 학년
# 여학생 0 남학생 1
# N: 학생 수
# K: 한 방 최대 인원 수
# S: 성별
# Y: 학년
# students 배열 첫째줄: 남, 둘째줄: 여
import math

N, K = map(int, input().split())
students = [[0] * 6 for _ in range(2)]


for i in range(N):
    S, Y = map(int, input().split())
    if S == 0:
        if Y == 1:
            students[0][0] += 1
        elif Y == 2:
            students[0][1] += 1
        elif Y == 3:
            students[0][2] += 1
        elif Y == 4:
            students[0][3] += 1
        elif Y == 5:
            students[0][4] += 1
        elif Y == 6:
            students[0][5] += 1

    elif S == 1:
        if Y == 1:
            students[1][0] += 1
        elif Y == 2:
            students[1][1] += 1
        elif Y == 3:
            students[1][2] += 1
        elif Y == 4:
            students[1][3] += 1
        elif Y == 5:
            students[1][4] += 1
        elif Y == 6:
            students[1][5] += 1
cnt = 0
for i in range(2):
    for j in range(6):
        cnt += math.ceil(students[i][j] / K)

print(cnt)


# print(students)
