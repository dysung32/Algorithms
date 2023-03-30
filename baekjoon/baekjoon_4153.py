import sys
input = sys.stdin.readline

while True:
    sides = list(map(int, input().split()))
    max_side = max(sides)
    if max_side == 0:
        break
    sum = 0
    for side in sides:
        if side != max_side:
            sum += (side * side)

    if max_side * max_side == sum:
        print("right")
    else:
        print("wrong")