#1분 지날때마다 1킬로미터씩 동쪽으로 

h,w = map(int, input().split()) #h:세로 w:가로
board = [list(input()) for _ in range(h)]
visited = [[-1] * w for _ in range(h)]
for i in range(h):
    c = -1
    for j in range(w):
        if board[i][j] == "c":
            c = j
            visited[i][j] = 0
        else:
            if c != -1:
                visited[i][j] = j-c

for i in visited:
    print(" ".join(map(str, i)))
