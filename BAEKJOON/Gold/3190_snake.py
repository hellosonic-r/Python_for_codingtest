##반례 다 맞는데 맞왜틀

def move(): #뱀의 머리 시작 좌표, 꼬리 좌표
    global d, sx,sy,ex,ey
    nx = sx + dx[d]
    ny = sy + dy[d]
    if nx<0 or nx>=n or ny<0 or ny>=n:
        return False
    else:
        if board[ny][nx] == 2:
            return False #false면 종료
        elif board[ny][nx] == 1: #사과가 있다면
            board[ny][nx] = 2
            sx,sy = nx,ny
            return True
        elif board[ny][nx] == 0:
            board[ny][nx] = 2
            board[ey][ex] = 0
            sx,sy = nx,ny
            for i in range(4):
                next_ex = ex + dx[i]
                next_ey = ey + dy[i]
                if 0<=next_ex<n and 0<=next_ey<n:
                    if board[next_ey][next_ex] == 2:
                        ex,ey = next_ex,next_ey  
                        break
            return True


n = int(input())

#뱀은 (0,0), 뱀의 길이 1
#뱀은 처음에 오른쪽

#이동한 칸에 사과 o >> 사과 없어지고 꼬리 그대로
#         사과 x >> 꼬리 비운다
board = [[0 for _ in range(n)] for _ in range(n)]
board[0][0] = 2

k = int(input())
apple = []
for _ in range(k):
    y, x = map(int, input().split())
    board[y-1][x-1] = 1

l = int(input())

d = 0
direction = []
for _ in range(l):
    x, c = input().split()
    direction.append((int(x),c))

dx = [1,0,-1,0] #동 남 서 북
dy = [0,1,0,-1]



sx,sy = 0,0
ex,ey = 0,0
time = 0
turn_t = 0
turn_d = ""
if direction:   
    t_list = direction.pop(0)
    turn_t = t_list[0]
    turn_d = t_list[1]

while True:
    time += 1
    if move() == False:
        break
    if time == turn_t:
        if turn_d == "L":
            d = (d-1)%4
            if direction:
                t_list = direction.pop(0)
                turn_t = t_list[0]
                turn_d = t_list[1]
        else:
            d = (d+1)%4
            if direction:
                t_list = direction.pop(0)
                turn_t = t_list[0]
                turn_d = t_list[1]
    print()
    print("time:",time)
    for i in range(n):
        print(" ".join(map(str, board[i])))

print(time)
# for i in range(n):
#     print(" ".join(map(str, board[i])))