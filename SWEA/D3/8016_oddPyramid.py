t = int(input())

for test_case in range(1,t+1):
    n = int(input())
    board = [[] for _ in range(n)]

    num = 1

    for i in range(n):
        cnt = 0
        while True:
            if num % 2 == 1:
                board[i].append(num)
                cnt += 1
            num += 1
            if cnt == ((i+1) * 2) -1:
                break

    print("#{} {} {}".format(test_case, board[n-1][0], board[n-1][-1]))

