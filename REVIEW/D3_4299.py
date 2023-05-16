t = int(input())
for test_case in range(1, t+1):
    d, h, m = map(int, input().split())
    ans = (d*24*60 + h*60 + m) - (11*24*60 + 11*60 + 11)

    if ans < 0:
        ans = -1

    print("#{} {}".format(test_case, ans)) 