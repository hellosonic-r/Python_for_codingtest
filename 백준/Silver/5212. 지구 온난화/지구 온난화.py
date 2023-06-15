
import copy

r, c = map(int, input().split()) #r*c
board = [list(input()) for _ in range(r)]

dx = [0,-1,0,1]
dy = [-1,0,1,0]

after = copy.deepcopy(board)
land_cnt = 0
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

            if cnt >= 3:
                after[y][x] = "."
                land_cnt -= 1


#줄이기

if land_cnt == 0:
    print("X")

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
            if after[y][x] == "X":
                idx.append(x)
                break

    for i in after[r_start:r_end+1]:
        print("".join(i[idx[0]:idx[-1]+1]))
    

