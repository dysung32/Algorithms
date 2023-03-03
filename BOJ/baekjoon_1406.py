# 에디터
# 소문자만 기록할 수 있는 편집기
# 커서는 문장의 맨 앞, 문장의 맨 뒤, 또는 문장의 중간 아무데나 위치 가능
# 길이가 N인 문자열 -> 커서가 위치할 수 있는 곳은 N+1가지 경우

# 편집기 지원 명령어
# L: 커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시됨)
# D: 커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤이면 무시됨)
# B: 커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨). 삭제로 인해 커서는 한 칸 왼쪽으로 이동한 것처럼 나타나지만, 실제로 커서의 오른쪽에 있던 문자는 그대로임
# P $: $라는 문자를 커서 왼쪽에 추가함

import sys

str1 = list(sys.stdin.readline().rstrip())
str2 = []

M = int(sys.stdin.readline()) # 입력할 명령줄 개수

for i in range(M):
    command = sys.stdin.readline().split()
    if command[0] == 'L' and str1:
        str2.append(str1.pop())
    elif command[0] == 'D' and str2:
        str1.append(str2.pop())
    elif command[0] == 'B' and str1:
        str1.pop()
    elif command[0] == 'P':
        str1.append(command[1])

print(''.join(str1 + list(reversed(str2))))
        