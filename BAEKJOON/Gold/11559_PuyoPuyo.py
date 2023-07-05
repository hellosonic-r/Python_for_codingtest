#연결된 뿌요들의 좌표를 구하는 코드 
def dfs(x,y):
    global color
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<6 and 0<=ny<12:
            if v[ny][nx] == 0 and board[ny][nx] == color:
                v[ny][nx] = 1
                puyo_list.append((nx,ny)) #연결된 블럭 리스트에 저장
                dfs(nx,ny)

#뿌요들이 없어지고나서 중력의 영향을 받아 아래로 떨어지게 하는 코드
def move():
    line = [0,0,0,0,0,0] #x좌표 idx0 ~ idx5
    for j in range(len(arr)):
        if line[arr[j][0]] == 0: #x좌표 방문처리
            line[arr[j][0]] = 1 #x좌표 방문처리
            stack = [] #stack에 뿌요들을 담는다.
            for i in range(12): #y좌표를 처음부터 끝까지 돌면서
                if board[i][arr[j][0]] != ".": #뿌요가 놓여져 있다면
                    stack.append(board[i][arr[j][0]]) #스택에 담는다
                    board[i][arr[j][0]] = "." #그 후 방문한 좌표의 뿌요를 없앤다
            
            for k in range(11,-1,-1): #아래에서부터 차례대로
                if stack: #스택에 뿌요가 없을 때까지
                    board[k][arr[j][0]] = stack.pop() #스택에 있는 뿌요를 하나씩 꺼내어 그리드에 채워준다
                else:
                    break


board = [list(input()) for _ in range(12)]

dx = [1,0,-1,0]
dy = [0,-1,0,1]

answer = 0 

color = ""

while True: #터질 뿌요가 없을때까지 반복을 진행
    v = [[0]*6 for _ in range(12)] 
    pung_list = [] #1회 연쇄 때, 터질 뿌요들의 좌표를 저장하는 리스트
    #전체 그리드를 돌면서 탐색
    for y in range(12):
        for x in range(6):
            if board[y][x] != "." and v[y][x] == 0: #만약 뿌요가 놓여져있고 방문안한 좌표라면
                color = board[y][x] #color 변수에 뿌요 색깔 저장
                v[y][x] = 1 #해당 좌표 방문처리
                puyo_list = [(x,y)] #뿌요 리스트에 해당 좌표 저장
                dfs(x,y) #연결된 뿌요의 좌표를 구하는 코드

                if len(puyo_list) >= 4: #dfs 돌고나서 뿌요가 4개이상 연결되어 있다면
                    pung_list.append(puyo_list) #터지는 리스트에 추가
                else: #뿌요가 4개 미만으로 연결되어 있다면
                    puyo_list = [] #그냥 넘어간다.

    if pung_list: #만약 터질 뿌요가 있다면
        for arr in pung_list: #터질 뿌요의 좌표가 저장된 리스트를 하나씩 꺼낸다
            for a,b in arr: 
                board[b][a] = "." #뿌요들을 터뜨린다.
            move() #공중에 떠있는 뿌요들을 아래로 내린다.
        answer += 1 #연쇄 카운트
    
    else: #만약 터질 뿌요가 없다면
        break #반복문 탈출

print(answer)


