# 원 안의 숫자: 리터당 가격
# 도로 위 숫자: 도로 길이
# 1km 당 1L 사용

# N: 도시의 개수

N = int(input())

dist = list(map(int, input().split())) # 각 도로 거리 (N-1 개)
oil = list(map(int, input().split())) # 각 도시의 리터당 주유 가격(원)

# 최소 비용 초기값: 제일 왼쪽 도시에서 그 다음 도시로만 가는데 드는 주유 가격
cost = dist[0] * oil[0]

# 지나온 도시들 중 제일 싼 주유 가격 변수 초기값: 제일 왼쪽 도시 주유 가격
min_oil = oil[0]

# 두번째 도시부터 마지막 도시까지 가는 동안
# min_oil 보다 싼 주유 가격이 나온다면
# 그 가격으로 비용 추가 and min_oil 값 갱신
for i in range(1, N - 1):
    if oil[i] < min_oil:
        cost += dist[i] * oil[i]
        min_oil = oil[i]
    else:
        cost += dist[i] * min_oil

# 최소 비용 출력
print(cost)