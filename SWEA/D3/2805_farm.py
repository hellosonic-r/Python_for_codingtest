###한 번에 패스

t = int(input())

for test_case in range(1, t+1):
    n = int(input())
    farm = []
    for _ in range(n):
        farm.append(list(map(int, input())))
    ans = 0
    
    for i in range(n): 
        if i <= ((n-1)//2):
            start_idx = ((n-1)//2) - i
            end_idx = ((n-1)//2) + i  
            ans += sum(farm[i][start_idx:end_idx+1])
        elif i > ((n-1)//2):
            start_idx = ((n-1)//2) - (n-1-i) 
            end_idx = ((n-1)//2) + (n-1-i)
            ans += sum(farm[i][start_idx:end_idx+1])
    print("#{} {}".format(test_case, ans))
            