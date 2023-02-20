###교재의 코드
n, m = map(int, input().split())

#방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
visit_list = [[0]*m for _ in range(n)]

#캐릭터의 위치, 방향을 입력받기
a,b,d = map(int, input().split())
visit_list[a][b] = 1 #현재 위치 방문 처리

#전체 맵 정보 입력받기
gameMap = []
for _ in range(n):
    gameMap.append(list(map(int, input().split())))

#북,동,남,서 방향 정의
da = [-1,0,1,0]
db = [0,1,0,-1]

#왼쪽으로 회전
def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3

#시뮬레이션 시작
count = 1
turn_time = 0
while True:
    #왼쪽으로 회전
    turn_left()
    nextA = a + da[d]
    nextB = b + db[d]
    #회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if visit_list[nextA][nextB] == 0 and gameMap[nextA][nextB] == 0:
        visit_list[nextA][nextB] = 1
        a, b = nextA, nextB
        count += 1
        turn_time = 0
        continue
    #회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    #네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nextA = a - da[d]
        nextB = b - db[d]
        #뒤로 갈 수 있다면 이동하기
        if gameMap[nextA][nextB] == 0:
            a = nextA
            b = nextB
        #뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0
print(count)

