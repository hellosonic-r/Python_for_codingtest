def dfs(x,y):
    global color
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<6 and 0<=ny<12:
            if v[ny][nx] == 0 and board[ny][nx] == color:
                v[ny][nx] = 1
                puyo_list.append((nx,ny))
                dfs(nx,ny)


def move():
    line = [0,0,0,0,0,0]
    for j in range(len(arr)):
        if line[arr[j][0]] == 0:
            line[arr[j][0]] = 1
            stack = []
            for i in range(12):
                if board[i][arr[j][0]] != ".":
                    stack.append(board[i][arr[j][0]])
                    board[i][arr[j][0]] = "."
            
            for k in range(11,-1,-1):
                if stack:
                    board[k][arr[j][0]] = stack.pop()
                else:
                    break

                    



board = [list(input()) for _ in range(12)]

dx = [1,0,-1,0]
dy = [0,-1,0,1]

v = [[0]*6 for _ in range(12)] 

answer = 0 

color = ""

while True:
    v = [[0]*6 for _ in range(12)] 
    flag = False
    pung_list = []
    for y in range(12):
        for x in range(6):
            if board[y][x] != "." and v[y][x] == 0:
                color = board[y][x]
                v[y][x] = 1
                puyo_list = [(x,y)]
                dfs(x,y)

                if len(puyo_list) >= 4: #만약 블럭이 4개 이상이라면 
                    pung_list.append(puyo_list) #터지는 리스트에 추가
                else: #아니라면
                    puyo_list = [] #걍 넘어가

    if pung_list:
        for arr in pung_list:
            for a,b in arr: 
                board[b][a] = "."
            move()
        answer += 1
    
    else:
        break


print(answer)


