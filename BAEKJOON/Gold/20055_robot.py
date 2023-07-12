def rotate():
    x = a.pop()
    y = b.pop(0)
    a.insert(0,y)
    b.append(x)

    r = robot.pop()
    robot.insert(0, r)

def move():
    for i in range(n-1,0,-1): #3 , 2, 1
        if robot[i] == 0 and a[i] >= 1:
            if robot[i-1] == 1:
                robot[i] += 1 
                a[i] -= 1
                robot[i-1] -= 1
            else:
                continue
        else:
            continue


n, k = map(int,input().split())
total = list(map(int, input().split()))
a = total[:len(total)//2]
b_r = total[len(total)//2:]
b = b_r[::-1] #거꾸로 입력받아야함
robot = [0] * n

time = 0

while True:
    time += 1
    rotate() #로봇과 함께 한칸 회전
    if robot[-1] == 1:
        robot[-1] = 0
    move()
    if robot[-1] == 1:
        robot[-1] = 0

    if a[0] != 0:
        robot[0] += 1
        a[0] -= 1


    # print(time,"단계 : ")
    # print("로봇위치 :",robot)
    # print(a)
    # print(b)
    # print()

    if a.count(0) + b.count(0) >= k:
        break

print(time)