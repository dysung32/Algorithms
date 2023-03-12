import sys
input = sys.stdin.readline

N = int(input())
votes = list(map(int, input().split()))
approved = 0 # 찬성
rejected = 0 # 반대
failed = 0 # 기권

for i in range(N):
    if votes[i] == 1:
        approved += 1
    elif votes[i] == -1:
        rejected += 1
    else:
        failed += 1

# 기권 >= N/2 -> 무효
if failed >= N/2:
    print("INVALID")
    sys.exit()
# 찬성 > 반대 -> 투표 통과
if approved > rejected:
    print("APPROVED")
# 반대 > 찬성 or 반대 == 찬성 -> 투표 통과 X
if rejected >= approved:
    print("REJECTED")
