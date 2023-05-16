# ## TC 12/23 맞왜틀..
# t = int(input())
# for test_case in range(1, t+1):
#     n, m = map(int, input().split()) #n: 주차공간 개수 / m: 차량의 개수
#     parking_fee = []

#     for _ in range(n):
#         parking_fee.append(int(input())) #무게당 요금 [2,3,5]
#     car_weight = [0]
#     for _ in range(m):
#         car_weight.append(int(input())) #차량의 무게 Wi = [2,1,3,8]
        
#     v = [0] * n
#     ans = 0
#     cars = []
    
#     for _ in range(2*m):
#         car_idx = int(input())
#         if car_idx > 0: #양수 나올때
#             cars.append(car_weight[car_idx])
#             for i in range(n):
#                 if v[i] == 0:
#                     v[i] = car_idx
#                     ans += cars.pop(0) * parking_fee[i]
#                     break
                
#         else: #음수 나올때
#             for i in range(n):
#                 if v[i] == abs(car_idx):
#                     v[i] = 0
#                     if cars:
#                         ans += cars.pop(0) * parking_fee[i]
#                     break
                
#     print("#{} {}".format(test_case, ans))

        
##다시 풀어보자 -> 패스 : 리스트에 한번에 담고 하나씩 꺼내면서 하니까 맞았다
t = int(input())
for test_case in range(1, t+1):
    n, m = map(int, input().split())
    fee = []
    for _ in range(n):
        fee.append(int(input()))
    weight = [0]
    for _ in range(m):
        weight.append(int(input()))
    inout = []
    for _ in range(2*m):
        inout.append(int(input()))
    
    v = [0] * n
    wait = []
    ans = 0 

    while inout:
        car_idx = inout.pop(0)
        if car_idx > 0:
            for i in range(n):
                if v[i] == 0:
                    v[i] = car_idx
                    break
            else:
                wait.append(car_idx)

        else:
            car_idx = abs(car_idx)
            for i in range(n):
                if v[i] == car_idx:
                    v[i] = 0 
                    ans += weight[car_idx] * fee[i]
                    parking = i
                    break
            if wait:
                v[parking] = wait.pop(0)
    
    print(ans)
            

##다시 풀어보기
t = int(input())
for test_case in range(1,t+1):
    n, m = map(int, input().split()) #n:주차공간개수 m:차량의무게
    park = []
    for _ in range(n):
        park.append(int(input()))
    weight = [0]
    for _ in range(m):
        weight.append(int(input()))
    inout = []
    for _ in range(2*m):
        inout.append(int(input()))

    wait = [] #주차공간에 차가 가득 찼을 때 대기열 리스트
    v = [0] * n #주차공간에 차가 들어온 것을 표시하기 위한 리스트
    ans = 0

    for i in inout: #출입정보를 하나씩 살펴본다.
        if i > 0: #양수가 왔을 때,(i는 차량 무게 리스트의 인덱스가 된다)
            if v.count(0) == 0: #주차 공간이 가득 찼다면,
                wait.append(i) #대기열에 추가
            else: #주차공간이 가득 차지 않았다면,
                for j in range(len(v)):
                    if v[j] == 0: #빈 공간을 찾는다.
                        v[j] = i #인덱스를 표시한다.
                        break
        elif i < 0: #음수가 왔을 때,
            i = abs(i)
            for j in range(len(v)):
                if v[j] == i: #해당 차량이 나가야 한다.
                    ans += park[j]*weight[i] #요금을 계산한다.
                    if wait: #만약 대기열이 있다면
                        v[j] = wait.pop(0) #새로운 차량이 들어온다.
                    else: #대기열이 없다면
                        v[j] = 0 #주차공간이 비었다고 표시한다.
                    break

    print("#{} {}".format(test_case, ans))






