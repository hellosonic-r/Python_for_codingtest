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

##다시 풀어보기
t = int(input())
for test_case in range(1, t+1):
    n, k = map(int, input().split()) #퍼즐 가로 세로 : n  단어 길이 : k
    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))
    
    garo_zip = []
    sero_zip = []

    for i in range(n):

        garo_count = 0
        sero_count = 0

        for j in range(n):
            #가로 분석
            if board[i][j] == 1: #좌표의 값이 1이면 
                garo_count += 1 #가로 카운트 1 증가
            elif board[i][j] == 0: #좌표의 값이 0이면
                garo_zip.append(garo_count) #현재까지 저장된 가로 카운트 garo_zip에 저장
                garo_count = 0 #가로 카운트 0으로 초기화

            #세로 분석
            if board[j][i] == 1: #좌표의 값이 1이면
                sero_count += 1 #세로 카운트 1 증가
            elif board[j][i] == 0: #좌표의 값이 0이면
                sero_zip.append(sero_count) #현재까지 저장된 세로 카운트 sero_zip에 저장
                sero_count = 0 #세로 카운트 0으로 초기화

        garo_zip.append(garo_count) #가로 한 줄 for문을 다 돌면 현재 가로 카운트 garo_zip에 저장
        sero_zip.append(sero_count) #세로 한 줄 for문을 다 돌면 현재 세로 카운트 seor_zip에 저장
            
    print("#{} {}".format(test_case, garo_zip.count(k) + sero_zip.count(k)))
       



