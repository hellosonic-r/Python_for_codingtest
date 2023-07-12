# ##내 풀이

# from itertools import permutations
# from collections import deque
# import copy

# #한 줄씩 방문하면서 스택에 값을 넣고, 다음 좌표에 값을 넣는다
# def bfs(sx,sy,ex,ey,stack,board):
#     queue = deque()
#     v = [[0 for _ in range(m)] for _ in range(n)]
#     v[sy][sx] = 1
#     stack.append(board[sy][sx])
#     queue.append((sx,sy))
#     i = 0
#     while queue:
#         x,y = queue.popleft()
#         if v[y][x] == (ex-sx) * 4:
#             return
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if nx<sx or ny<sy or nx>ex or ny>ey:
#             i = (i+1)%4
#             nx = x + dx[i]
#             ny = y + dy[i]
#             queue.append((nx,ny))
#             stack.append(board[ny][nx]) #다음 좌표 값을 스택에 넣고
#             board[ny][nx] = stack.pop(0) #이전 좌표 값을 꺼내어 업데이트한다.
#             v[ny][nx] = v[y][x] + 1
#         else:
#             if v[ny][nx] == 1:
#                 i = (i+1)%4
#                 nx = x + dx[i]
#                 ny = y + dy[i]
#                 queue.append((nx,ny))
#                 stack.append(board[ny][nx])
#                 board[ny][nx] = stack.pop(0)
#                 v[ny][nx] = v[y][x] + 1

#             elif v[ny][nx] == 0:
#                 v[ny][nx] = v[y][x] + 1
#                 queue.append((nx,ny))
#                 stack.append(board[ny][nx])
#                 board[ny][nx] = stack.pop(0)

# #회전이 가능할 때까지 회전을 수행한다.
# def rotate(a,b,e,f,cnt,board):
#     for i in range(cnt): #0,1
#         stack = []
#         temp = board[b+i+1][a+i]
#         bfs(a+i,b+i,e-i,f-i,stack,temp_arr)
#         board[b+i][a+i] = temp
#         # print()
#         # for j in range(n):
#         #     print(" ".join(map(str, board[j])))
#         # print()

# n, m, k = map(int, input().split()) #n:세로 m:가로 k:연산 개수

# board = [list(map(int, input().split())) for _ in range(n)]

# oper = []
# for _ in range(k):
#     oper.append(list(map(int, input().split())))

# oper_all = permutations(oper,len(oper)) #순열 : 가능한 회전연산 경우의 수
# # for i in oper_all:
# #     print(i)

# dx = [1,0,-1,0]
# dy = [0,1,0,-1]

# ans = 1e9
# data = 0

# for i in oper_all:
#     temp_arr = copy.deepcopy(board)
#     for r,c,s in i:
#         a = c-1-s #시작 x좌표
#         b = r-1-s #시작 y좌표
#         e = c-1+s #끝 x좌표
#         f = r-1+s #끝 y좌표
#         cnt = ((r+s) - (r-s)) // 2 
#         rotate(a,b,e,f,cnt,temp_arr)
#     for j in range(n):
#         data = sum(temp_arr[j])
#         ans = min(ans, data)

# # ans = 1e9
# # data = 0
# # for i in range(n):
# #     data = sum(board[i])
# #     ans = min(ans, data)

# print(ans)



##다른 코드
from itertools import permutations
import copy

n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
oper = [list(map(int, input().split())) for _ in range(k)]

ans = 1e9

for p in permutations(oper, k):
    copy_a = copy.deepcopy(board)
    for r, c, s in p:
        r -= 1
        c -= 1
        for n in range(s, 0, -1):
            tmp = copy_a[r-n][c+n] #끝값 저장 # 6
            copy_a[r-n][c-n+1:c+n+1] = copy_a[r-n][c-n:c+n] #[1 2 3 2 5 6] >> [1 1 2 3 2 5] #오른쪽으로 가면서
            for row in range(r-n,r+n): #[2 8 2 4 3] >> [8 2 4 3 3] #위로 올라가면서
                copy_a[row][c-n] = copy_a[row+1][c-n]
            copy_a[r+n][c-n:c+n] = copy_a[r+n][c-n+1:c+n+1] #[3 2 1 4 3] >> [2 1 4 3 3]
            for row in range(r+n, r-n, -1):
                copy_a[row][c+n] = copy_a[row-1][c+n]
            copy_a[r-n+1][c+n] = tmp #마지막 값(오른쪽 위) 처리

    for j in copy_a:
        ans = min(ans, sum(j))

print(ans)