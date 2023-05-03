#1: 스위치 켜져있음 0:꺼져있음
#남 : 스위치 번호가 자기가 받은 수의 배수이면, 그 스위치 상태 바꿈
#    3 받으면 3,6 스위치 바꿈
#여 : 자기가 받은 수와 좌우 대칭 스위치 상태 바꿈 (항상 홀수)

n = int(input())
switch = [-1] + list(map(int ,input().split()))

total = int(input()) #사람 수
for _ in range(total):
    sex, num = map(int, input().split())
    if sex == 1:
        for i in range(1, len(switch)): #1,2,3,,,
            if i % num == 0:
                switch[i] = abs(switch[i] - 1)
    elif sex == 2:
        switch[num] = abs(switch[num]-1)
        j = 1
        while True:
            if num-j == 0 or num+j == len(switch):
                break
            if switch[num-j] == switch[num+j]:
                switch[num-j] = abs(switch[num-j]-1)
                switch[num+j] = abs(switch[num+j]-1)
                j+=1 
            else:
                break

switch.pop(0)

for i in range(len(switch)):
    print(switch[i], end = " ")
    if (i+1) % 20 == 0:
        print()

            


