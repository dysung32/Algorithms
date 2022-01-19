# 바둑판 준비
# 19*19 크기의 2차원 배열 선언
b = [[0]*19 for i in range(19)]

# 19*19 크기의 바둑판 채우기
for i in range(19):
    nums = input().split()
    for j in range(19):
        b[i][j] = int(nums[j])

# 십자 뒤집기 횟수(n) 입력 받기
n = int(input())

# 좌표(x, y) n번 입력 받고
# 그 좌표를 제외한 가로줄과 세로줄의 바둑알 모두 뒤집기
# 흰 돌(1), 검은 돌(0)
for i in range(n):
    x, y = map(int, input().split())
    for j in range(19):
        # x행 뒤집기
        if b[x - 1][j] == 0:
            b[x - 1][j] = 1
        else:
            b[x - 1][j] = 0
        # y열 뒤집기
        if b[j][y - 1] == 0:
            b[j][y - 1] = 1
        else:
            b[j][y - 1] = 0

# 뒤집은 바둑판 출력
for i in range(19):
    for j in range(19):
        print(b[i][j], end=' ')
    print()