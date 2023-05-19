t = int(input())
for test_case in range(1,t+1):
    n = int(input())
    num_list = list(map(int, input().split()))
    avg = sum(num_list) / n

    ans = 0
    for num in num_list:
        if num <= avg:
            ans += 1

    print("#{} {}".format(test_case, ans))