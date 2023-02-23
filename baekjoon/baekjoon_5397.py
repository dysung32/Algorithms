# 키로거
# N: 테스트 케이스 개수
# < 왼쪽으로 한 칸 이동
# > 오른쪽으로 한 칸 이동
# - 백스페이스: 커서 바로 앞에 글자 존재한다면 지우기

import sys

N = int(sys.stdin.readline())

for i in range(N):
    str1 = []
    str2 = []
    keys = list(sys.stdin.readline().rstrip())
    for key in keys:
        if key == '<':
            if str1:
                str2.append(str1.pop())
        elif key == '>':
            if str2:
                str1.append(str2.pop())
        elif key == '-':
            if str1:
                str1.pop()
        else:
            str1.append(key)

    print(''.join(str1 + list(reversed(str2))))
