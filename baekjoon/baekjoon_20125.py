import sys
input = sys.stdin.readline

N = int(input())

arr = []

for _ in range(N):
    arr.append(list(input().rstrip()))

head_r = 0
head_c = 0
head = False

for i in range(N):
    for j in range(N):
        if arr[i][j] == '*':
            head_r = i
            head_c = j
            head = True
            break
    if head:
        break

heart_r = head_r + 1
heart_c = head_c

# 왼쪽 팔, 오른쪽 팔, 허리, 왼쪽 다리, 오른쪽 다리
# 왼쪽 팔 길이 찾기
left_arm = 0
for c in range(heart_c):
    if arr[heart_r][c] == '*':
        left_arm += 1

# 오른 쪽 팔 길이 찾기
right_arm = 0
for c in range(heart_c + 1, N):
    if arr[heart_r][c] == '*':
        right_arm += 1

# 허리 길이 찾기
back = 0
back_end = 0
for r in range(heart_r + 1, N):
    if arr[r][heart_c] == '*':
        back_end = r
        back += 1

# 왼쪽 다리 길이 찾기
left_leg = 0
for r in range(back_end + 1, N):
    if arr[r][heart_c - 1] == '*':
        left_leg += 1

# 오른쪽 다리 길이 찾기
right_leg = 0
for r in range(back_end + 1, N):
    if arr[r][heart_c + 1] == '*':
        right_leg += 1

print(heart_r + 1, heart_c + 1)
print(left_arm, right_arm, back, left_leg, right_leg)