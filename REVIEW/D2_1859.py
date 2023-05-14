t = int(input())
for test_case in range(1,t+1):
    n = int(input())
    num_list = list(map(int, input().split()))
    ans = 0
    sell = num_list[-1]
    for i in range(n-1, -1, -1):
        if num_list[i] <= sell:
            ans += (sell - num_list[i])
        else:
            sell = num_list[i]

    print("#{} {}".format(test_case, ans))