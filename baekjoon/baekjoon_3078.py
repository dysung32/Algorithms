import sys
from collections import deque
input = sys.stdin.readline

# 등수의 차이가 K보다 작거나 같으면서 이름의 길이가 같은 친구 == 좋은 친구

N, K = map(int, input().split())

# 성적 순으로 입력받은 학생 이름 길이 배열
students = deque()
# 이름 길이 cnt 배열 2 ~ 20글자
lengths = [0] * 21
cnt = 0

for i in range(N):
    name_length = len(input().rstrip())
    students.append(name_length)
    lengths[name_length] += 1
    if len(students) > 0:
        if len(students) >= K + 2:
            popped_name_len = students.popleft()
            lengths[popped_name_len] -= 1
        cnt += (lengths[name_length] - 1)

print(cnt)