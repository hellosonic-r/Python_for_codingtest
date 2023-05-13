def check_garo():
    global garo_max
    for y in range(n):
        garo_cnt = 1
        for x in range(n-1):
            if board[y][x] == board[y][x+1]:
                garo_cnt += 1
                if garo_cnt > garo_max:
                    garo_max = garo_cnt
            else:
                garo_cnt = 1

def check_sero():
    global sero_max
    for x in range(n):
        sero_cnt = 1
        for y in range(n-1):
            if board[y][x] == board[y+1][x]:
                sero_cnt += 1
                if sero_cnt > sero_max:
                    sero_max = sero_cnt
            else:
                sero_cnt = 1

n = int(input())
board = [list(input()) for _ in range(n)]

ans = 1

#가로 체인지
for i in range(n):
    for j in range(n-1):
        if board[i][j] != board[i][j+1]:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            garo_max = 1
            sero_max = 1
            check_garo()
            if ans < garo_max:
                ans = garo_max 
            check_sero()
            if ans < sero_max:
                ans = sero_max
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]

#세로 체인지
for i in range(n):
    for j in range(n-1):
        if board[j][i] != board[j+1][i]:
            board[j][i], board[j+1][i] = board[j+1][i], board[j][i]
            garo_max = 1
            sero_max = 1
            check_garo()
            if ans < garo_max:
                ans = garo_max 
            check_sero()
            if ans < sero_max:
                ans = sero_max
            board[j][i], board[j+1][i] = board[j+1][i], board[j][i]

print(ans)
