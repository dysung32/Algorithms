import sys
input = sys.stdin.readline

D = 0
while True:
    word = input().strip()
    if word == '*':
        break
    bool = True
    if len(word) > 1:
        D = len(word) - 2

    for i in range(D):
        word_list = []
        for j in range(len(word) - i - 1):
            word_list.append(''.join([word[j], word[j + i + 1]]))
        if len(word_list) != len(set(word_list)):
            bool = False
            break

    if bool:
        print(word + ' is surprising.')
    else:
        print(word + ' is NOT surprising.')