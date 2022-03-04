import math

def solution(progresses, speeds):
    answer = []
    days = []

    num = len(progresses)

    for i in range(num):
        left = 100 - progresses[i]
        day = math.ceil(left / speeds[i])
        days.append(day)

    cnt = 1
    first = days[0]

    for i in range(1, num):
        if days[i] <= first:
            cnt += 1
        else:
            first = days[i]
            answer.append(cnt)
            cnt = 1
    answer.append(cnt)


    return answer

print(solution([93, 30, 55], [1, 30, 5]))