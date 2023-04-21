t = int(input())
for test_case in range(1,t+1):
    p, q, r, s, w = map(int, input().split())
    a = p*w
    if w <= r:
        b = q
    else:
        b = q + (w-r) * s
    print("#{} {}".format(test_case, min(a,b)))
    