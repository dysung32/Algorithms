# 미로 : m
m = [[0] * 10 for i in range(10)]

# 10*10 크기의 미로 채우기
for i in range(10):
    nums = input().split()
    for j in range(10):
        m[i][j] = int(nums[j])

# 개미 움직이기
# 개미집 위치(2, 2)에서 출발
a = 1
b = 1

# 0(갈 수 있는 곳), 1(벽 또는 장애물)
# 먹이가 2
while True:
    # 갈 수 있는 곳이라면 경로 표시
    if m[a][b] == 0:
        m[a][b] = 9
    # 먹이가 있는 곳이라면 경로 표시하고 이동 멈추기
    elif m[a][b] == 2:
        m[a][b] = 9
        break
    # 더 이상 움직일 수 없는 경우 이동 멈추기
    if (m[a][b + 1] == 1 and m[a + 1][b] == 1) or (a == 9 and b == 9):
        break
    # 오른쪽에 길이 나타나면 오른쪽으로 움직인다
    if m[a][b + 1] != 1:
        b += 1
    # 아래쪽에 길이 나타나면 아래쪽으로 움직인다
    elif m[a + 1][b] != 1:
        a += 1

# 성실한 개미가 이동한 경로를 출력
for i in range(10):
    for j in range(10):
        print(m[i][j], end=' ')
    print()
