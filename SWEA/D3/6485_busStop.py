t = int(input())
for test_case in range(1,t+1):
    n = int(input())
    bus_stop = []
    for _ in range(n):
        a, b = map(int, input().split())
        bus_stop.append((a,b))
    p = int(input())
    ans = []
    for _ in range(p):
        bus = int(input())
        cnt = 0
        for (a,b) in bus_stop:
            if a<=bus<=b:
                cnt += 1
        ans.append(cnt)
    print("#{} {}".format(test_case, " ".join(map(str, ans))))
                
        