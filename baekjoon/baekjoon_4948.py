import sys
input = sys.stdin.readline

def is_prime_number(x):
    if x == 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

numbers = [n for n in range(1, 246913)]
prime_numbers = []

for num in numbers:
    if is_prime_number(num):
        prime_numbers.append(num)

while True:
    n = int(input())
    if n == 0:
        break

    cnt = 0

    for p in prime_numbers:
        if n < p and p <= 2 * n:
            cnt += 1

    print(cnt)