string = list(input())

d = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7}

loc = [d[string[0]],int(string[1])-1]

dx = [1,2,2,1,-1,-2,-2,-1]
dy = [-2,-1,1,2,2,1,-1,-2]

cnt = 0

for i in range(8):
    nx = loc[0] + dx[i]
    ny = loc[1] + dy[i]
    if 0<=nx<8 and 0<=ny<8:
        cnt += 1

print(cnt)
