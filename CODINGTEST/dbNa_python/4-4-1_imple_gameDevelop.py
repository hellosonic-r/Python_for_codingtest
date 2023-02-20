###게임 개발
##다른 사람의 코드 (무한입력)
#가로:n 세로:m 저장
n, m = map(int, input().split())
#게임 캐릭터가 있는 위치 (a,b) 와 바라보고 있는 방향 : d 저장
a,b,d = map(int, input().split())

#게임 캐릭터가 방문한 칸의 수 count 생성
count = 0

#2차원 배열 gameMap 생성
gameMap = []
for _ in range(n):
    gameMap.append(list(map(int, input().split())))

#동서남북 direction 생성
direction = [0,1,2,3]

#움직일 수 있는 da,db 정의
da = [0,-1,0,1]
db = [-1,0,1,0]

#가본 칸은 바다로 변경, count 추가
gameMap[a][b] = 1
count += 1

#문제 매뉴얼대로 움직이기
while True:
    #4번동안 반복
    i = 0
    while i < 4:
        newA = a + da[d]
        newB = b + db[d]
        #바로 왼쪽에 0이 있으면
        if gameMap[newA][newB] == 0:
            #d 방향 왼쪽으로 회전
            d = direction[direction.index(d)-1]
            #왼쪽 한 칸 전진
            a, b = newA, newB
            #가본 칸은 바다로 변경, count 추가
            gameMap[a][b] = 1
            count+=1
            i = 0
        #바로 왼쪽에 1이 있다면(갈 수 없다면)
        else:
            d = direction[direction.index(d)-1]
            i += 1

    #4번 반복 후에도 갈 곳이 없다면 뒤로 한 칸 후진
    newA = a - db[d]
    newB = b - da[d]
    #후진 할 수 있다면
    if gameMap[newA][newB] == 0:
        #1단계 다시 진행
        a, b = newA, newB
        #가본 칸은 바다로 변경
        gameMap[a][b] = 1
        count += 1
    else: 
        break
print(count)
