king, stone, n = input().split()

king = list(map(str, str(king)))
stone = list(map(str, str(stone)))
king = [ord(king[0])-65, int(king[1])-1]
stone = [ord(stone[0])-65, int(stone[1])-1]
         
n = int(n)
command_list = []
for _ in range(n):
    command_list.append(input())

board = [[0]*8 for _ in range(8)]
c = {"R":0, "L":1, "B":2, "T":3, "RT":4, "LT":5, "RB":6, "LB":7}

board[king[1]][king[0]] = 1
board[stone[1]][stone[0]] = 2

dx = [1,-1,0,0,1,-1,1,-1]
dy = [0,0,-1,1,1,1,-1,-1]
k_x = king[0]
k_y = king[1]
s_x = stone[0]
s_y = stone[1]
for i in range(n):
    k_nx = k_x + dx[c[command_list[i]]]
    k_ny = k_y + dy[c[command_list[i]]]
    s_nx = s_x + dx[c[command_list[i]]]
    s_ny = s_y + dy[c[command_list[i]]]
    if 0<=k_nx<8 and 0<=k_ny<8: #킹이 범위 안에 있는데
        if board[k_ny][k_nx] == 2: #다음 갈 곳에 돌이 있는 경우
            if 0<=s_nx<8 and 0<=s_ny<8: #돌이 다음으로 갈 수 있다면
                #킹과 돌 같이 이동
                board[k_y][k_x] = 0
                board[k_ny][k_nx] = 1
                k_x,k_y = k_nx,k_ny
                board[s_y][s_x] = 0
                board[s_ny][s_nx] = 2
                s_x,s_y = s_nx,s_ny
                #다음으로 갈 수 없다면 킹도 돌도 못감
            else:
                continue
        else: #다음 갈 곳에 돌이 없는 경우 킹만 이동
            board[k_y][k_x] = 0
            board[k_ny][k_nx] = 1
            k_x,k_y = k_nx,k_ny


print(chr(k_x+65)+str(k_y+1))
print(chr(s_x+65)+str(s_y+1))

