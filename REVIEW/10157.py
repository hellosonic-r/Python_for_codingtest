###런타임 에러 코드
# c, r = map(int, input().split()) #c:가로7 r:세로6
# k = int(input())

# seat = [[0]*c for _ in range(r)]

# time = 0
# num = 0

# def up():
#     global time, num
#     for i in range(time, r-time):
#         num += 1
#         seat[i][0+time] = num 
# def right():
#     global time, num
#     for i in range(time+1, c-time):
#         num += 1
#         seat[r-1-time][i] = num
# def down():
#     global time, num
#     for i in range(r-2-time, time-1, -1):
#         num += 1
#         seat[i][-(time+1)] = num
# def left():
#     global time, num
#     for i in range(c-2-time, time,-1):
#         num += 1
#         seat[time][i] = num

# while True:
#     if (r+1) // (time+1) < 2:
#         break
#     up()
#     right()
#     down()
#     left()
#     time += 1

# x = 0
# y = 0
# for i in range(r):
#     for j in range(c):
#         if seat[i][j] == k:
#             y,x = i,j
#             break

# if x==0 and y==0:
#     print(0)
# else:
#     print(x+1,y+1)


###다른 사람의 코드
c, r = map(int, input().split())

k = int(input())

if k > c*r:
    print(0)
    exit() #종료

dx = [0,1,0,-1]
dy = [1,0,-1,0]

grid = [[0]*c for _ in range(r)]
direction = x = y = 0

for seat in range(1, c*r + 1):
    if seat == k:
        print(x+1, y+1)
        break
    else:
        grid[y][x] = seat
        x += dx[direction]
        y += dy[direction]
        if x<0 or y<0 or x>=c or y>=r or grid[y][x] != 0:
            x -= dx[direction]
            y -= dy[direction]
            #범위를 벗어나면 뒤로 뺐다가 방향 바꿔서 전진
            direction = (direction+1)%4
            x += dx[direction]
            y += dy[direction]