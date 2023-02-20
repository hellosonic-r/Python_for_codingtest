##다른사람 풀이 참고한 나의 풀이 (실패)
n, m = map(int, input().split())
a, b, d = map(int, input().split()) # 2, 2,0
direction = [0,1,2,3]
da = [0,-1,0,1]
db = [-1,0,1,0]
count = 0
gameMap = []
for _ in range(n):
    gameMap.append(list(map(int, input().split())))

gameMap[a][b] = 1
count += 1
while True:
    i = 0
    while i < 4:
        newA = a + da[d]  
        newB = b + db[d]
        if gameMap[newA][newB] == 0:
            a ,b = newA, newB
            d = direction[direction.index(d)-1]
            gameMap[a][b] = 1
            count += 1
            i = 0
        else:
            d = direction[direction.index(d)-1]
            i += 1
    newA = a - da[d]
    newB = b - db[d]
    if gameMap[newA][newB] == 0:
        a = newA
        b = newB
        gameMap[a][b] = 1
        count += 1
    else: 
        break
print(count)
