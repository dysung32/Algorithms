import sys
import math
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    S = input().rstrip()
    prime_len = math.ceil(len(S) / 3)

    S_prime = S[0:prime_len]
    S_prime_rev = S_prime[::-1]
    S_prime_tail = S_prime[1:]

    S_list = []

    S_list.append(S_prime + S_prime_rev + S_prime)
    S_list.append(S_prime + S_prime_rev[1:] + S_prime)
    S_list.append(S_prime + S_prime_rev + S_prime_tail)
    S_list.append(S_prime + S_prime_rev[1:] + S_prime_tail)

    if S in S_list:
        print(1)
    else:
        print(0)