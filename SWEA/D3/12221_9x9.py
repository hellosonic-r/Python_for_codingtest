t = int(input())
for test_case in range(1,t+1):
    a, b = map(int, input().split())
    ans = a * b
    if a>=10 or b>=10:
        ans = -1

    print("#{} {}".format(test_case, ans))