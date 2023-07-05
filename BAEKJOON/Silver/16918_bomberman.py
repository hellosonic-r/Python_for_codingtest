'''
##시간초과
import sys

r, c, n = map(int,input().split()) #r*c격자판 #n초가 흐른 후의 격자판
board = [] 
for _ in range(r):
    board.append(list(sys.stdin.readline()))

check = []

for y in range(r):
    for x in range(c):
        if board[y][x] == "O":
            check.append((x,y))

#시간이 2의 배수일 경우 : 꽉찬 폭탄들
#0, 1, 5,... 초 일때 : 초기 폭탄
#3, 7, 11, ... 초 일때 : 초기 폭탄 터짐

dx = [0,1,0,-1]
dy = [-1,0,1,0]

if n != 0 and n % 2 == 0:
    line = "O"*c
    for _ in range(r):
        print(line)
elif n == 0 or n%4 == 1:
    for i in range(r):
        print("".join(map(str, board[i])))
elif n%4 == 3:
    v = []
    for y in range(r):
        for x in range(c):
            if (x,y) in check:
                board[y][x] = "."
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0<=nx<c and 0<=ny<r:
                        board[ny][nx] = "."
                        v.append((nx, ny))
            elif ((x,y) not in check) and ((x,y) not in v):
                board[y][x] = "O"

    for i in range(r):
        print("".join(map(str, board[i])))



#또 시간초과
import sys

r, c, n = map(int,input().split()) #r*c격자판 #n초가 흐른 후의 격자판
board = [] 
check = []
for _ in range(r):
    board.append(list(sys.stdin.readline().strip()))
    for idx in range(c):
        if board[-1][idx] == "O":
            check.append((idx, len(board)-1))


#시간이 2의 배수일 경우 : 꽉찬 폭탄들
#0, 1, 5,... 초 일때 : 초기 폭탄
#3, 7, 11, ... 초 일때 : 초기 폭탄 터짐

dx = [0,1,0,-1]
dy = [-1,0,1,0]

if n != 0 and n % 2 == 0:
    line = "O"*c
    for _ in range(r):
        print(line)
elif n == 0 or n%4 == 1:
    for i in range(r):
        print("".join(map(str, board[i])))
elif n%4 == 3:
    v = []
    for y in range(r):
        for x in range(c):
            if (x,y) in check:
                board[y][x] = "."
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0<=nx<c and 0<=ny<r:
                        board[ny][nx] = "."
                        v.append((nx, ny))
            elif ((x,y) not in check) and ((x,y) not in v):
                board[y][x] = "O"

    for i in range(r):
        print("".join(map(str, board[i])))


##또 시간초과
import sys

r, c, n = map(int,input().split()) #r*c격자판 #n초가 흐른 후의 격자판
board = [] 
check = []
for _ in range(r):
    board.append(list(sys.stdin.readline().strip()))
    for idx in range(c):
        if board[-1][idx] == "O":
            check.append((idx, len(board)-1))

#시간이 2의 배수일 경우 : 꽉찬 폭탄들
#0, 1, 5,... 초 일때 : 초기 폭탄
#3, 7, 11, ... 초 일때 : 초기 폭탄 터짐

dx = [0,1,0,-1]
dy = [-1,0,1,0]
side_check = []
for (x,y) in check:
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<c and 0<=ny<r:
            side_check.append((nx,ny))

check.extend(side_check)
check = list(set(check))

if n != 0 and n % 2 == 0:
    line = "O"*c
    for _ in range(r):
        print(line)
elif n == 0 or n%4 == 1:
    for i in range(r):
        print("".join(map(str, board[i])))
elif n%4 == 3:
    for y in range(r):
        for x in range(c):
            if (x,y) in check:
                board[y][x] = "."
            else:
                board[y][x] = "O"

    for i in range(r):
        print("".join(map(str, board[i])))


##틀림
import sys

r,c,n = map(int, input().split())
board = []
for _ in range(r):
    board.append(list(input()))

#시간이 2의 배수일 경우 : 꽉찬 폭탄들
#0, 1, 5,... 초 일때 : 초기 폭탄
#3, 7, 11, ... 초 일때 : 초기 폭탄 터짐

dx = [0,1,0,-1]
dy = [-1,0,1,0]

if n == 0 or n%4 == 1:
    for i in range(r):
        print("".join(map(str, board[i])))

elif n != 0 and n%2 == 0:
    for i in range(r):
        print("O"*c)

elif n%4 == 3:
    bomb = [["O"] * c for _ in range(r)]
    for y in range(r):
        for x in range(c):
            if board[y][x] == "O":
                bomb[y][x] = "."
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0<=nx<c and 0<=ny<r:
                        bomb[ny][nx] = "."
    for i in range(r):
        print("".join(map(str,bomb[i])))
'''

##맞음
import sys

r,c,n = map(int, input().split())
board = []
for _ in range(r):
    board.append(list(input()))

dx = [0,1,0,-1]
dy = [-1,0,1,0]

if n <= 1:
    for i in range(r):
        print("".join(map(str, board[i])))

elif n != 0 and n%2 == 0:
    for i in range(r):
        print("O"*c)

else: 
    bomb1 = [["O"] * c for _ in range(r)]
    for y in range(r):
        for x in range(c):
            if board[y][x] == "O":
                bomb1[y][x] = "."
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0<=nx<c and 0<=ny<r:
                        bomb1[ny][nx] = "."
    bomb2 = [["O"] * c for _ in range(r)]
    for y in range(r):
        for x in range(c):
            if bomb1[y][x] == "O":
                bomb2[y][x] = "."
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0<=nx<c and 0<=ny<r:
                        bomb2[ny][nx] = "."           
    if n%4 == 3:
        for i in range(r):
            print("".join(map(str, bomb1[i])))
    elif n%4 == 1:
        for i in range(r):
            print("".join(map(str, bomb2[i])))



