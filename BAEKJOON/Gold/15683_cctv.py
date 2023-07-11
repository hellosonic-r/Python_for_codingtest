# # from collections import deque
# # import copy


# # def dfs(count, )
# #     global cctv_cnt
# #     if count == cctv_cnt:
# #         return
    


# # # def check(): #사각지대 체크 함수
# # #     cnt = 0 
# # #     for y in range(n):
# # #         for x in range(m):
# # #             if temp[y][x] == 0:
# # #                 cnt += 1
# # #     return cnt
                
# # n, m = map(int, input().split()) #n:세로 m:가로
# # board = [list(map(int, input().split())) for _ in range(n)]

# # dx = [0,1,0,-1]
# # dy = [-1,0,1,0]

# # cctv = [[] for _ in range(6)]

# # cctv_cnt = 0
# # for y in range(n):
# #     for x in range(m):
# #         if board[y][x] == 1:
# #             cctv[1].append((x,y))
# #             cctv_cnt += 1
# #         elif board[y][x] == 2:
# #             cctv[2].append((x,y))
# #             cctv_cnt += 1
# #         elif board[y][x] == 3:
# #             cctv[3].append((x,y))
# #             cctv_cnt += 1
# #         elif board[y][x] == 4:
# #             cctv[4].append((x,y))
# #             cctv_cnt += 1
# #         elif board[y][x] == 5:
# #             cctv[5].append((x,y))
# #             cctv_cnt += 1

# # print(cctv)



# import copy

# def monitoring(board, direction, x, y):
#     for i in direction:
#         nx = x
#         ny = y
#         while True:
#             nx += dx[i]
#             ny += dy[i]
#             if nx<0 or ny<0 or nx>=m or ny>=n:
#                 break
#             else:
#                 if board[ny][nx] == 6:
#                     break
#                 elif board[ny][nx] == 0:
#                     board[ny][nx] = -1

# def dfs(depth, board):
#     global min_ans
#     if depth == len(cctv):
#         cnt = 0
#         for i in range(n):
#             cnt += board[i].count(0)
#         min_ans = min(min_ans, cnt)
#         return
    
#     temp = copy.deepcopy(board)
#     cctv_num, x, y = cctv[depth] #ex) cctv_num = 2
#     for i in direction[cctv_num]: # direction[cctv_num] = [[0,2], [1,3]] 
#         monitoring(temp, i, x, y)
#         dfs(depth+1, temp)
#         temp = copy.deepcopy(board)


# n, m = map(int, input().split())
# board = []
# cctv = []

# direction = [
#     [],
#     [[0],[1],[2],[3]],
#     [[0,2], [1,3]],
#     [[0,1], [1,2], [2,3], [0,3]],
#     [[0,1,2], [0,1,3], [1,2,3], [0,2,3]],
#     [[0,1,2,3]]
# ]

# dx = [0,1,0,-1]
# dy = [-1,0,1,0]

# for i in range(n):
#     data = list(map(int, input().split()))
#     board.append(data)
#     for j in range(m):
#         if data[j] in [1,2,3,4,5]:
#             cctv.append((data[j], j, i))

# min_ans = 1e9
# dfs(0, board)
# print(min_ans)

import copy

#--------------------함수 정의 부분------------------
#cctv번호에 맞게 감시 지역을 채우는 함수
def fill(board, direction, x,y):
    for i in direction: #ex) 여기서 direction은 [1,2]...이다
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]
            if nx<0 or ny<0 or nx>=m or ny>=n:
                break
            else:
                if board[ny][nx] == 6:
                    break
                elif board[ny][nx] == 0:
                    board[ny][nx] = -1

#가능한 감시 지역을 백트래킹으로 모두 파악
def dfs(depth, board):
    global min_ans
    if depth == len(cctv): #종료조건: depth가 존재한 cctv개수만큼 된다면 종료
        cnt = 0
        for i in range(n):
            cnt += board[i].count(0)
        min_ans = min(min_ans, cnt)
        return

    #cctv = [(1,0,0), (5,3,2)] 꼴로 저장되어 있음
    cctv_num, x, y = cctv[depth] #cctv정보를 하나씩 꺼낸다.
    temp = copy.deepcopy(board) #그리드 복사
    #for문을 통해 cctv번호에 따른 모든 감시 방향을 파악한다.
    for i in direction[cctv_num]: #direction[cctv]:[[0,1],[1,2],[2,3],[0,3]] i:[1,2]
        fill(temp, i, x,y) #cctv정보에 담긴 감시방향, x, y를 매개변수로 받아서 함수 실행
        dfs(depth+1, temp) #다음 cctv정보 탐색
        temp = copy.deepcopy(board) #돌아와서는 그리드 초기화
#-----------------------------------------------

n, m = map(int, input().split())
board = []

cctv = []

#cctv번호에 따른 가능한 감시 방향을 리스트에 담는다.
#idx : cctv번호
direction = [
    [],
    [[0],[1],[2],[3]],#1
    [[0,2],[1,3]],#2
    [[0,1],[1,2],[2,3],[0,3]],#3
    [[0,1,2],[0,1,3],[1,2,3],[0,2,3]],#4
    [[0,1,2,3]]#5
]

dx = [0,1,0,-1]
dy = [-1,0,1,0]

min_ans = 1e9

for i in range(n):
    data = list(map(int, input().split()))
    board.append(data)
    for j in range(m):
        if data[j] in [1,2,3,4,5]:
            #cctv 정보를 담는다
            cctv.append((data[j],j,i)) # ex) 4, x,y

dfs(0, board)
print(min_ans)