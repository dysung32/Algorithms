import sys
import math
input = sys.stdin.readline

M, N = map(int, input().split())

def is_prime_num(num):
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

for n in range(M, N + 1):
    if is_prime_num(n):
        print(n)