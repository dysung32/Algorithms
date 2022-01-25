# N: 사람 수
# sum: 각 사람이 돈을 인출하는데 필요한 시간
# total_sum: 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값

N = int(input()) # 사람 수 입력 받기
total_sum = 0

# 각 사람이 돈을 인출하는데 걸린 시간 입력 받아서 times 리스트에 저장
times = list(map(int, input().split()))

times.sort() # times 배열 오름차순 정렬

for i in range(N):
    sum = 0
    for j in range(i + 1):
        sum += times[j] # 각 사람이 필요한 시간
    total_sum += sum # 필요한 시간들의 합

print(total_sum) # 결과 출력