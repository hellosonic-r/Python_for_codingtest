t = int(input())
for test_case in range(1,t+1):
    h,w = map(int, input().split()) #h: 높이, w: 너비
    board = [list(input()) for _ in range(h)]
    #전차 위치 부터 찾자
    for i in range(h):
        for j in range(w):
            if board[i][j]=="^" or board[i][j]=="v" or board[i][j]=="<" or board[i][j]==">":
                location = [j,i]
                break

    n = int(input())
    command = list(input())

    for i in range(n):
        if command[i] == "S":
            if board[location[1]][location[0]] == "<": #y: location[1] x: location[0]
                for x in range(location[0],-1,-1):
                    if board[location[1]][x] == "*":
                        board[location[1]][x] = "."
                        break
                    elif board[location[1]][x] == "#":
                        break
            elif board[location[1]][location[0]] == ">":
                for x in range(location[0],w):
                    if board[location[1]][x] == "*":
                        board[location[1]][x] = "."
                        break
                    elif board[location[1]][x] == "#":
                        break
            elif board[location[1]][location[0]] == "^":
                for y in range(location[1],-1,-1):
                    if board[y][location[0]] == "*":
                        board[y][location[0]] = "."
                        break
                    elif board[y][location[0]] == "#":
                        break
            elif board[location[1]][location[0]] == "v":
                for y in range(location[1],h):
                    if board[y][location[0]] == "*":
                        board[y][location[0]] = "."
                        break
                    elif board[y][location[0]] == "#":
                        break
        elif command[i] == "U": #y: location[1] x: location[0]
            nx = location[0]
            ny = location[1] - 1
            if 0<=nx<w and 0<=ny<h and board[ny][nx] == ".":
                board[location[1]][location[0]] = "."
                board[ny][nx] = "^"
                location = [nx,ny]
            else:
                board[location[1]][location[0]] = "^"
        elif command[i] == "D":
            nx = location[0]
            ny = location[1] + 1
            if 0<=nx<w and 0<=ny<h and board[ny][nx] == ".":
                board[location[1]][location[0]] = "."
                board[ny][nx] = "v"
                location = [nx,ny]
            else:
                board[location[1]][location[0]] = "v"
        elif command[i] == "L":
            nx = location[0] - 1
            ny = location[1]
            if 0<=nx<w and 0<=ny<h and board[ny][nx] == ".":
                board[location[1]][location[0]] = "."
                board[ny][nx] = "<"
                location = [nx,ny]
            else:
                board[location[1]][location[0]] = "<"
        elif command[i] == "R":
            nx = location[0] + 1
            ny = location[1]
            if 0<=nx<w and 0<=ny<h and board[ny][nx] == ".":
                board[location[1]][location[0]] = "."
                board[ny][nx] = ">"
                location = [nx,ny]
            else:
                board[location[1]][location[0]] = ">"
    print("#{}".format(test_case),end = " ")
    for i in board:
        print("".join(map(str, i)))



##다시 풀기
t = int(input())

for test_case in range(1, t+1):
    h, w = map(int, input().split()) #h:높이 w:너비
    board = [list(input()) for _ in range(h)]
    n = int(input())
    command = list(input())

    dx = [0,1,0,-1]
    dy = [-1,0,1,0]

    #먼저 탱크의 위치부터 찾는다
    for i in range(h):
        for j in range(w):
            if board[i][j] == "^" or board[i][j] == "v" or board[i][j] == "<" or board[i][j] == ">":
                location = [j, i]
                break

    for c in command:
        if c == "S":
            if board[location[1]][location[0]] == "^":
                for i in range(location[1]-1, -1, -1): #현위치에서 반대로 가면서 체크
                    if board[i][location[0]] == "*":
                        board[i][location[0]] = "."
                        break
                    if board[i][location[0]] == "#":
                        break
            elif board[location[1]][location[0]] == "v":
                for i in range(location[1]+1,h):
                    if board[i][location[0]] == "*":
                        board[i][location[0]] = "."
                        break
                    if board[i][location[0]] == "#":
                        break
            elif board[location[1]][location[0]] == "<":
                for i in range(location[0],-1,-1): #현위치에서 반대로 가면서 체크
                    if board[location[1]][i] == "*":
                        board[location[1]][i] = "."
                        break
                    if board[location[1]][i] == "#":
                        break
            elif board[location[1]][location[0]] == ">":
                for i in range(location[0]+1,w):
                    if board[location[1]][i] == "*":
                        board[location[1]][i] = "."
                        break
                    if board[location[1]][i] == "#":
                        break
        elif c == "U":
            nx = location[0] + dx[0]
            ny = location[1] + dy[0]
            if 0<=nx<w and 0<=ny<h and board[ny][nx] == ".":
                board[ny][nx] = "^"
                board[location[1]][location[0]] = "."
                location[0], location[1] = nx, ny
            else:
                board[location[1]][location[0]] = "^"
        elif c == "D":
            nx = location[0] + dx[2]
            ny = location[1] + dy[2]
            if 0 <= nx < w and 0 <= ny < h and board[ny][nx] == ".":
                board[ny][nx] = "v"
                board[location[1]][location[0]] = "."
                location[0], location[1] = nx, ny
            else:
                board[location[1]][location[0]] = "v"
        elif c == "L":
            nx = location[0] + dx[3]
            ny = location[1] + dy[3]
            if 0 <= nx < w and 0 <= ny < h and board[ny][nx] == ".":
                board[ny][nx] = "<"
                board[location[1]][location[0]] = "."
                location[0], location[1] = nx, ny
            else:
                board[location[1]][location[0]] = "<"
        elif c == "R":
            nx = location[0] + dx[1]
            ny = location[1] + dy[1]
            if 0 <= nx < w and 0 <= ny < h and board[ny][nx] == ".":
                board[ny][nx] = ">"
                board[location[1]][location[0]] = "."
                location[0], location[1] = nx, ny
            else:
                board[location[1]][location[0]] = ">"

    print("#{}".format(test_case),end = " ")
    for i in board:
        print("".join(map(str,i)))






