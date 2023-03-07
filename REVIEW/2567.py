num = int(input())

#전체 도화지 : 0
graph = [[0] * 100 for _ in range(100)]

#색종이가 놓여진 부분에 1을 저장
for _ in range(num):
    x, y = map(int, input().split())
    for i in range(y,y+10):
        for j in range(x,x+10):
            if graph[i][j] == 0:
                graph[i][j] = 1
#전체 도화지 현재 인덱스와 그 다음 인덱스에 저장된 값이 다르면 둘레라고 보며
#가로, 세로 따로 저장한다.
sero = 0
for i in range(100):
    for j in range(100):
        if j == 99:
           continue 
        elif graph[i][j] != graph[i][j+1]:
            sero += 1
garo = 0
for i in range(100):
    for j in range(100):
        if j == 99:
            continue
        elif graph[j][i] != graph[j+1][i]:
            garo += 1
            
#전체 도화지의 끝 부분을 계산하게 된다면 for문의 범위를 초과하게 되므로
#전체 도화지의 끝 부분만 둘레를 따로 계산
edge_sero = 0
for k in range(100):
    if graph[k][0] == 1:
        edge_sero += 1
    if graph[k][99] == 1:
        edge_sero += 1
edge_garo = 0
for z in range(100):
    if graph[0][z] == 1:
        edge_garo += 1
    if graph[99][z] == 1:
        edge_garo += 1

print(sero + garo + edge_sero + edge_garo)
