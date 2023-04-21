t = int(input())

for test_case in range(1, t+1):
    n = int(input())
    num_list = list(map(int, input().split()))
    
    ans = 0
    price = 0
    max_price = 0
    #매매가를 역순으로 본다.
    for i in range(n-1, -1, -1): # 4 ~ 0 
        price = num_list[i]
        if max_price < price:
            max_price = price
        else:
            ans += (max_price - price)
            
    print("#{} {}".format(test_case, ans))


##다시 풀어보기
t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    num_list = list(map(int, input().split()))

    buy = 0
    max_price = 0
    for i in range(len(num_list)-1, -1, -1):
        if num_list[i] > max_price:
            max_price = num_list[i]
        else:
            buy += (max_price-num_list[i])

    print("#{} {}".format(test_case, buy))

