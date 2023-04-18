# B번 - 사격 내기

import sys
input = sys.stdin.readline

A, B = map(int, input().split())

# 점수 배열 선언
scores = [2**i for i in range(0, 10)]

answer_list = []

def combi(n, ans, total):
    if sum(ans) > total:
        return
    if n == len(scores):
        temp = [i for i in ans]
        if sum(temp) == total:
            answer_list.append(temp)
        return
    ans.append(scores[n])
    combi(n + 1, ans, total)
    ans.pop()
    combi(n + 1, ans, total)

combi(0, [], A)
A_list = answer_list[0]
answer_list = []
combi(0, [], B)
B_list = answer_list[0]

C_list = []
for a in A_list:
    if a in B_list:
        continue
    else:
        C_list.append(a)

for b in B_list:
    if b in A_list:
        continue
    else:
        C_list.append(b)

print(sum(C_list))