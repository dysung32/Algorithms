N = int(input())
S = []
cnt = 0

S = list(input())

for i in range(N):
    if S[i] == 'W':
        for j in range(i, N):
            if S[j] == 'H':
                for k in range(j, N):
                    if S[k] == 'E':
                        for l in range(k, N):
                            if S[l] == 'E':
                                cnt += 1

print(int(cnt / 2))