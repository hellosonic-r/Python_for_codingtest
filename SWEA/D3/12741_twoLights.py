t = int(input())
board = []
for test_case in range(1, t+1):
    board.append(list(map(int, input().split())))

cnt = 1
for (a,b,c,d) in board:
    v = [0] * 101
    for i in range(a,b):
        v[i] += 1
    for j in range(c,d):
        v[j] += 1
    
    ans = v.count(2)
    
    print("#{} {}".format(cnt, ans))
    cnt += 1


