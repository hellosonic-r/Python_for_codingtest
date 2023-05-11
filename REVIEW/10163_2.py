n = int(input()) #색종이 개수
board = [[0] * 1001 for _ in range(1001)]

for num in range(1,n+1):
    sx,sy,w,h = map(int, input().split())
    #슬라이싱으로 하니까 100점
    for i in range(sy, sy+h):
        board[i][sx:sx+w] = [num] * w

for num in range(1,n+1):
    cnt = 0
    for i in range(1001):
        cnt += board[i].count(num)
    print(cnt)