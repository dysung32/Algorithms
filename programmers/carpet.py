def solution(brown, yellow):
    total = brown + yellow
    answer = [0] * 2
    num = 3
    while True:
        if total % num == 0:
            if (num - 2) * (total // num - 2) == yellow:
                answer[0] = num
                answer[1] = total // num
                if answer[0] >= answer[1]:
                    break
        num += 1

    return answer