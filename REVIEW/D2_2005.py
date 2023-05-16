t = int(input())
for test_case in range(1,t+1):
    n = int(input())
    board = [[] for _ in range(n)]
    board[0].append(1) #i=0일때, 1
    i = 1 #i=1일때부터 시작
    while True:
        if i == n:
            break
        board[i].append(1) #맨 앞에 1 넣는다

        #규칙을 찾아 식 구현
        for j in range(1,i):
            board[i].append(board[i-1][j-1]+board[i-1][j])

        board[i].append(1) #맨 뒤에 1 넣는다
        i+=1 #다음 층으로

    print("#{}".format(test_case))
    for num in board:
        print(" ".join(map(str, num)))

