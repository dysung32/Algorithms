import math

n, m = map(int, input().split())
bunja = math.factorial(n)
bunmo = math.factorial(n - m) * math.factorial(m)

print(bunja // bunmo)