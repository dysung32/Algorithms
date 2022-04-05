# Strfry
# 문자열을 무작위로 재배열하여 새로운 문자열을 만들어냄
# N: 테스트 케이스 수

N = int(input())

for i in range(N):
    str1, str2 = input().split()
    list1 = sorted(str1)
    list2 = sorted(str2)
    if list1 == list2:
        print("Possible")
    else:
        print("Impossible")