from heapq import *

def solution(scoville, K):
    answer = 0 # answer 초기값
    heapify(scoville) # 오름차순 정렬

    while True:
        min1 = heappop(scoville) # 리스트의 가장 작은 값을 return 하며 삭제 (가장 작은 값)
        # 모든 음식의 스코빌 지수가 K 이상이면 break
        if min1 >= K:
            break
        # 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우 -1 리턴
        if len(scoville) == 0:
            return -1
        min2 = heappop(scoville) # 리스트의 가장 작은 값을 return 하며 삭제 (두번째로 작은 값)
        heappush(scoville, min1 + min2 * 2) # 값 삽입 및 자동 오름차순 정렬
        answer += 1 # 섞은 횟수 +1

    return answer