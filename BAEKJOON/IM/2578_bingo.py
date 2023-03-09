board = [] #빙고판
call_temp = [] #사회자가 부른 번호(임시)
for _ in range(5):
    board.append(list(map(int, input().split())))
for _ in range(5):
    call_temp.append(list(map(int, input().split())))

call = [] 

#사회자가 부른 번호 2차원 리스트를 1차원 리스트로 변환
for i in range(5):
    for j in range(5):
        call.append(call_temp[i][j])

#빙고판이 몇줄 지워졌는지 체크하는 메서드 작성
def bingo(board):
    global cnt
    cnt = 0 #메서드가 수행될때마다 카운트 값을 반드시 초기화
    for i in range(5):
        if board[i][0] == board[i][1] == board[i][2] == board[i][3] \
            == board[i][4] == 0:
            cnt += 1
        else:
            continue
    for j in range(5):
        if board[0][j] == board[1][j] == board[2][j] == board[3][j] \
            == board[4][j] == 0:
            cnt += 1
        else:
            continue
    if board[0][0] == board[1][1] == board[2][2] == board[3][3] \
        == board[4][4] == 0:
        cnt += 1
    if board[4][0] == board[3][1] == board[2][2] == board[1][3] \
        == board[0][4] == 0:
        cnt += 1   

#사회자가 부른 번호를 지우는 for문 작성
for k in range(len(call)-1):
    for i in range(5):
        for j in range(5):
            if board[i][j] == call[k]:
                board[i][j] = 0
    bingo(board) #사회자가 번호를 부를 때마다 몇 줄이 지워졌는지 카운트하는 메서드 동작
    if cnt >= 3: 
        print(k+1)
        break

# import sys

# c = [list(map(int, input().split())) for _ in range(5)]
# mc = []

# for _ in range(5):
#     mc += list(map(int, input().split()))

# print(mc)

# def check():
#     #가로 확인
#     for x in c:
#         if x.count(0) == 5:
#             bingo += 1

#     #세로 확인
#     for i in range(5):
#         y = 0
#         for j in range(5):
#             if c[j][i] == 0:
#                 y += 1
#         if y == 5:
#             bingo += 1

#     #왼쪽 위부터 시작하는 대각선 확인
#     d1 = 0
#     for i in range(5):
#         if c[i][i] == 0:
#             d1 += 1
#     if d1 == 5:
#         bingo += 1

#     #오른쪽 위부터 시작하는 대각선 확인
#     d2 = 0
#     for i in range(5):
#         if c[i][4-i] == 0:
#             d2 += 1
#     if d2 == 5:
#         bingo += 1
    
#     return bingo #지워진 줄이 몇 줄인지 체크하고 리턴한다.

# cnt = 0 
# for i in range(25):
#     for x in range(5):
#         for y in range(5):
#             if mc[i] == c[x][y]:
#                 c[x][y] = 0
#                 cnt += 1
#     if cnt >= 12:
#         result = check()
        
#         if result >= 3:
#             print(i + 1)
#             break
