# 애너그램 만들기
# 순서를 바꾸면 같은 단어가 되는 관계: 애너그램
# 두 개의 영단어
# 애너그램 관계가 되도록 제거해야 하는 최소 개수의 문자 수

word1 = list(input())
word2 = list(input())

cnt = 0

for alpha in range(ord('a'), ord('z') + 1):
    cnt += abs(word1.count(chr(alpha)) - word2.count(chr(alpha)))

print(cnt)
