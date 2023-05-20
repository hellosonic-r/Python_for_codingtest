n = int(input())
board = [[0] * 1001 for _ in range(1001)]

paper = []
for _ in range(n):
    paper.append(list(map(int, input().split())))

num = 0
for x,y,w,h in paper:
    num += 1
    for i in range(y, y+h):
        board[i][x:x+w] = [num] * w

ans = []

for k in range(1, n+1):
    result = 0
    for i in range(1001):
        result += board[i].count(k)
    ans.append(result)

for i in ans:
    print(i)


