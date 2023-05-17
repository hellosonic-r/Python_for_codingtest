t = int(input())
for test_case in range(1, t+1):
    n, m = map(int, input().split())
    pw = { "0001101":0, "0011001":1, "0010011":2, "0111101":3, "0100011":4, "0110001":5, "0101111":6, "0111011":7, "0110111":8, "0001011":9 }
    board = [list(map(int, input())) for _ in range(n)]
    result = []
    ans = 0
    for i in range(n):
        temp_list = []
        for j in range(m-56+1):
            temp_list = board[i][j:j+56]
            for k in range(8): #0,1,2,3,4,5,6,7
                small_temp = temp_list[7*k:7*k+7]
                if ("".join(map(str, small_temp))) in pw:
                    result.append(pw["".join(map(str, small_temp))])
                else:
                    result = []
                    break
                
            if len(result) == 8:
                break
        if len(result) == 8:
            break

    h_sum = 0
    j_sum = 0
    for i in range(len(result)):
        if i%2 == 0:
            h_sum += result[i]
        else:
            j_sum += result[i]
    if ((h_sum) * 3 + j_sum) % 10 == 0:
        ans = h_sum + j_sum
    print("#{} {}".format(test_case, ans))    



##다시 풀어보기
t = int(input())

for test_case in range(1,t+1):
    n, m = map(int, input().split()) #n:세로 m:가로
    d = {"0001101":0, "0011001":1, "0010011":2, "0111101":3, "0100011":4, "0110001":5, "0101111":6, "0111011":7, "0110111":8, "0001011":9}
    board = [list(map(int, input())) for _ in range(n)]

    ans = 0
    check = False
    for i in range(n):
        for j in range(m-1,-1,-1):
            if board[i][j] == 1:
                temp_list = board[i][j-55:j+1]
                check = True
                break
        if check:
            break

    result = []
    for i in range(8):
        small_list = temp_list[7*i:7*i+7]
        result.append(d["".join(map(str, small_list))])

    odd = 0
    even = 0
    for i in range(len(result)):
        if i % 2 == 0:
            odd += result[i]
        else:
            even += result[i]

    if (odd*3 + even) % 10 == 0:
        ans = sum(result)

    print("#{} {}".format(test_case, ans))
