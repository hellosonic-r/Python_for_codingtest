import sys
sys.setrecursionlimit(10**6)

def dfs(x,y):
    global cnt
    #동서남북 네 방향
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or ny<0 or nx>=m or ny>=n:
            continue
        else:
            #다음 좌표에 음식물 쓰레기가 있고, 아직 방문 안했다면
            if board[ny][nx] == 1 and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                #카운트 값 증가
                cnt += 1
                #다음 좌표에 대한 dfs함수 호출
                dfs(nx,ny)

n,m,k = map(int, input().split()) #n:세로 / m:가로 / k:쓰레기개수
board = [[0]*m for _ in range(n)]

for _ in range(k):
    r,c = map(int, input().split()) 
    board[r-1][c-1] = 1

dx = [0,1,0,-1]
dy = [-1,0,1,0]

visited = [[0 for _ in range(m)] for _ in range(n)]

cnt = 0 
max_cnt = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and visited[i][j] == 0:
            dfs(j,i) 
            max_cnt = max(cnt, max_cnt)
            cnt = 0

print(max_cnt)
