import sys
input = sys.stdin.readline

N = int(input())

word_list = []
ans_list = []

for _ in range(N):
    word_list.append(input())

for word in word_list:
    ans_list.append((''.join(sorted(word))))

print(len(set(ans_list)))