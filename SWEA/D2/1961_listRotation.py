t = int(input())
for test_case in range(1,t+1):
    n = int(input())
    board = []
    for _ in range(n):
        board.append(list(map(int ,input().split())))
    board_90 = [[] * n for _ in range(n)]
    board_180 = [[] * n for _ in range(n)]
    board_270 = [[] * n for _ in range(n)]
    
    for i in range(n-1, -1, -1):
        for j in range(n-1,-1,-1):
            board_90[i].append(board[j][i])
    
    for i in range(n):
        for j in range(n-1, -1, -1):
            board_180[n-1-i].append(board[i][j])
    
    for i in range(n-1, -1,-1):
        for j in range(n):
            board_270[i].append(board[j][n-1-i])
            
    print("#{}".format(test_case))
    for i in range(n):
        print("".join(map(str, board_90[i])),end=" ")
        print("".join(map(str, board_180[i])),end=" ")
        print("".join(map(str, board_270[i])),end="\n")
        

    