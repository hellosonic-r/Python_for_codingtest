# #컨베이어, 로봇 위치 회전
# def rotate():
#     x = a.pop()
#     y = b.pop(0)
#     a.insert(0,y)
#     b.append(x)

#     r = robot.pop()
#     robot.insert(0, r)

# #로봇 이동 
# def move():
#     for i in range(n-1,0,-1): #3 , 2, 1 #맨 끝에서부터
#         if robot[i] == 0 and a[i] >= 1: #로봇이 없고, 내구도가 1 이상이면
#             if robot[i-1] == 1: #이전 칸에 로봇이 있다면
#                 robot[i] += 1 #현재 칸에 로봇 +1
#                 a[i] -= 1 #내구도 1 감소
#                 robot[i-1] -= 1 #이전 칸 로봇이 현재 칸으로 이동한 것이므로 이전 칸 로봇 -1
#             else:
#                 continue
#         else:
#             continue

# n, k = map(int,input().split())
# total = list(map(int, input().split()))
# a = total[:len(total)//2]
# b_r = total[len(total)//2:]
# b = b_r[::-1] #거꾸로 입력받아야함
# robot = [0] * n

# time = 0

# while True:
#     time += 1
#     rotate() #로봇과 함께 한칸 회전
#     if robot[-1] == 1: #만약 로봇이 마지막 칸에 있으면
#         robot[-1] = 0 #내린다.
#     move() #로봇이 이동한다.
#     if robot[-1] == 1: #만약 로봇이 마지막 칸에 있으면
#         robot[-1] = 0 #내린다.

#     if a[0] != 0: #첫 번째 칸(올리는 위치)의 내구도가 0이 아니면
#         robot[0] += 1 #로봇을 올린다.
#         a[0] -= 1 #내구도는 1 감소한다.

#     # print(time,"단계 : ")
#     # print("로봇위치 :",robot)
#     # print(a)
#     # print(b)
#     # print()

#     if a.count(0) + b.count(0) >= k:
#         break

# print(time)



from collections import deque

n, k = map(int, input().split())
belt = deque(list(map(int, input().split())))
robot = deque([0]*n)
ans = 0

while True:
    belt.rotate(1) #한 칸씩 회전
    robot.rotate(1) #한 칸씩 회전
    robot[-1] = 0 #내리는 위치에 있는 로봇 내리기
    if sum(robot): #로봇이 존재한다면,
        for i in range(n-2, -1, -1): #로봇 내려가는 부분 i-1 인덱스 이므로 그 전인 i-2부터
            if robot[i] == 1 and robot[i+1] == 0 and belt[i+1] >= 1:
                robot[i+1] = 1
                robot[i] = 0
                belt[i+1] -= 1
        robot[-1] = 0 #내리는 위치에 로봇이 생기면 그 즉시 무조건 내려야 함
    if robot[0] == 0 and belt[0] >= 1: #올리는 위치에 로봇이 없고 내구도가 1 이상이면
        robot[0] = 1
        belt[0] -= 1
    ans += 1

    if belt.count(0) >= k:
        break

print(ans)
