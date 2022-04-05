# N: 물약의 종류
# 특정 물약 구매 -> 다른 물약 할인
# ci: i번째 물약 가격

N = int(input())

price = []
price = list(map(int, input().split()))

sale_cnt = int(input())
sale_price = [[0] * 2] * sale_cnt


for i in range(sale_cnt):
    num, sale = map(int, input().split(' '))
    price[num - 1] -= sale
    if price[num - 1] <= 0:
        price[num - 1] = 1

zero = int(input())
one = int(input())

num, sale = map(int, input().split(' '))
price[num-1] -= sale

one = int(input())
num, sale = map(int, input().split(' '))

price_sum = 0
for i in range(N):
    price_sum += price[i]

print(price_sum)
