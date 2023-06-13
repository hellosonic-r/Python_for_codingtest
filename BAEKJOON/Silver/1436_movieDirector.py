n = int(input())
cnt = 0
title = 666 #영화제목(1번째 시리즈는 666)

#영화제목을 1씩 증가시켜주면서 666이 포함되었는지 확인하는 반복문
while True:
    if "666" in str(title): #영화제목에 666이 포함되어 있다면
        cnt += 1 #시리즈 카운트
    title += 1 #영화제목을 1증가하면서 666이 포함되었는지 확인
    if cnt == n: #만약 n번째 시리즈라면
        break #반복문 탈출

print(title-1) #영화제목 출력