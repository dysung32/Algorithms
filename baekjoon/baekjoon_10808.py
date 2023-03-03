# word: 알파벳 소문자로만 이루어진 단어
# word의 길이는 100을 넘지 않음
# 출력: 단어에 포함돼 있는 a,b,c,...,z의 개수를 공백으로 구분해 출력

word = input()
word_cnt = []
alpha = 'a'

for i in range(26):
    word_cnt.append(word.count(alpha))
    alpha = chr(ord(alpha) + 1)
    print(word_cnt[i], end=" ")
