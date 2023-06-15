import sys
input = sys.stdin.readline

N = int(input())

board_row = [-1] * N
ans = 0

def possible(r):
    for i in range(r):
        if board_row[r] == board_row[i] or abs(board_row[r] - board_row[i]) == abs(r - i):
            return False
    return True

def queens(r):
    global ans
    if r == N:
        ans += 1
        return

    for c in range(N):
        board_row[r] = c
        if possible(r):
            queens(r + 1)

queens(0)
print(ans)