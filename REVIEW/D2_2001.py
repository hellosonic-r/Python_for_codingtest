t = int(input())

for test_case in range(1,t+1):
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    max_ans = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            fly = 0 
            for k in range(m):
                fly += sum(board[i+k][j:j+m])
            if max_ans < fly:
                max_ans = fly

    print("#{} {}".format(test_case, max_ans))
            
