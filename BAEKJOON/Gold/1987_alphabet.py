#set() 시간복잡도 O(1)
def dfs(x,y,count):
    global ans
    ans = max(ans, count)
    for i in range(4): #네 방향에 대하여
        #가능한 다음 좌표를 만들고
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or ny<0 or nx>=c or ny>=r: #범위를 벗어나면 안됨
            continue
        else: #범위 안에서
            if alphabet_list[ny][nx] not in v: #다음좌표의 알파벳이 방문테이블에 없다면
                v.add(alphabet_list[ny][nx]) #방문테이블에 추가
                dfs(nx,ny,count+1) #count를 1씩 더하며, 다음 좌표에 대한 dfs호출
                v.remove(alphabet_list[ny][nx]) #돌아와서는 방문체크 해제

r, c = map(int, input().split()) # 세로, 가로

alphabet_list = [list(input()) for _ in range(r)]

dx = [0,1,0,-1]
dy = [-1,0,1,0]

ans = 0
v = set() 
v.add(alphabet_list[0][0])#처음 알파벳 방문처리
dfs(0,0,1)

print(ans)

##시간초과 - 리스트 시간 복잡도 O(n)
def dfs(x,y,count):
    global ans
    ans = max(ans, count)
    for i in range(4): #네 방향에 대하여
        #가능한 다음 좌표를 만들고
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or ny<0 or nx>=c or ny>=r: #범위를 벗어나면 안됨
            continue
        else: #범위 안에서
            if alphabet_list[ny][nx] not in v: #다음좌표의 알파벳이 방문테이블에 없다면
                v.append(alphabet_list[ny][nx]) #방문테이블에 추가
                dfs(nx,ny,count+1) #count를 1씩 더하며, 다음 좌표에 대한 dfs호출
                v.pop() #돌아와서는 방문체크 해제

r, c = map(int, input().split()) # 세로, 가로

alphabet_list = [list(input()) for _ in range(r)]

dx = [0,1,0,-1]
dy = [-1,0,1,0]

ans = 0
v = [alphabet_list[0][0]] #처음 알파벳 방문처리
dfs(0,0,1)

print(ans)

##제일 처음 작성한 코드(틀린코드)
def dfs(x,y):
    global count
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or ny<0 or nx>=c or ny>=r:
            continue
        else:
            if alphabet_list[ny][nx] not in v:
                v.append(alphabet_list[ny][nx])
                count += 1
                dfs(nx,ny)

r, c = map(int, input().split()) # 세로, 가로

alphabet_list = [list(input()) for _ in range(r)]

dx = [0,1,0,-1]
dy = [-1,0,1,0]


count = 1

v = [alphabet_list[0][0]]
dfs(0,0)

print(count)

# ##시간초과 (너무 많은 좌표 방문)
# def dfs(n,x,y):
#     global count, max_count
#     if v.count(alphabet_list[y][x]) == 2:
#         max_count = max(max_count, count-1)
#         return
#     if n == r*c:
#         return
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if nx<0 or ny<0 or nx>=c or ny>=r:
#             continue
#         else:
#             v.append(alphabet_list[ny][nx])
#             count += 1
#             dfs(n+1,nx,ny)
#             count -= 1
#             v.pop()

# r, c = map(int, input().split()) # 세로, 가로

# alphabet_list = [list(input()) for _ in range(r)]

# dx = [0,1,0,-1]
# dy = [-1,0,1,0]


# count = 1
# max_count = 0

# v = [alphabet_list[0][0]]
# dfs(0,0,0)

# print(max_count)