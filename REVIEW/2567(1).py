num = int(input())
graph = [[0] * 102 for _ in range(102)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for _ in range(num):
    x, y = map(int, input().split())
    for i in range(y, y+10):
        for j in range(x,x+10):
            graph[i][j] = 1

result = 0

for i in range(1,102): #1 ~ 100
    for j in range(1,102):
        if graph[i][j] == 1:
            cnt = 0
            for k in range(4):
                nx = j + dx[k]
                ny = i + dy[k]
                if graph[ny][nx] == 1:
                    cnt += 1
            if cnt == 3: #상하좌우 중 3칸이 1로 채워져 있으면 변에 해당
                result += 1
            elif cnt == 2: #상하좌우 중 2칸이 1로 채워져 있으면 모서리에 해당
                result += 2
print(result)                