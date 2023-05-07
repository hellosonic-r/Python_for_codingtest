# ##맞왜틀
# n, m = map(int,input().split()) #n:세로 m:가로

# board = [list(input()) for _ in range(n)]

# min_cnt = 64

# for i in range(n-8+1): # 2 (0~1)
#     for j in range(m-8+1): # 16 (0~15) 
#         temp_board = []
#         for k in range(i,8+i):
#             temp_board.append(board[k][j:j+8])
#         cnt = 0
#         if temp_board[0][0] == "B":
#             for a in range(8):
#                 for b in range(8):
#                     if a%2 == 0:
#                         if b%2 == 0 and temp_board[a][b] == "W":
#                             cnt += 1
#                         if b%2 == 1 and temp_board[a][b] == "B":
#                             cnt += 1
#                     if a%2 == 1:
#                         if b%2 == 0 and temp_board[a][b] == "B":
#                             cnt += 1
#                         if b%2 == 1 and temp_board[a][b] == "W":
#                             cnt += 1
#         if temp_board[0][0] == "W":
#             for a in range(8):
#                 for b in range(8):
#                     if a%2 == 0:
#                         if b%2 == 0 and temp_board[a][b] == "B":
#                             cnt += 1
#                         if b%2 == 1 and temp_board[a][b] == "W":
#                             cnt += 1
#                     if a%2 == 1:
#                         if b%2 == 0 and temp_board[a][b] == "W":
#                             cnt += 1
#                         if b%2 == 1 and temp_board[a][b] == "B":
#                             cnt += 1
#         if min_cnt > cnt:
#             min_cnt = cnt
# print(min_cnt)
                    

##다시 풀어보고 정답판정 받았다.
n, m = map(int,input().split()) #n:세로 m:가로

board = [list(input()) for _ in range(n)]

min_cnt = 64

for i in range(n-8+1): #그리드를 이동하면서 체스판 분석 (세로)
    for j in range(m-8+1): #그리드를 이동하면서 체스판 분석 (가로)
        temp_board = [] #임시 체스판
        for k in range(i,8+i):
            temp_board.append(board[k][j:j+8])
        wcnt = 0 #첫번째 체스판 칸이 w일 경우
        for a in range(8):
            for b in range(8):
                #정상적으로 말이 놓여진 경우들
                if (a%2 == 0 and b%2 == 0 and temp_board[a][b] == "W") or \
                    (a%2 == 0 and b%2 == 1 and temp_board[a][b] == "B") or \
                    (a%2 == 1 and b%2 == 0 and temp_board[a][b] == "B") or\
                    (a%2 == 1 and b%2 == 1 and temp_board[a][b] == "W"):
                    continue #통과
                #그렇지 않다면, 비정상적으로 말이 놓여진 경우이고 바꿔줘야됨. -> 카운트
                else:
                    wcnt += 1
        bcnt = 0 #첫번째 체스판 칸이 b일 경우
        for a in range(8):
            for b in range(8):
                #정상적으로 말이 놓여진 경우들
                if (a%2 == 0 and b%2 == 0 and temp_board[a][b] == "B") or \
                    (a%2 == 0 and b%2 == 1 and temp_board[a][b] == "W") or \
                    (a%2 == 1 and b%2 == 0 and temp_board[a][b] == "W") or\
                    (a%2 == 1 and b%2 == 1 and temp_board[a][b] == "B"):
                    continue #통과
                #그렇지 않다면, 비정상적으로 말이 놓여진 경우이고 바꿔줘야됨. -> 카운트
                else: 
                    bcnt += 1

        #칠해야하는 체스판 칸수의 최소값을 구한다.
        if min_cnt > min(wcnt,bcnt):
            min_cnt = min(wcnt,bcnt)
print(min_cnt)


##다른코드
n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

min_cnt = 64 

for i in range(n-7):
    for j in range(n-7):
        w_cnt = 0 #w로 시작
        b_cnt = 0 #b로 시작
        for a in range(a, a+8):
            for b in range(b, b+8):
                if (a+b)%2 == 0:
                    if board[a][b] != "W": #x,y가 짝수인 좌표 값이 B일 경우 따로 비교
                        w_cnt += 1 #w로 시작할 경우 -> 추가 카운트
                    else: #x,y가 짝수인 좌표 값이 W일 경우 따로 비교
                        b_cnt += 1 #b로 시작할 경우 -> 추가 카운트
                else:
                    if board[a][b] != "W": #x,y가 홀수인 좌표 값이 B일 경우 따로 비교
                        b_cnt += 1 #b로 시작할 경우 -> 추가 카운트
                    else: #x,y가 홀수인 좌표 값이 W일 경우 따로 비교
                        w_cnt += 1 #w로 시작할 경우 -> 추가 카운트
        if min_cnt > min(w_cnt, b_cnt):
            min_cnt = min(w_cnt, b_cnt)
print(min_cnt)