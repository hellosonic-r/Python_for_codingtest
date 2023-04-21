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
                
            
##다시 풀어보기
t = int(input())
for test_case in range(1, t+1):
    n, m = map(int, input().split()) #n:가로세로 m:파리채 크기
    board = []
    #전체 보드를 채운다.
    for _ in range(n):
        board.append(list(map(int, input().split())))
    catch = []
    #파리채의 크기에 따라 for문의 범위가 달라진다.
    for i in range(n-m+1):
        for j in range(n-m+1):
            temp_catch = 0
            #파리채를 내리쳤을 때 시작 좌표를 기준으로
            #파리채의 크기에 해당하는 보드의 숫자들을 더해준다.
            for k in range(m):
                #가로에 해당하게 된다. 
                #for문이 m-1번 반복되면서 자연히 세로도 더해줄 수 있다.
                temp_catch += sum(board[i+k][j:j+m]) 
            catch.append(temp_catch)

    print("#{} {}".format(test_case, max(catch)))