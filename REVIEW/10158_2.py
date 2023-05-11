##시간초과
w, h = map(int, input().split()) #w: 가로 / h: 세로
sx, sy = map(int, input().split())
t = int(input())
time = 0
x_turn = 0
y_turn = 0
while True:
    time += 1
    if x_turn % 2 == 0:
        sx = sx + 1
        if sx == w or sx == 0:
            x_turn += 1
    else:
        sx = sx - 1
        if sx == w or sx == 0:
            x_turn += 1
    if y_turn % 2 == 0:
        sy = sy + 1
        if sy == h or sy == 0:
            y_turn += 1
    else:
        sy = sy - 1
        if sy == h or sy == 0:
            y_turn += 1
    if time == t:
        break

print(sx, sy)


##시간 초과
w, h = map(int ,input().split())
sx, sy = map(int ,input().split())
t = int(input())

x_turn = 0
y_turn = 0

for i in range(1,t+1):
    if x_turn%2 == 0:
        sx += 1
        if sx == w:
            x_turn += 1
    else:
        sx -= 1
        if sx == 0:
            x_turn +=1
    if y_turn%2 == 0:
        sy += 1
        if sy == h:
            y_turn += 1
    else:
        sy -= 1
        if sy == 0:
            y_turn += 1

print(sx,sy)


##반복문 안쓰고 구현해보기
w, h = map(int ,input().split())
sx, sy = map(int ,input().split())
t = int(input())

x = (sx + t) // w #(시작x + time) // 전체가로
y = (sy + t) // h


if x%2 == 0:
    x_ans = (sx + t) % w
else:
    x_ans = w - ((sx+t)%w)
if y%2 == 0:
    y_ans = (sy + t) % h
else:
    y_ans = h - ((sy+t)%h) 

print(x_ans,y_ans)