h, w = map(int, input().split())
area = []
for i in range(h):
    area.append(list(input()))
#구름 예보
result = [[0] * w for _ in range(h)]

cloud = 0 #구름 수
for i in range(h):
    cloud = 0 #구름 수 / 행이 바뀔때마다 0으로 초기화
    for j in range(w):
        #i,j에 현재 구름이 떠있다면
        if area[i][j] == "c": 
            result[i][j] = 0 #구름 예보 정보 값에 0 저장
            cloud += 1 #i행에 구름개수가 하나 있다는 것을 알려줌
            x = j #x는 현재 i행의 구름이 j번째에 있다는 것을 알려줌
        else: #구름이 없는 열에서.. 
            if cloud < 1: #만약 이전 열에서 카운트한 구름의 개수가 0 이라면
                #수 분이 지나도 구름이 올 확률이 없으므로 -1 저장
                result[i][j] = -1 
            else: #구름이 있다면,
                #현재 열에서 구름이 있는 열을 빼준다.
                result[i][j] = j-x 

for i in range(h):
    for j in range(w):
        print(result[i][j], end = " ")
    print()



# h,w = map(int, input().split())
# city = []
# answer = [[0]*w for i in range(h)]
# cloud = False
# for _ in range(h):
#     city.append(list(map(str, input())))
# for i in range(h):
#     if cloud == False and city[i][j] == '.':
#         answer[i][j] = -1
#     elif city[i][j] == 'c':
#         cloud=True
#         answer[i][j] = 0
#         num = 1 
#     elif cloud == True and city[i][j] == '.':
#         answer[i][j] = num
#         num += 1
#     cloud = False
#     num = 1
# for i in range(h):
#     for j in range(w):
#         print(answer[i][j], end = " ")
#     print()