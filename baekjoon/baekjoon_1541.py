# 양수, +, -, () 만을 사용
# 괄호를 적절히 쳐서
# 식의 값을 최소로 만들기

result = 0

# 입력받은 식을
# 마이너스를 기준으로 split 해주기
# 이걸 가장 먼저 하는 것이 중요 !!
numbers = input().split('-')

# 첫번째 원소에 + 가 있는 경우를 대비
# + 를 기준으로 split 해서 정수형으로 모두 더해주기
for i in numbers[0].split('+'):
    result += int(i)

# 뺄셈 연산 갯수를 최대로 만들기
# 두번째 원소부터는 - 뒤의 덧셈들은 모두 괄호로 묶어줘야 함
# 이렇게 해야 최솟값을 구할 수 있음
# + 를 기준으로 split 해서 정수형으로 모두 빼주기
for i in numbers[1:]:
    for j in i.split('+'):
        result -= int(j)

# 정답 출력
print(result)