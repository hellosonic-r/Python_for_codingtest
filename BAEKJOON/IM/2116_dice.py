n = int(input())
dice_list = []

for i in range(n):
    dice_list.append(list(map(int, input().split())))
    # [[2 3 1 6 5 4],[3 1 2 4 6 5],[5 6 4 1 3 2],[1 3 6 2 4 5],[4 1 6 5 2 3]]

result = []
dice_sum = 0
#첫 번째 주사위를 어떻게 두느냐에 따라 위에 놓이는 주사위들의 최대 눈금이 정해진다.
def dice(first): #첫 번째 주사위의 윗면 인덱스
    global dice_sum 
    dice_sum = 0
    if first == 0: #첫 번째 주사위의 윗면 인덱스가 0 일 때
        up = 0
        #첫 번째 주사위의 윗면 인덱스가 0일 때, 아랫면 인덱스는 5이다. 
        #따라서, 위아랫면을 제외한 나머지 인덱스 1,2,3,4 중 가장 큰 숫자를 저장한다.
        dice_sum = max(dice_list[0][1],dice_list[0][2],dice_list[0][3],dice_list[0][4])
    elif first == 1:
        up = 1
        dice_sum = max(dice_list[0][0],dice_list[0][2],dice_list[0][4],dice_list[0][5])
    elif first == 2:
        up = 2
        dice_sum = max(dice_list[0][0],dice_list[0][1],dice_list[0][3],dice_list[0][5])
    elif first == 3:
        up = 3 
        dice_sum = max(dice_list[0][0],dice_list[0][2],dice_list[0][4],dice_list[0][5])
    elif first == 4:
        up = 4
        dice_sum = max(dice_list[0][0],dice_list[0][1],dice_list[0][3],dice_list[0][5])
    else:
        up = 5
        dice_sum = max(dice_list[0][1],dice_list[0][2],dice_list[0][3],dice_list[0][4])
    #두 번째 주사위 부터의 옆면 숫자들의 합  
    for i in range(0,n-1): 
        for j in range(6):
            #첫 번째 주사위의 윗면과 닿는 두 번째 주사위의 인덱스 j를 찾는다.
            if dice_list[i][up] == dice_list[i+1][j]:
                #j가 0 일때,
                if j == 0:
                    #두 번째 주사위의 윗면은 5가 된다.
                    up = 5
                    #그리고, 위아랫면의 인덱스를 제외한 나머지 숫자 중 가장 큰 수를 dice_sum에 저장한다.
                    dice_sum += max(dice_list[i+1][1],dice_list[i+1][2],\
                                    dice_list[i+1][3],dice_list[i+1][4])
                    break #만약 j를 찾는다면 j를 찾는 반복문을 탈출하고, 
                          #세 번째 주사위와 두 번째 주사위가 만나는 인덱스를 찾는다. (i = 1)
                elif j == 1:
                    up = 3
                    dice_sum += max(dice_list[i+1][0],dice_list[i+1][2],\
                                    dice_list[i+1][4],dice_list[i+1][5])
                    break
                elif j == 2:
                    up = 4
                    dice_sum += max(dice_list[i+1][0],dice_list[i+1][1],\
                                    dice_list[i+1][3],dice_list[i+1][5])
                    break
                elif j == 3:
                    up = 1
                    dice_sum += max(dice_list[i+1][0],dice_list[i+1][2],\
                                    dice_list[i+1][4],dice_list[i+1][5])
                    break
                elif j == 4:
                    up = 2
                    dice_sum += max(dice_list[i+1][0],dice_list[i+1][1],\
                                    dice_list[i+1][3],dice_list[i+1][5])
                    break       
                elif j == 5:
                    up = 0
                    dice_sum += max(dice_list[i+1][1],dice_list[i+1][2],\
                                    dice_list[i+1][3],dice_list[i+1][4])
                    break
    result.append(dice_sum)

#첫 번째 주사위의 윗면이 인덱스 0~5 일때의 옆면 숫자의 합을 result 리스트에 저장한다.
for i in range(6):
    dice(i)

#옆면 숫자의 합 중 가장 큰 값을 출력한다.
print(max(result))




# #############다른 코드###
# n = int(input())
# dice = []
# for _ in range(n):
#     dice.append(list(map(int, input().split())))
# rotate = {0:5, 1:3, 2:4, 3:1, 4:2, 5:0} #주사위 아랫면에 따른 윗면 로테이션 등록

# maxnum = 0 #최댓값을 저장해둘 변수 선언
# for i in range(6): #첫 번째 주사위를 기준으로 1~6까지 모두 순회
#     result = [] #각 주사위마다 옆면의 최댓값 1개를 저장해둘 리스트 선언
#     temp = [1,2,3,4,5,6] # 주사위 각 면에 써져있는 1~6
#     temp.remove(dice[0][i]) #주사위 아랫면의 숫자 제거
#     next = dice[0][rotate[i]] #첫 번째 주사위의 윗면 값 계산
#     temp.remove(next)
#     result.append(max(temp)) #첫 번째 주사위의 옆면들 중 가장 큰 값 삽입 
#     for j in range(1,n): #두 번째 주사위부터 마지막 주사위 까지 반복
#         temp = [1,2,3,4,5,6]
#         temp.remove(next) #현재 주사위의 아랫면 숫자 제거
#         next = dice[j][rotate[dice[j].index(next)]] #현재 주사위의 윗면 계산
#         temp.remove(next) #현재 주사위의 윗면 삭제
#         result.append(max(temp))
#     result = sum(result)
#     if maxnum < result:
#         maxnum = result
# print(maxnum)