def dfs(count, start, temp_list):
    if len(temp_list) == m:
        result.append(temp_list)
        return
    
    for i in range(start, len(chicken)):
        if i not in v:
            v.append(i)
            dfs(count+1, i+1, temp_list+[chicken[i]])
            v.pop()




n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

chicken = []
result = [] #폐업하지 않은 치킨집 케이스들

for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            chicken.append((j,i))

v = []

dfs(0,0,[])

total = 0

ans = []

for k in result:
    total = 0
    for y in range(n):
        for x in range(n):
            if board[y][x] == 1:
                distance = 1000
                for c in k:
                    if distance > abs(x-c[0]) + abs(y-c[1]):
                        distance = abs(x-c[0]) + abs(y-c[1])
                total += distance
    
    ans.append(total)
                
print(min(ans))