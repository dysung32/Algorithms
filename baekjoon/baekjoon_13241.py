import math
import sys
input = sys.stdin.readline

A, B = map(int, input().split())
n = math.gcd(A, B)
print(A * B // n)
