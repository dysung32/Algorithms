import sys
input = sys.stdin.readline

S = input().rstrip()
word_list = []

for i in range(len(S)):
    word_list.append(S[i:])

word_list.sort()

for word in word_list:
    print(word)