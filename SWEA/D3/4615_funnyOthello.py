t = int(input())

for test_case in range(1, t+1):
    n,m = map(int, input().split())
    #돌을 놓을 보드 설정
    board = [[0]*n for _ in range(n)]
    #초기에 놓여진 돌 정보들 저장
    board[n//2][n//2] = 2
    board[(n//2)-1][(n//2)-1] = 2
    board[(n//2)][(n//2)-1] = 1
    board[(n//2)-1][(n//2)] = 1
    #방향벡터
    dx = [0,1,0,-1,1,1,-1,-1]
    dy = [-1,0,1,0,-1,1,1,-1]
    #m번만큼 돌을 놓는다
    for _ in range(m):
        x,y,color = map(int, input().split()) 
        board[y-1][x-1] = color #(x-1, y-1)에 돌을 둔다
        #동서남북 & 대각선 방향 확인
        for i in range(8):
            r = []
            #한번 정한 방향에 대해서는 끝까지 가봐야 함
            for j in range(1, n):
                nx = x-1 + j*dx[i]
                ny = y-1 + j*dy[i]
                #만약 다음 좌표가 범위 안에 있다면
                if 0<=nx<=n-1 and 0<=ny<=n-1:
                    #만약 다음 좌표에 아무 돌도 없다면
                    if board[ny][nx] == 0:
                        break #다음 방향 확인
                    #만약 현재 두었던 돌과 일치한다면
                    elif board[ny][nx] == color:
                        #다른 돌을 만났을때 r리스트에 저장했던 좌표를 꺼내서 
                        #현재돌과 일치하는 색상으로 바꿔준다.
                        while r:
                            a,b = r.pop()
                            board[b][a] = color
                        break #다음 방향 확인
                    #만약 현재 두었던 돌과 다르면 
                    else:
                        r.append((nx,ny)) #해당 좌표를 r 리스트에 저장한다
                else:
                    break
    bcnt, wcnt = 0, 0
    for i in board:
        bcnt += i.count(1)
        wcnt += i.count(2)

    print("#{} {} {}".format(test_case, bcnt, wcnt))


##다시풀어보기


t = int(input())
for test_case in range(1,t+1):
    n, m = map(int, input().split())

    board = [[0]*n for _ in range(n)]

    board[n//2][n//2] = 2
    board[(n//2)-1][(n//2)-1] = 2
    board[(n//2)-1][n//2] = 1
    board[n//2][(n//2)-1] = 1

    dx = [0,1,0,-1,1,1,-1,-1]
    dy = [-1,0,1,0,-1,1,1,-1]

    for _ in range(m):
        x,y,color = map(int, input().split())
        board[y-1][x-1] = color
        for i in range(8):
            r = []
            for j in range(1, n):
                nx = x + j*dx[i]
                ny = y + j*dy[i]
                if nx<0 or ny<0 or nx>=n or ny>=n:
                    break
                else:
                    if board[ny][nx] == 0:
                        break
                    elif board[ny][nx] == color:
                        while r:
                            a,b = r.pop()
                            board[b][a] = color
                        break
                    else:
                        r.append((nx,ny))

    bcnt, wcnt = 0,0
    for i in board:
        bcnt += i.count(2)
        wcnt += i.count(1)

    print(bcnt, wcnt)




