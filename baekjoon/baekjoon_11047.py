# N: 동전 종류 수
# K: 동전 가치 합(총 금액)
# sum: 필요한 동전 개수(결과값)

sum = 0
coins = []

# N, K 입력 받기
N, K = map(int, input().split())

# 동전 종류 N개 만큼 입력 받기
for i in range(N):
    coin = int(input())
    coins.append(coin)

# 입력 받은 동전 종류 내림차순으로 뒤집기
coins = sorted(coins, reverse=True)

for i in coins:
    if K / i >= 1: # 총 금액을 현재 동전으로 나누었을 때 1 이상이면
        sum += int(K / i) # 동전 개수 카운트
        K = K % i # K를 나머지 금액으로 바꿔주기

# 필요한 동전 개수의 최솟값 출력
print(sum)

