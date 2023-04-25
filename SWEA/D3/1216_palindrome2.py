##Pass 받긴 했는데 더 좋게 코드 짜야할 것 같다
for test_case in range(1, 11):
    t = int(input())
    board = []
    for _ in range(100):
        board.append(list(input()))
    
    garo_max_length = 0
    for i in range(100):
        for j in range(100): # 2
            for k in range(j, 100): #2
                garo_temp_list = board[i][j:k+1]
                if garo_temp_list == garo_temp_list[::-1]:
                    if garo_max_length < len(garo_temp_list):
                        garo_max_length = len(garo_temp_list)
                        
    for i in range(100):                   
        for j in range(100):
            sero_temp_list = []
            for k in range(j,100):
                sero_temp_list += board[k][i]
                if sero_max_length < len(sero_temp_list):
                    sero_max_length = len(sero_temp_list)
                       
    print(max(garo_max_length,sero_max_length))
                