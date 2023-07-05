##맞왜틀
r, c = map(int, input().split()) #r*c
board = [list(input()) for _ in range(r)]

dx = [0,-1,0,1]
dy = [-1,0,1,0]

after = [["."] * c for _ in range(r)] #50년 후의 지도를 정보

for y in range(r):
    for x in range(c):
        if board[y][x] == "X": #현재 지도의 부분 중 섬인 부분
            cnt = 0 #섬을 둘러싼 바다의 개수 카운트
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<c and 0<=ny<r:
                    if board[ny][nx] == ".": #만약 "."이라면 바다개수 +1
                        cnt += 1
                else: #범위를 벗어나는 곳이라면 바다개수 +1
                    cnt += 1

            if cnt <= 2: #바다의 개수가 2이하이면 50년 후에도 그곳은 섬이 있다.
                after[y][x] = "X"

#지도의 크기 줄이기
result = []

for y in range(r):
    if after[y].count(".") == c:
        continue
    else:
        result.append(after[y])

start_idx = c-1 
end_idx = 0

for x in range(c):
    for y in range(len(result)):
        if result[y][x] == "X":
            if start_idx > x:
                start_idx = x
            if end_idx < x:
                end_idx = x

for i in range(len(result)):
    print("".join(map(str,result[i][start_idx:end_idx+1])))



# ##맞왜틀
# r, c = map(int, input().split()) #r*c
# board = [list(input()) for _ in range(r)]

# dx = [0,-1,0,1]
# dy = [-1,0,1,0]

# after = [["."] * c for _ in range(r)]

# for y in range(r):
#     for x in range(c):
#         if board[y][x] == "X":
#             cnt = 0
#             for i in range(4):
#                 nx = x + dx[i]
#                 ny = y + dy[i]
#                 if 0<=nx<c and 0<=ny<r:
#                     if board[ny][nx] == ".":
#                         cnt += 1
#                 else:
#                     cnt += 1

#             if cnt <= 2:
#                 after[y][x] = "X"

# #줄이기
# result = []

# for y in range(r):
#     if after[y].count(".") == c:
#         continue
#     else:
#         result.append(after[y])

# start_idx = c-1 
# end_idx = 0

# flag = True
# for x in range(c):
#     for y in range(len(result)):
#         if result[y][x] == "X":
#             start_idx = x
#             flag = False
#             break
#     if flag == False:
#         break
# flag = True
# for x in range(c-1, -1, -1):
#     for y in range(len(result)):
#         if result[y][x] == "X":
#             end_idx = x
#             flag = False
#             break
#     if flag == False:
#         break

# for i in range(len(result)):
#     print("".join(map(str,result[i][start_idx:end_idx+1])))



import copy

r, c = map(int, input().split()) #r*c
board = [list(input()) for _ in range(r)]

dx = [0,-1,0,1]
dy = [-1,0,1,0]

after = copy.deepcopy(board) #현재 지도를 50년 후의 지도에 그대로 복사
land_cnt = 0 #섬의 개수 카운트
for y in range(r):
    for x in range(c):
        if board[y][x] == "X":
            cnt = 0
            land_cnt += 1 
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<c and 0<=ny<r:
                    if board[ny][nx] == ".":
                        cnt += 1
                else:
                    cnt += 1

            if cnt >= 3: #삼면 이상이 바다로 둘러쌓여 있다면,
                after[y][x] = "." #50년 후의 지도를 바다로 갱신
                land_cnt -= 1 #섬의 개수 - 1


#줄이기

if land_cnt == 0: #섬이 하나도 없다면, 
    print("X") #그냥 X 출력

else:
    #위에서부터 체크
    r_start = 0
    r_end = 0
    for i in range(r):
        if "X" in after[i]:
            r_start = i
            break

    #아래에서부터 체크
    for i in range(r-1, -1, -1):
        if "X" in after[i]:
            r_end = i
            break

    #가로 체크
    idx = []
    for x in range(c):
        for y in range(r_start, r_end+1):
            if after[y][x] == "X": #열에 하나라도 섬이 있으면
                idx.append(x) #x좌표를 저장하고
                break #반복문 탈출

    for i in after[r_start:r_end+1]:
        print("".join(i[idx[0]:idx[-1]+1]))
    

