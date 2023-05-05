def dfs(x,y,cnt):
    global ans
    #그리드 상 오른쪽 위에 도착하면
    if x == c-1 and y == 0:
        if cnt == k: #만약 거리가 k이면
            ans += 1 #ans에 1 추가
        return
    #네 방향에 대해 다음 좌표로 이동할 수 있는지 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or ny<0 or nx>=c or ny>=r:
            continue
        else:
            #다음 좌표를 아직 방문 안했고, '.'이라면 다음 좌표 방문
            if v[ny][nx] == 0 and board[ny][nx] == '.':
                v[ny][nx] = 1
                dfs(nx,ny,cnt+1) #다음 좌표 방문했으니 cnt+1. 이것은 거리가 된다.
                v[ny][nx] = 0

r, c, k = map(int,input().split()) #거리가 k인 가짓수 세기
board = [list(map(str, input())) for _ in range(r)]

v = [[0]*c for _ in range(r)]

dx = [0,1,0,-1]
dy = [-1,0,1,0]

ans = 0

v[r-1][0] = 1 #시작 좌표는 방문처리 해주어야 함
dfs(0,r-1,1)

print(ans)