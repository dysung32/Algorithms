import sys
input = sys.stdin.readline

total_sum = 0
sum = 0

def change_to_number(grade):
    if grade == 'A+':
        return 4.5
    elif grade == 'A0':
        return 4.0
    elif grade == 'B+':
        return 3.5
    elif grade == 'B0':
        return 3.0
    elif grade == 'C+':
        return 2.5
    elif grade == 'C0':
        return 2.0
    elif grade == 'D+':
        return 1.5
    elif grade == 'D0':
        return 1.0
    elif grade == 'F':
        return 0.0

for _ in range(20):
    name, cnt, grade = map(str, input().split())
    if grade != 'P':
        total_sum += float(cnt) * change_to_number(grade)
        sum += int(float(cnt))

print(f"{total_sum / sum:.6f}")
