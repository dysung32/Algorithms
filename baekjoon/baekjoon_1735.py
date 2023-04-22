import math
import sys
input = sys.stdin.readline

n1, m1 = map(int, input().split())
n2, m2 = map(int, input().split())

bunja = n1 * m2 + n2 * m1
bunmo = m1 * m2

yaksu = math.gcd(bunja, bunmo)

print(bunja // yaksu, bunmo // yaksu)