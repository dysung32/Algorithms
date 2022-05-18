coke = int(input()) # 콜라 금액 입력
juice = int(input()) # 주스 금액 입력
water = int(input()) # 물 금액 입력

money = int(input()) # 투입 금액 입력

while money >= 0:
    beverage = input()
    if beverage == 'coke':
        if money - coke >= 0:
            money = money - coke
            print('Success')
        else:
            print('There is not enough money')
            break
    elif beverage == 'juice':
        if money - juice >= 0:
            money = money - juice
            print('Success')
        else:
            print('There is not enough money')
            break
    elif beverage == 'water':
        if money - water >= 0:
            money = money - water
            print('Success')
        else:
            print('There is not enough money')
            break


print(money)