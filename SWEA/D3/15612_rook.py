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
    for i in range(8):
        chess.append(list(input()))
    for i in range(8): #Y측 줄
        for j in range(8): #x측 
            temp_ok = 0
            if chess[i].count("O") == 1: #Y축이 룩이 1인 것만..
                if chess[i][j] == "O": # chess[0][7]
                    for k in range(i,8):
                        if chess[k][j] == "O":
                            temp_ok += 1
                    if temp_ok == 1:
                        ok += 1
                else:
                    continue
    if ok == 8:
        print("#{} {}".format(test_case, "yes"))
        
    else:
        print("#{} {}".format(test_case, "no"))
    
                        