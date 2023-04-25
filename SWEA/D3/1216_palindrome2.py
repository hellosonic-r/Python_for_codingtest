# ##Pass 받긴 했는데 클린코드 노력해야할 것 같다
# for test_case in range(1, 11):
#     t = int(input())
#     board = []
#     for _ in range(100):
#         board.append(list(input()))
    
#     garo_max_length = 0
    
#     for i in range(100): #세로 줄 만큼 반복
#         for j in range(100): #가로 줄 시작점
#             for k in range(j, 100): #가로 줄 끝나는점
#                 garo_temp_list = board[i][j:k+1] #가로 줄 시작점 부터 끝나는점까지 리스트로 만든다
#                 if garo_temp_list == garo_temp_list[::-1]: #뒤집어서 일치한다면
#                     if garo_max_length < len(garo_temp_list): #회문의 길이를 저장한다.
#                         garo_max_length = len(garo_temp_list)
                        
#     for i in range(100): #가로 줄 만큼 반복
#         for j in range(100): #세로 줄 시작점
#             sero_temp_list = []
#             for k in range(j,100): #세로 줄 끝나는점
#                 sero_temp_list += board[k][i] #세로 줄 시작점 부터 끝나는점까지 리스트로 만든다.
#                 if sero_temp_list == sero_temp_list[::-1]: #뒤집어서 일치한다면
#                     if sero_max_length < len(sero_temp_list): #회문의 길이를 저장한다.
#                         sero_max_length = len(sero_temp_list)
                       
#     print("#{} {}".format(test_case, max(garo_max_length,sero_max_length)))
                

##다른 코드
#2차원 리스트 가로, 세로 변환
def rotated(a):
    n = len(a) 
    m = len(a[0]) 

    result = [[""]*n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            result[j][i] = a[i][j]

    return result

for test_case in range(1,11):
    t = int(input())

    board_garo = []
    for _ in range(5):
        board_garo.append(list(input()))

    board_sero = rotated(board_garo)


    print(board_garo)
    print(board_sero)