t = int(input())

for test_case in range(1,t+1):
    board = [list(input()) for _ in range(8)]

    dx = [0,1,0,-1]
    dy = [-1,0,1,0]

    cnt = 0
    ans = 1

    for y in range(8):
        for x in range(8):
            if board[y][x] == "O": #룩이 있는 자리 일 때
                cnt += 1 #룩이 개수를 카운트한다.
                for i in range(4): #동서남북 네 방향에 대하여
                    for j in range(1,8): #체스판 끝까지 이동해본다
                        nx = x + j*dx[i]
                        ny = y + j*dy[i]
                        if nx<0 or ny<0 or nx>=8 or ny>=8: #범위를 벗어나면 다음 방향 확인 
                            break
                        if 0<=nx<8 and 0<=ny<8: #범위 안에 있을 때 
                            if board[ny][nx] == "O": #룩이 또 있으면  
                                ans = 0 #ans = 0 표시하고 
                                break #반복문 탈출  
                    if ans == 0:
                        break
            if ans == 0:
                break
        if ans == 0:
            break

    if ans == 1 and cnt == 8: #룩의 개수가 딱 8개이고, ans = 0 이 아니면 yes 
        print("#{} {}".format(test_case, "yes"))
    else:
        print("#{} {}".format(test_case, "no"))
