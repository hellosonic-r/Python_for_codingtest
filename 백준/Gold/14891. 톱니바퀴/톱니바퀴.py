def turn_right(arr): #시계방향 회전
    arr.insert(0,arr.pop())
    return

def turn_left(arr): #반시계방향 회전
    arr.append(arr.pop(0))
    return

gear = []
for _ in range(4):
    gear.append(list(map(int, str(input()))))

k = int(input()) #회전 횟수
board = []

for _ in range(k):
    board.append(list(map(int, input().split()))) #1: 시계 -1:반시계

ans = 0

while board:
    x = board.pop(0)
    g_no = x[0] #3입력 -> 실제로 인덱스는 2
    direction = x[1]
    left = 0
    right = 0
    if direction == 1: #시계방향 회전
        left = gear[g_no-1][6]
        right = gear[g_no-1][2]
        turn_right(gear[g_no-1]) #고른 톱니바퀴는 회전
        left_flag = True
        right_flag = True
        if g_no == 2 or g_no == 3:
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