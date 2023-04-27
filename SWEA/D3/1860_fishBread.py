##while문 시간초과
t = int(input())
for test_case in range(1,t+1):
    n,m,k = map(int, input().split())
    customers = list(map(int, input().split()))
    customers.sort()
    total = 0
    time = 0
    i = 0
    ans = 1
    while True:
        if i == n:
            break
        time += 1
        if time % m == 0:
            total += k
        if time == customers[i]:
            if total >= 1:
                total -= 1
                i += 1
            else:
                ans = -1
                break
                
    if ans == 1:
        print("#{} {}".format(test_case, "Possible"))
    else:
        print("#{} {}".format(test_case, "Impossible"))

##for문으로 해결
t = int(input())
for test_case in range(1,t+1):
    n,m,k = map(int, input().split())
    customers = list(map(int, input().split()))
    customers.sort()
    max_time = max(customers)
    
    total = 0
    i = 0 
    ans = 1
    for time in range(0, max_time+1):
        if time != 0 and time % m == 0:
            total += k
        if time == customers[i]:
            if total >= 1:
                total -= 1
                i+=1
            else:
                ans = -1
                break
                
    if ans == 1:
        print("#{} {}".format(test_case, "Possible"))
    else:
        print("#{} {}".format(test_case, "Impossible"))
      
                
        
        
        