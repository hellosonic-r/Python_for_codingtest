#내 풀이
t = int(input())
for test_case in range(1, t+1):
    n, m = map(int, input().split()) #n:세로 m:가로
    board = [list(input()) for _ in range(n)]
    b_cnt = 0 #첫 번째 칸이 "#" 일 때
    w_cnt = 0 #첫 번째 칸이 "." 일 때
    #먼저 첫 번째 칸이 "#" 일 때,
    for i in range(n):
        for j in range(m):
            if (i+j)%2 == 0: #짝수 인덱스 칸
                if board[i][j] == "#":
                    continue
                elif board[i][j] == ".": #"."이 온다면 잘못된 것임.
                    b_cnt = -1 #-1 저장
                    break 
            else: #홀수 인덱스 칸
                if board[i][j] == ".":
                    continue
                elif board[i][j] == "#":
                    b_cnt = -1
                    break
        if b_cnt == -1:
            break
    
    #첫 번째 칸이 "#"이 아닐수도 있으니 "."일때도 살펴보자
    for i in range(n):
        for j in range(m):
            if (i+j)%2 == 0: #짝수 인덱스 칸
                if board[i][j] == ".":
                    continue
                elif board[i][j] == "#": #"#"이 온다면 잘못된 것임.
                    w_cnt = -1 
                    break
            else: #홀수 인덱스 칸
                if board[i][j] == "#":
                    continue
                elif board[i][j] == ".":
                    w_cnt = -1
                    break
        if w_cnt == -1:
            break
    if w_cnt == -1 and b_cnt == -1: #만약 두 경우 다 -1 이라면
        print("#{} {}".format(test_case, "impossible"))
    else:
        print("#{} {}".format(test_case, "possible"))
                   

                    
#for문을 한번만 쓸 수는 없을까
