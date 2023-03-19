# garo_ok = 0
# sero_ok = 0
# sero = 0
# def check():
#     global garo_ok, sero_ok, sero
#     #가로 체크 
#     garo_ok = 0
#     for i in range(8):
#         if chess[i].count("O") == 1:
#             garo_ok += 1
#         else:
#             continue
#     #세로 체크
#     for i in range(8):
#         sero = 0
#         for j in range(8):
#             if chess[j][i] == "O":
#                 sero += 1
#         if sero == 1:
#             sero_ok += 1
#     if garo_ok == 8 and sero_ok == 8:
#         return True
#     else:
#         return False

# t = int(input())

# for test_case in range(1, t+1):
#     chess = []
#     rook = 0
#     for i in range(8):
#         chess.append(list(input()))
#     for i in range(8):
#         rook += chess[i].count("O")
#     if rook == 8 and check() == True:
#         print("#{} {}".format(test_case, "yes"))
#     else:
#         print("#{} {}".format(test_case, "no"))
        

t = int(input())

for test_case in range(1, t+1):
    chess = []
    ok = 0
    temp_ok = 0
    #입력받은 체스판 채우기
    for i in range(8):
        chess.append(list(input()))
    #체스판 좌표 하나하나 살펴보기   
    #y축 중 x좌표에 해당하는 체스판 정보를 확인
    for i in range(8): #Y측 
        for j in range(8): #x측 
        	#임시 값, 현재 위치의 y좌표값을 변동 시키면서 확인하기 위함.
            temp_ok = 0
			#특정 열에 놓인 룩의 개수가 한 개일 때만
            if chess[i].count("O") == 1: 
            	#특정 열/ 행(가로,세로) 좌표에 해당하는 룩이 있는 칸에서
                if chess[i][j] == "O": 
                	#현재 칸 포함, 8열까지 사렾본다.
                    for k in range(i,8):
                    	#만약 룩이 또 있다면
                        if chess[k][j] == "O":
                        	#사전에 초기화해둔 임시 값을 1씩 증가시킨다.
                            temp_ok += 1
                    #임시 값이 1이라면(현재 칸 빼고는 룩이 놓여져있지 않다면)
                    if temp_ok == 1:
                    	#ok에 1씩 증가시킨다.
                        ok += 1
                else:
                    continue
    if ok == 8:
        print("#{} {}".format(test_case, "yes"))
        
    else:
        print("#{} {}".format(test_case, "no"))
