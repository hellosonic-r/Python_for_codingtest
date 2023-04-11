###여러 번 시도 끝에 패스 / 가로 세로 구하는 법 다름.. 리스트 슬라이싱 이용 Y축에서 못함
for test_case in range(1, 11):
    length = int(input())
    board = []
    for _ in range(8):
        board.append(list(input()))
        
    garo_count = 0
    sero_count = 0
    
    for i in range(8):
        for j in range(9-length): #0,1,2,3,4 
            garo_list = board[i][j:j+length]
            garo_list_reversed = garo_list[::-1]
            sero_list = []
            for k in range(j,j+length):
                sero_list.append(board[k][i])
            sero_list_reversed = sero_list[::-1]
            if sero_list == sero_list_reversed:
                sero_count+=1
            if garo_list == garo_list_reversed:
                garo_count+=1
               
                        
    print("#{} {}".format(test_case, garo_count+sero_count))
                