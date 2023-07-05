def turn_right(arr): #시계방향 회전
    arr.insert(0,arr.pop())
    return

def turn_left(arr): #반시계방향 회전
    arr.append(arr.pop(0))
    return

#4개의 톱니바퀴에 대한 상태 저장
gear = []
for _ in range(4):
    gear.append(list(map(int, str(input()))))

#회전시킨 방법 저장 (톱니바퀴의 번호, 방향)
k = int(input()) #회전 횟수
board = []
for _ in range(k):
    board.append(list(map(int, input().split()))) #1: 시계 -1:반시계

ans = 0

while board:
    x = board.pop(0)
    g_no = x[0] #톱니바퀴 번호
    direction = x[1] #회전시킨 방향
    left = 0
    right = 0
    if direction == 1: #시계방향 회전
        left = gear[g_no-1][6] #현재 톱니바퀴의 왼쪽 부분
        right = gear[g_no-1][2] #현재 톱니바퀴의 오른쪽 부분
        turn_right(gear[g_no-1]) #고른 톱니바퀴는 회전
        left_flag = True #시계방향 회전했다고 체크(왼쪽에 놓인 톱니바퀴 체크용)
        right_flag = True #시계방향 회전했다고 체크(오른쪽에 놓인 톱니바퀴 체크용)
        if g_no == 2 or g_no == 3: #만약 톱니바퀴 번호가 두 번째나 세 번째일 때,
            #왼쪽에 놓인 톱니바퀴들과 오른쪽에 놓인 톱니바퀴들. 총 두가지 케이스 확인
            #왼쪽 부분 체크
            for i in range(g_no-2,-1,-1):
                if gear[i][2] == left: #맞닿은 부분이 같을 때
                    break #나머지 톱니바퀴 확인할 필요 없이 반복문 탈출
                else:
                    if left_flag: #만약 고른 톱니바퀴가 시계 방향으로 회전했다면
                        left = gear[i][6] #방문한 톱니바퀴의 왼쪽 부분으로 갱신
                        turn_left(gear[i]) #톱니바퀴를 돌린다.
                        left_flag = False #반시계 방향으로 회전했다고 체크 
                    else: #만약 고른 톱니바퀴가 반시계 방향으로 회전했다면
                        left = gear[i][6] #방문한 톱니바퀴의 왼쪽 부분으로 갱신
                        turn_right(gear[i]) #톱니바퀴를 돌린다.
                        left_flag = True #시계 방향으로 회전했다고 체크
            #오른쪽 부분 체크
            for i in range(g_no,4):
                if gear[i][6] == right: #맞닿은 부분이 같을 때
                    break #나머지 톱니바퀴 확인할 필요 없이 반복문 탈출
                else:
                    if right_flag: #만약 고른 톱니바퀴가 시계 방향으로 회전했다면
                        right = gear[i][2] #방문한 톱니바퀴의 오른쪽 부분으로 갱신
                        turn_left(gear[i]) #톱니바퀴를 돌린다.
                        right_flag = False #반시계 방향으로 회전했다고 체크
                    else: #만약 고른 톱니바퀴가 반시계 방향으로 회전했다면
                        right = gear[i][2] #방문한 톱니바퀴의 오른쪽 부분으로 갱신
                        turn_right(gear[i]) #톱니바퀴를 돌린다.
                        right_flag = True #시계 방향으로 회전했다고 체크
                
        elif g_no == 1:
            for i in range(g_no,4):
                if gear[i][6] == right:
                    break
                else:
                    if right_flag:
                        right = gear[i][2]
                        turn_left(gear[i])
                        right_flag = False
                    else:
                        right = gear[i][2]
                        turn_right(gear[i])
                        right_flag = True

        else:
            for i in range(g_no-2,-1,-1):
                if gear[i][2] == left: #맞닿은 부분이 같을 때
                    break
                else:
                    if left_flag:
                        left = gear[i][6]
                        turn_left(gear[i])
                        left_flag = False
                    else:
                        left = gear[i][6]
                        turn_right(gear[i])
                        left_flag = True

    else: #반시계방향 회전
        left = gear[g_no-1][6]
        right = gear[g_no-1][2]
        turn_left(gear[g_no-1]) #고른 톱니바퀴는 회전
        left_flag = False
        right_flag = False
        if g_no == 2 or g_no == 3:
            for i in range(g_no-2,-1,-1):
                if gear[i][2] == left: #맞닿은 부분이 같을 때
                    break
                else:
                    if left_flag == False:
                        left = gear[i][6]
                        turn_right(gear[i])
                        left_flag = True
                    else:
                        left = gear[i][6]
                        turn_left(gear[i])
                        left_flag = False
                
            for i in range(g_no,4):
                if gear[i][6] == right:
                    break
                else:
                    if right_flag == False:
                        right = gear[i][2]
                        turn_right(gear[i])
                        right_flag = True
                    else:
                        right = gear[i][2]
                        turn_left(gear[i])
                        right_flag = False
                
        elif g_no == 1:
            for i in range(g_no,4):
                if gear[i][6] == right:
                    break
                else:
                    if right_flag == False:
                        right = gear[i][2]
                        turn_right(gear[i])
                        right_flag = True
                    else:
                        right = gear[i][2]
                        turn_left(gear[i])
                        right_flag = False

        else:
            for i in range(g_no-2,-1,-1):
                if gear[i][2] == left: #맞닿은 부분이 같을 때
                    break
                else:
                    if left_flag == False:
                        left = gear[i][6]
                        turn_right(gear[i])
                        left_flag = True
                    else:
                        left = gear[i][6]
                        turn_left(gear[i])
                        left_flag = False

if gear[0][0] == 0:
    ans += 0
else:
    ans += 1

if gear[1][0] == 0:
    ans += 0
else:
    ans += 2


if gear[2][0] == 0:
    ans += 0
else:
    ans += 4

if gear[3][0] == 0:
    ans += 0
else:
    ans += 8


print(ans)

#print()
#for i in range(4):
#    print(" ".join(map(str,gear[i])))
