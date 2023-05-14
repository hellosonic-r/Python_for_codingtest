t = int(input())
for test_case in range(1, t+1):
    n, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(n):
        gc = 0
        for j in range(n):
            if board[i][j] == 1:
                gc += 1
            else:
                if gc == k:
                    ans += 1
                gc = 0
            if j == n-1:
                if gc == k:
                    ans += 1
        
    for i in range(n):
        sc = 0
        for j in range(n):
            if board[j][i] == 1:
                sc += 1
            else:
                if sc == k:
                    ans += 1
                sc = 0
            if j == n-1:
                if sc == k:
                    ans += 1
    print("#{} {}".format(test_case, ans))
