number = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0}

N = input()

for i in range(len(N)):
    if N[i] == '6' or N[i] == '9':
        number['6'] += 1
    else:
        number[N[i]] += 1

if number['6'] % 2 == 0:
    number['6'] = number['6'] // 2
else:
    number['6'] = number['6'] // 2 + 1

print(max(number.values()))