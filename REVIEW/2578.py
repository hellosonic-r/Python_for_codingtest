def check():
    global bingo
    for i in range(5):
        if board[i][:5] == [0] * 5:
            bingo += 1

    for i in range(5):
        temp_cnt = 0
        for j in range(5):
            if board[j][i] == 0:
                temp_cnt += 1
        if temp_cnt == 5:
            bingo += 1

    temp_cnt1 = 0
    for i in range(5):
        for j in range(5):
            if board[i][j] == 0 and i-j == 0:
                temp_cnt1 += 1
    if temp_cnt1 == 5:
        bingo += 1

    temp_cnt2 = 0
    for i in range(5):
        for j in range(5):
            if board[i][j] == 0 and i+j == 4:
                temp_cnt2 += 1
    if temp_cnt2 == 5:
        bingo += 1


            
board = [list(map(int, input().split())) for _ in range(5)]

call = []
for i in range(5):
    call_list = list(map(int, input().split()))
    for j in call_list:
        call.append(j)

bingo = 0
cnt = 0

for num in call:
    
    for y in range(5):
        for x in range(5):
            if board[y][x] == num:
                board[y][x] = 0
                cnt += 1
            check()
            if bingo >= 3:
                break
            else:
                bingo = 0
        if bingo >= 3:
            break
    if bingo >= 3:
        break

print(cnt)