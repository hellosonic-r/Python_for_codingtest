from itertools import permutations
from collections import deque
import copy

def bfs(sx,sy,ex,ey,stack,board):
    queue = deque()
    v = [[0 for _ in range(m)] for _ in range(n)]
    v[sy][sx] = 1
    stack.append(board[sy][sx])
    queue.append((sx,sy))
    i = 0
    while queue:
        x,y = queue.popleft()
        if v[y][x] == (ex-sx) * 4:
            return
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<sx or ny<sy or nx>ex or ny>ey:
            i = (i+1)%4
            nx = x + dx[i]
            ny = y + dy[i]
            queue.append((nx,ny))
            stack.append(board[ny][nx])
            board[ny][nx] = stack.pop(0)
            v[ny][nx] = v[y][x] + 1
        else:
            if v[ny][nx] == 1:
                i = (i+1)%4
                nx = x + dx[i]
                ny = y + dy[i]
                queue.append((nx,ny))
                stack.append(board[ny][nx])
                board[ny][nx] = stack.pop(0)
                v[ny][nx] = v[y][x] + 1

            elif v[ny][nx] == 0:
                v[ny][nx] = v[y][x] + 1
                queue.append((nx,ny))
                stack.append(board[ny][nx])
                board[ny][nx] = stack.pop(0)

def rotate(a,b,e,f,cnt,board):
    for i in range(cnt): #0,1
        stack = []
        temp = board[b+i+1][a+i]
        bfs(a+i,b+i,e-i,f-i,stack,temp_arr)
        board[b+i][a+i] = temp
        # print()
        # for j in range(n):
        #     print(" ".join(map(str, board[j])))
        # print()

n, m, k = map(int, input().split()) #n:세로 m:가로 k:연산 개수

board = [list(map(int, input().split())) for _ in range(n)]

oper = []
for _ in range(k):
    oper.append(list(map(int, input().split())))

oper_all = permutations(oper,len(oper))
# for i in oper_all:
#     print(i)

dx = [1,0,-1,0]
dy = [0,1,0,-1]

ans = 1e9
data = 0

for i in oper_all:
    temp_arr = copy.deepcopy(board)
    for r,c,s in i:
        a = c-1-s #시작 x좌표
        b = r-1-s #시작 y좌표
        e = c-1+s #끝 x좌표
        f = r-1+s #끝 y좌표
        cnt = ((r+s) - (r-s)) // 2 
        rotate(a,b,e,f,cnt,temp_arr)
    for j in range(n):
        data = sum(temp_arr[j])
        ans = min(ans, data)

# ans = 1e9
# data = 0
# for i in range(n):
#     data = sum(board[i])
#     ans = min(ans, data)

print(ans)


#r-s : 3-2 = 1
#r+s : 3+2 = 6
# stack = []
# bfs(1,0,5,4,stack)
# print(stack)
