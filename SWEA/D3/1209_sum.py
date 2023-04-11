### 한 번에 패스, input.txt 잘보기 
for test_case in range(1, 11):
    num = int(input())
    arr = []
    for _ in range(100):
        arr.append(list(map(int, input().split())))
    up = 0
    down = 0
    garo = 0
    sero_max = 0

    for i in range(100):
        garo = max(garo, sum(arr[i]))
        sero = 0
        for j in range(100):
            if i == j:
                up += arr[i][j]
            if i == 99-j: 
                down += arr[i][j]
            sero += arr[j][i] 
        if sero > sero_max:
            sero_max = sero
   
    print("#{} {}".format(test_case, max(up, down, garo, sero_max)))
                