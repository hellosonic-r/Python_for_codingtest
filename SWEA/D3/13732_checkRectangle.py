# ##Pass code
# def check_rec(board):
#     start_y,start_x = -1, -1
#     ans = 0
#     total_cnt = 0
#     #추가한 부분 "#"의 개수를 체크함으로써 하나의 정사각형이 완성되는지 확인한다.
#     for y in range(n):
#         total_cnt += board[y].count("#")
#     for y in range(n):
#         for x in range(n):
#             if board[y][x] == "#":
#                 start_y = y
#                 start_x = x
#                 break
#         if start_y != -1 and start_x != -1:
#             break
#     a = board[start_y].count("#")
#     for y in range(start_y, start_y+a):
#         if board[y].count("#") != a:
#             ans = -1
#             break
#     cnt = 0
#     for x in range(start_x, start_x+a):
#         cnt = 0
#         for y in range(n):
#             if board[y][x] == "#":
#                 cnt += 1
#         if cnt != a:
#             ans = -1
#             break
#     #추가한 부분 
#     if ans == 0 and a*a == total_cnt:
#         return True
#     else:
#         return False

# t = int(input())

# for test_case in range(1, t+1):
#     n = int(input())
#     board = []
#     for _ in range(n):
#         board.append(list(input()))
#     if check_rec(board) == True:
#         print("#{} {}".format(test_case, "yes"))
#     else:
#         print("#{} {}".format(test_case, "no"))
    


# ##TC 20 중에 15개 Pass
# def check_rec(board):
#     global ans, garo_cnt, sero_cnt
#     start_x,start_y = -1,-1
#     #첫 번째로 "#"이 등장할 때의 x,y 좌표를 구한다
#     for y in range(n):
#         for x in range(n):
#             if board[y][x] == "#":
#                 start_y = y
#                 start_x = x
#                 break
#         if start_x != -1 and start_y != -1:
#             break
#     #첫 번째로 "#"이 등장한 y축의 "#"개수를 저장한다.            
#     a = board[start_y].count("#")
#     sero_cnt = 0
#     #y축의 "#"개수 만큼 반복을 수행한다.
#     for y in range(start_y,start_y+a):
#         garo_cnt = 0
#         for x in range(start_x,n):
#             #범위 내에서 "#"이 등장할 때 마다 garo_cnt의 값을 1씩 증가시킨다.
#             if board[y][x] == "#":
#                 garo_cnt += 1
#             else:
#                 break
#         sero_cnt += 1
#         #y축의 "#"의 개수가 garo_cnt의 값과 다르다면, "#"은 붙어있지 않고 떨어져 있다.
#         #따라서 정사각형이 될 수 없다.
#         if board[y].count("#") != garo_cnt:
#             ans = -1
#             break
#     if sero_cnt == garo_cnt and ans == 0:
#         ans = 1
#     else:
#         ans = -1
        
# t = int(input())

# for test_case in range(1, t+1):
#     n = int(input())
#     board = []
#     ans = 0
#     garo_cnt = 0
#     sero_cnt = 0
#     for _ in range(n):
#         board.append(list(input()))
#     check_rec(board)
#     if ans == 1:
#         print("#{} {}".format(test_case, "yes"))
#     else:
#         print("#{} {}".format(test_case, "no"))



# ## TC 20개 중에 16개 Pass
# def check_rec(board):
#     start_y,start_x = -1, -1
#     ans = 0
#     #첫 번째로 "#"이 등장할 때의 x,y 좌표를 구한다.
#     for y in range(n):
#         for x in range(n):
#             if board[y][x] == "#":
#                 start_y = y
#                 start_x = x
#                 break
#         if start_y != -1 and start_x != -1:
#             break
#     ##y축을 살펴본다.    
#     #첫 번째로 "#"이 등장한 y축의 "#" 개수를 저장한다.
#     a = board[start_y].count("#")
#     #첫 번째로 "#"이 등장한 y축부터, "#"의 개수만큼 반복을 수행하는데
#     for y in range(start_y, start_y+a):
#         #이 때, y축에 해당하는 "#"의 개수가 서로 다르다면
#         if board[y].count("#") != a:
#             #ans에 -1을 저장하고
#             ans = -1
#             #반복문을 그 즉시 탈출한다.
#             break

#     ##x축을 살펴본다.
#     cnt = 0
#     #첫 번째로 "#"이 등장한 x축의 "#"의 개수만큼 반복을 수행하는데
#     for x in range(start_x, start_x+a):
#         cnt = 0
#         #x축은 가만히 있고 y축을 변동시키며 x축에 "#"가 몇 개 있는지 센다.
#         for y in range(n):
#             if board[y][x] == "#":
#                 cnt += 1
#         #만약 저장된 "#"의 개수와 다르다면
#         if cnt != a:
#             #ans에 -1을 저장하고 반복문을 그 즉시 탈출한다
#             ans = -1
#             break
#     #모든 반복을 수행하고 나서 ans가 -1이 아니라면 참이다.    
#     if ans == 0:
#         return True
#     else:
#         return False

# t = int(input())

# for test_case in range(1, t+1):
#     n = int(input())
#     board = []
#     for _ in range(n):
#         board.append(list(input()))
#     if check_rec(board) == True:
#         print("#{} {}".format(test_case, "yes"))
#     else:
#         print("#{} {}".format(test_case, "no"))


##다른 사람 코드(BFS)
from collections import deque

def bfs(square, board):
    len_sq = len(square) ** 0.5
    #정사각형이 이루어질 수 있는 개수가 아니다
    if len_sq % 1 != 0:
        return "no"
    x,y = square.popleft()
    for i in range(y, y+int(len_sq)):
        for j in range(x, x+int(len_sq)):
            if board[i][j] != "#":
                return "no"
    return "yes"
            

t = int(input())
for test_case in range(1, t+1):
    board = []
    n = int(input())
    for _ in range(n):
        board.append(list(input()))
    square = deque((x,y) for y in range(n) for x in range(n) if board[y][x] == "#")
    answer = bfs(square, board)
    
    print("#{} {}".format(test_case, answer))
    
    
        
                
              