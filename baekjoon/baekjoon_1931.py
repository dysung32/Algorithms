# N: 입력 받을 회의 수
# I: 각 회의를 지칭

# 회의실 개수는 1개
# 회의 시작 시각과 끝나는 시각 동일할 수 있음
# 회의 끝나는 즉시 다음 회의 시작 가능
# 회의는 한번 시작되면 중간에 중단 불가 !!

N = int(input()) # 회의 수 입력 받기
meetings = [] # 회의 리스트
cnt = 0 # 회의 최대 개수 초기값 설정

for i in range(N): # N개씩
    begin, end = map(int, input().split()) # 각 회의 시작 시각(begin), 종료 시각(end) 입력 받아서
    meetings.append((begin, end)) # meetings(회의 정보) 리스트에 append

# 종료 시각을 기준으로 오름차순으로 먼저 정렬
# 다음으로 그 안에서 시작 시각을 기준으로 오름차순 정렬
meetings = sorted(meetings, key=lambda x: (x[1], x[0]))

meeting_end = 0 # 최종 회의 종료 시각 초기값 설정

for I in meetings: # I는 각 회의를 지칭
    begin = I[0]
    end = I[1]
    # 회의 시작 시각이 최종 회의 종료 시각보다 같거나 크면
    if begin >= meeting_end:
        cnt += 1 # 회의 개수 카운트
        meeting_end = end # 최종 회의 종료 시각(meeting_end) end 로 변경

print(cnt) # 회의 최대 개수 출력
