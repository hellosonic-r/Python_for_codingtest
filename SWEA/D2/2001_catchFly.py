t = int(input())
for test_case in range(1, t+1):
    n, m = map(int, input().split())
    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))
    
    ans = []
    
    for i in range(n-m+1):
        for j in range(n-m+1):
            temp_ans = 0
            for k in range(m):
                temp_ans += sum(board[i+k][j:j+m])
            ans.append(temp_ans)
    
    print("#{} {}".format(test_case, max(ans)))
                
            
            
        
        