from collections import deque

def rectangle(sx,sy):
    cnt = 0
    if 0<=sx+1<m and 0<=sy+1<n:
        cnt += (board[sy][sx] + board[sy+1][sx] + board[sy][sx+1] + board[sy+1][sx+1])
        return cnt
    else:
        return 0
    
def garo_bar(sx,sy):
    cnt = 0
    if 0<=sx+3<m:
        cnt += (board[sy][sx] + board[sy][sx+1] + board[sy][sx+2] + board[sy][sx+3])
        return cnt
    else:
        return 0
    
def sero_bar(sx,sy):
    cnt = 0
    if 0<=sy+3<n:
        cnt += (board[sy][sx] + board[sy+1][sx] + board[sy+2][sx] + board[sy+3][sx])
        return cnt
    else:
        return 0

def L1(sx,sy):
    pilar = 0
    cnt1,cnt2,cnt3,cnt4 = 0,0,0,0
    if 0<=sy<n and 0<=sy+1<n and 0<=sy+2<n:
        pilar += (board[sy][sx] + board[sy+1][sx] + board[sy+2][sx]) 
        if 0<=sx+1<m:
            cnt1 += (pilar + (board[sy][sx+1]))
            cnt2 += (pilar + (board[sy+2][sx+1]))
        if 0<=sx-1<m:
            cnt3 += (pilar + (board[sy][sx-1]))
            cnt4 += (pilar + (board[sy+2][sx-1]))
        return max(cnt1,cnt2,cnt3,cnt4)
    else:
        return 0 
    
def L2(sx,sy):
    pilar = 0
    cnt1,cnt2,cnt3,cnt4 = 0,0,0,0
    if 0<=sx<m and 0<=sx+1<m and 0<=sx+2<m:
        pilar += (board[sy][sx] + board[sy][sx+1] + board[sy][sx+2])
        if 0<=sy+1<n:
            cnt1 += (pilar + (board[sy+1][sx]))
            cnt2 += (pilar + (board[sy+1][sx+2]))
        if 0<=sy-1<n:
            cnt3 += (pilar + (board[sy-1][sx]))
            cnt4 += (pilar + (board[sy-1][sx+2]))
        return max(cnt1,cnt2,cnt3,cnt4)
    else:
        return 0 

def zigzag1(sx,sy):
    pilar = 0 
    cnt1,cnt2,cnt3,cnt4 = 0,0,0,0
    if 0<=sy<n and 0<=sy+1<n:
        pilar += (board[sy][sx] + board[sy+1][sx])
        if 0<=sx-1<m and 0<=sy-1<n:
            cnt1 += (pilar + (board[sy][sx-1] + board[sy-1][sx-1]))
        if 0<=sx-1<m and 0<=sy+2<n:
            cnt2 += (pilar + (board[sy+1][sx-1] + board[sy+2][sx-1]))
        if 0<=sx+1<m and 0<=sy-1<n:
            cnt3 += (pilar + (board[sy-1][sx+1] + board[sy][sx+1]))
        if 0<=sx+1<m and 0<=sy+2<n:
            cnt4 += (pilar + (board[sy+1][sx+1]) + board[sy+2][sx+1])
        return max(cnt1,cnt2,cnt3,cnt4)
    else:
        return 0

def zigzag2(sx,sy):
    pilar = 0
    cnt1,cnt2,cnt3,cnt4 = 0,0,0,0
    if 0<=sx<m and 0<=sx+1<m:
        pilar += (board[sy][sx] + board[sy][sx+1])
        if 0<=sx-1<m and 0<=sy-1<n:
            cnt1 += (pilar + (board[sy-1][sx-1] + board[sy-1][sx]))
        if 0<=sx-1<m and 0<=sy+1<n:
            cnt2 += (pilar + (board[sy+1][sx-1] + board[sy+1][sx]))
        if 0<=sx+2<m and 0<=sy-1<n:
            cnt3 += (pilar + (board[sy-1][sx+1] + board[sy-1][sx+2]))
        if 0<=sx+2<m and 0<=sy+1<n:
            cnt4 += (pilar + (board[sy+1][sx+1] + board[sy+1][sx+2]))
        return max(cnt1,cnt2,cnt3,cnt4)
    else:
        return 0

def fuq1(sx,sy):
    pilar = 0
    cnt1,cnt2 = 0,0
    if 0<=sx+2<m and 0<=sy<n:
        pilar += (board[sy][sx] + board[sy][sx+1] + board[sy][sx+2])
        if 0<=sy-1<n:
            cnt1 += (pilar + board[sy-1][sx+1])
        if 0<=sy+1<n:
            cnt2 += (pilar + board[sy+1][sx+1])
        return max(cnt1,cnt2)
    else:
        return 0
    
def fuq2(sx,sy):
    pilar = 0
    cnt1,cnt2 = 0,0
    if 0<=sx<m and 0<=sy+2<n:
        pilar += (board[sy][sx] + board[sy+1][sx] + board[sy+2][sx])
        if 0<=sx-1<m:
            cnt1 += (pilar + board[sy+1][sx-1])
        if 0<=sx+1<m:
            cnt2 += (pilar + board[sy+1][sx+1])
        return max(cnt1,cnt2)
    else:
        return 0

n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

dx = [0,1,0,-1]
dy = [-1,0,1,0]

result = 0
for y in range(n):
    for x in range(m):
        result = max(result, max(rectangle(x,y), garo_bar(x,y), sero_bar(x,y), L1(x,y), L2(x,y), zigzag1(x,y), zigzag2(x,y), fuq1(x,y), fuq2(x,y)))

print(result)