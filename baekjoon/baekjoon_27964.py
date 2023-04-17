import sys
input = sys.stdin.readline

N = int(input())

cheeses = list(input().split())

kinds = []
for cheese in cheeses:
    if cheese not in kinds:
        if cheese[len(cheese) - 6:] == 'Cheese':
            kinds.append(cheese)

if len(kinds) >= 4:
    print('yummy')
else:
    print('sad')