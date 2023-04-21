t = int(input())
for test_case in range(1, t+1):
    board = []
    for _ in range(9):
        board.append(list(map(int, input().split())))
        
    line_check = 1        
    for i in range(9):
        garo_check = list(range(1,10))
        sero_check = list(range(1,10))
        for j in range(9):
            if board[i][j] not in garo_check:
                line_check = 0
                break
            else: 
                garo_check.remove(board[i][j])
            if board[j][i] not in sero_check:
                line_check = 0
                break
            else:
                sero_check.remove(board[j][i])           
        if line_check == 0:
            break
    
    nine_check = 1
    nine_check_list = list(range(1,10))
    for i in range(3): #0 1 2       / 0,  3,  6 
        for j in range(3): #0 1 2
            temp_nine = []
            for k in range(3):
                temp_nine += board[3*i+k][3*j:(3*j)+3]
            temp_nine.sort()
            if temp_nine == nine_check_list:
                continue
            else:
                nine_check = 0
                break
        if nine_check == 0:
            break
    
    ans = -1
    if line_check == 1 and nine_check == 1:
        ans = 1
    else:
        ans = 0
    print("#{} {}".format(test_case, ans))
            
        
##다시 풀어보기
t = int(input())
for test_case in range(1, t+1):
    board = []
    for _ in range(9):
        board.append(list(map(int, input().split())))
    
    must = list(range(1,10))
    line_check = -1
    for i in range(9):
        garo_check = []
        sero_check = []
        for j in range(9):
            garo_check.append(board[i][j]) 
            sero_check.append(board[j][i])
        garo_check.sort()
        sero_check.sort()
        if garo_check == must and sero_check == must:
            line_check = 1
        else:
            line_check = 0
            break

    box_check = -1
    for i in range(3): # 0, 1, 2 / 0, 3, 6이 되어야 함.
        for j in range(3):
            temp_list = []
            for k in range(3):
                temp_list += board[(i*3)+k][j*3:(j*3)+3]
            temp_list.sort()
            if temp_list == must:
                box_check = 1
            else:
                box_check = 0
                break
        #반드시 상위 for문에 대해 break 처리 해주어야 함
        if box_check == 0:
            break

    if line_check == 1 and box_check == 1:
        print("#{} {}".format(test_case, 1))
    else:
        print("#{} {}".format(test_case, 0))


    