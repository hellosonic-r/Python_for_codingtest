c, r = map(int, input().split())
k = int(input())
if k > c*r:
    print(0)
r_list = list(range(r,0,-1))
c_list = list(range(c-1,0,-1))

i = 0
seat = 0
plus_time = 0
while True:
    if i > len(r_list)-1 or i > len(c_list)-1:
        break
    if seat >= k:
        break
    else:
        seat = seat + r_list[i]
        plus_time += 1
    if seat >= k:
        break
    else:
        seat = seat + c_list[i]
        plus_time += 1
    i+=1

if k > seat:
    if k <= c*r and plus_time % 4 == 0:
        x = 1 + plus_time // 4
        y = plus_time // 4
        print(x,y+abs(seat-k))
    elif k <= c*r and plus_time % 4 == 1:
        x = 1 + plus_time // 4
        y = r - plus_time // 4
        print(x+abs(seat-k),y)
    elif k <= c*r and plus_time % 4 == 2:
        x = c - plus_time // 4
        y = r - plus_time // 4
        print(x,y-abs(seat-k))
    elif k <= c*r and plus_time % 4 == 3:
        x = c - plus_time // 4
        y = 1 + plus_time // 4
        print(x-abs(seat-k),y)
else: 
    if k <= c*r and plus_time % 4 == 1: #plus time =5 # y값에서 빼기
        x = 1 + plus_time // 4
        y = r - plus_time // 4
        print(x,y-abs(seat-k))
    elif k <= c*r and plus_time % 4 == 2: #plustime = 6 x 값에서 빼기 
        x = c - plus_time // 4
        y = r - plus_time // 4
        print(x-abs(seat-k),y)
    elif k <= c*r and plus_time % 4 == 3: #y에서 더하기
        x = c - plus_time // 4
        y = 1 + plus_time // 4
        print(x,y+abs(seat-k)) 
    elif k <= c*r and plus_time % 4 == 0: # x에서 더하기 
        x = 1 + plus_time // 4
        y = plus_time // 4
        print(x+abs(seat-k),y)


