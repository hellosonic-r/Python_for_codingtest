# ##TC 10/23
# t = int(input())
# for test_case in range(1,t+1):
#     n, m = map(int, input().split()) #n:주차공간개수 m:차량대수
#     park = [] #2 3 5
#     weight = [] #2 1 3 8
#     for _ in range(n):
#         park.append(int(input()))
#     for _ in range(m):
#         weight.append(int(input()))
    
#     command = []
#     for _ in range(2*m):
#         command.append(int(input()))

#     ans = 0
#     v = [0] * n
#     wait = []
#     count = 0

#     for i in command:
#         if i > 0: #차량 들어올때
#             if count < n: #주차장을 초과 안했다면
#                 for j in range(len(v)):
#                     if v[j] == 0:
#                         v[j] = weight[i-1]
#                         break
#                 count += 1
#             else: #주차장을 초과 했다면
#                 wait.append(weight[i-1])
#         else:
#             i = abs(i)
#             ans += (park[v.index(weight[i-1])] * weight[i-1])
#             v[v.index(weight[i-1])] = 0
#             count -= 1
            
#             if wait:
#                 next_car = wait.pop(0)
#                 for k in range(len(v)):
#                     if v[k] == 0:
#                         v[k] = next_car
#                         break
#                 count += 1
            
#     print("#{} {}".format(test_case, ans))


##
t = int(input())

for test_case in range(1,t+1):
    n,m = map(int, input().split()) #n:주차공간개수 m:차량의개수
    park = []
    for _ in range(n):
        park.append(int(input()))
    weight = [0]
    for _ in range(m):
        weight.append(int(input()))
    command = []
    for _ in range(2*m):
        command.append(int(input()))

    v = [0] * n
    wait = []
    ans = 0

    for i in command:
        if i > 0: #차량이 들어올 때
            for j in range(len(v)):
                if v[j] == 0:
                    v[j] = i
                    break
            else:
                wait.append(i)

        else: #차량이 나갈 때
            i = abs(i)
            for j in range(len(v)):
                if v[j] == i:
                    v[j] = 0
                    ans += (park[j] * weight[i])
                    parking = j
                    break
            if wait:
                v[parking] = wait.pop(0)
    print("#{} {}".format(test_case, ans))



