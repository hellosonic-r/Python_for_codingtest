t = int(input())

for test_case in range(1, t+1):
    n = int(input())
    num_list = list(range(1, n+1))
    
    ans = 0
    for i in num_list:
        if i % 2 == 1:
            ans += i
        else:
            ans -= i
            
    print("#{} {}".format(test_case, ans))
    
    