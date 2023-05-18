t = int(input())

for test_case in range(1,t+1):
    board = []
    for _ in range(5):
        board.append(list(map(str, input())))

    length = 0

    for i in range(len(board)):
        if len(board[i]) > length:
            length = len(board[i])

    for i in range(len(board)):
        if len(board[i]) == length:
            continue
        else:
            for j in range(length - len(board[i])):
                board[i].append("")

    ans = ""
    for i in range(length):
        for j in range(5):
            ans += board[j][i]

    print("#{} {}".format(test_case, ans))