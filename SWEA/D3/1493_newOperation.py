##제한시간 초과

t = int(input())
for test_case in range(1,t+1):

    p, q = map(int, input().split())
    n = max(p,q)

    board = [[] for _ in range(2*n)]


    num = 1
    for k in range(0,((2*n-1)*2)+1):
        for i in range(2*n-1, -1, -1):
            for j in range(2*n):
                if i+j == k:
                    board[i].append(num)
                    num+=1
    a_p = []
    a_q = []
    for i in range(len(board)-1):
        for j in range(len(board)-1):
            if board[i][j] == p:
                a_p = [j+1, i+1]
            if board[i][j] == q:
                a_q = [j+1, i+1]

    pq = [a_p[0]+a_q[0], a_p[1]+a_q[1]]

    print("#{} {}".format(test_case, board[pq[1]-1][pq[0]-1]))
    


##다른 코드 - 대각선의 시작점과 끝점을 찾아서 해결
t = int(input())

for test_case in range(1, t+1):
    p,q = map(int, input().split())

    p_n = 0 #좌표(?,?)의 값 p는 p_n번째 대각선에 속한다.
    q_n = 0 #좌표(?,?)의 값 q는 q_n번째 대각선에 속한다.

    #각각 몇 번째 대각선에 속하는지 찾는다.
    while True:
        if 1+((p_n - 1) * p_n)//2 <= p <= (p_n * (p_n + 1))//2:
            break
        p_n += 1
    while True:
        if 1+((q_n - 1) * q_n)//2 <= q <= (q_n * (q_n + 1))//2:
            break
        q_n += 1

    #대각선이 시작하는 값에서 얼마만큼 떨어져있는지(p_d와 q_d) 찾는다.
    p_d = p - (1+((p_n - 1) * p_n)//2)
    q_d = q - (1+((q_n - 1) * q_n)//2)

    #얼마만큼 떨어져있는지 찾았다면, 값 p의 좌표를 구할 수 있다. (p_x, p_y)
    p_x = 1 + p_d
    p_y = p_n - p_d

    #얼마만큼 떨어져있는지 찾았다면, 값 q의 좌표를 구할 수 있다. (q_x, q_y)
    q_x = 1 + q_d
    q_y = q_n - q_d

    #문제 지시에 따라 x좌표는 x좌표끼리, y좌표는 y좌표끼리 더해서 새로운 좌표를 만든다.(new_x, new_y)
    new_x = p_x + q_x
    new_y = p_y + q_y

    new_n = new_x + new_y - 1 #새로운 좌표는 몇 번째 대각선에 속해있는지 찾는다. 
    new_start = 1+((new_n - 1)*new_n)//2 #대각선의 시작점을 찾는다. 

    ans = new_start + (new_x-1) #대각선에서 얼마만큼 떨어졌는지를 이용해서 답을 찾는다. 

    print("#{} {}".format(test_case, ans))
