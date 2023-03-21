# n, l = map(int, input().split())

# time = 0
# distance = 0
# for _ in range(n):
#     d, r, g = map(int, input().split())

#     time += (d - distance)
#     distance = d
#     if time % (r+g) <= r:
#         time += (r - (time % (r+g)))

# time += (l - distance)
# print(time)

n, l = map(int, input().split())
light = []

#신호등 정보를 리스트에 저장
for _ in range(n):
    light.append(list(map(int, input().split())))

#시간
time = 0
#이동한 거리
distance = 0
i = 0
while True:
    #시간이 1씩 경과
    time += 1
    #시간이 1씩 경과함에 따라 이동한 거리도 1씩 증가
    distance += 1
    #이동한 거리가 도로의 끝에 다다르면 반복문 탈출 
    if distance == l:
        break

    else: 
        #신호등이 저장된 리스트를 하나하나 살펴본다. i=0부터 시작
        if i < n:
            #이동한 거리에 신호등이 있다면
            if distance == light[i][0]:
                #시간을 빨간불+파란불 지속시간으로 나눈 것이 빨간불 지속시간보다 작거나 같으면,
                #아직 빨간불이라는 것, 즉 시간에 남은 빨간불 지속시간을 빼주면 된다.
                if time % (light[i][1] + light[i][2]) <= light[i][1]:
                    time += (light[i][1] - (time % (light[i][1] + light[i][2])))
                #만약 초록불인 상태라면 시간에 아무것도 더해주지 않는다.
                else:
                    time += 0
                #신호등을 살펴봤으므로 다음 신호등을 살펴보기 위해 i를 1 증가
                i += 1
print(time)
    