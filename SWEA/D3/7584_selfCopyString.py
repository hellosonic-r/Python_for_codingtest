t = int(input())

for test_case in range(1,t+1):
    k = int(input()) #k번째 숫자 구하기 p[k-1]
    p = ["0"]
    i = 1
    while True:
        if k< len(p):
            break
        g_p = p[::-1]
        p.append("0")
        for j in g_p:
            if j == "0":
                p.append("1")
            elif j == "1":
                p.append("0")
        i+=1

    print("#{} {}".format(test_case, p[k-1]))