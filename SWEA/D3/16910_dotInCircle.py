t = int(input())
for test_case in range(1, t+1):
    n = int(input()) #반지름
    ans = 0
    for i in range(-n, n+1):
        for j in range(-n, n+1):
            if i**2 + j**2 <= n**2:
                ans += 1
    print("#{} {}".format(test_case, ans))
                