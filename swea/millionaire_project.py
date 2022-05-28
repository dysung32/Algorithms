T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = []
    arr = list(map(int, input().split()))

    max = arr[N - 1]
    profit = 0
    for i in range(N - 2, -1, -1):
        if arr[i] >= max:
            max = arr[i]
        else:
            profit += (max - arr[i])

    print(f'#{test_case} {profit}')