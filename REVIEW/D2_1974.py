t = int(input())

for test_case in range(1,t+1):
    board = [list(map(int, input().split())) for _ in range(9)]

    gans = 1
    sans = 1
    bans = 1

    for i in range(9):
        if len(list(set(board[i]))) == 9:
            continue
        else:
            gans = -1
            break

    for i in range(9):
        temp_list = []
        for j in range(9):
            temp_list.append(board[j][i])
        if len(list(set(temp_list))) == 9:
            continue
        else:
            sans = -1
            break
    

    for i in (0,3,6):
        for j in (0,3,6):
            temp_list = []
            for k in range(3): #0,1,2
                temp_list += board[i+k][j:j+3]
            if len(list(set(temp_list))) == 9:
                continue
            else:
                bans = -1
        if bans == -1:
            break

    if gans == 1 and sans == 1 and bans == 1:
        result = 1
    else:
        result = 0

    print("#{} {}".format(test_case, result))
