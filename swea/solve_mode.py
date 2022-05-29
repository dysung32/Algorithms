T = int(input())

for test_case in range(1, T + 1):
    n = int(input())

    scores = list(map(int, input().split()))

    scores_frequency = [0] * 101

    for score in scores:
        scores_frequency[score] += 1

    mode = max(scores_frequency)

    for i in range(100, -1, -1):
        if scores_frequency[i] == mode:
            print(f'#{n} {i}')
            break

