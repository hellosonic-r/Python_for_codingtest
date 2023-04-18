t = int(input())
for test_case in range(1, t+1):
    n, k = map(int, input().split())
    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))
    garo_visited = [[0] * n for _ in range(n)] 
    for i in range(n):
        garo_check = 1
        for j in range(n):
            if board[i][j] == 1:
                if garo_check > k:
                    garo_check = 1
                    garo_visited[i][j-1] -= 1
                    continue
                else:
                    garo_visited[i][j] = garo_check
                    garo_check += 1
            if board[i][j] == 0:
                garo_check = 1
                
    sero_visited = [[0] * n for _ in range(n)]
    for i in range(n):
        sero_check = 1
        for j in range(n):
            if board[j][i] == 1:
                if sero_check > k:
                    sero_check = 1
                    sero_visited[j-1][i] -= 1
                    continue
                else:
                    sero_visited[j][i] = sero_check
                    sero_check += 1
            if board[j][i] == 0:
                sero_check = 1
    ans = 0
    for i in range(n):
        ans += garo_visited[i].count(k)
    for i in range(n):
        ans += sero_visited[i].count(k)
    print("#{} {}".format(test_case, ans))  