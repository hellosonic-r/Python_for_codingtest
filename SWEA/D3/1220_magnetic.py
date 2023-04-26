for test_case in range(1,11):
    n = int(input())
    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))
        
    count = 0
    for i in range(n):
        temp_list = [] #0을 제외하고 1,2가 연속으로 있는지 확인하기 위한 리스트
        for j in range(n):
            if board[j][i] == 1: #1일 때, 
                if temp_list: #temp_list에 혹시 값이 담겨있다면
                    temp_list.clear() #temp_list를 초기화시키고
                temp_list.append(1) #1을 추가
            if board[j][i] == 2: #2일 때,
                if temp_list: #temp_list에 값이 담겨 있다면 그건 1
                    count += 1 #1,2가 연속으로 있게됨
                    temp_list.clear() #clear
                else:
                    continue
    print("#{} {}".format(test_case, count))
                    