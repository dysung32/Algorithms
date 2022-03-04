from math import gcd

def solution(w, h):
    k = gcd(w, h)  # 최대 공약수 구하기

    answer = w * h - (w + h - k)

    return answer