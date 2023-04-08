import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [0] * n
for i in range(n):
    coins[i] = int(input())

dp = [0 for i in range(k+1)]

dp[0] = 1

for coin in coins:
    for i in range(coin, k+1):
        if i - coin >= 0:
            dp[i] += dp[i-coin]

print(dp[k])