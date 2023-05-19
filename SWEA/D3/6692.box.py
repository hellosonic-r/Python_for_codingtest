t = int(input())

for test_case in range(1, t+1):
    n = int(input())
    box = []
    for _ in range(n):
        box.append(list(map(float,input().split())))

    ans = 0
    for p,x in box:
        ans += (p*x)

    print("#{} {:.6f}".format(test_case, ans))