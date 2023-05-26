# ##메모리초과
# def dfs(count, pick, temp_sum):
#     if count == n-1:
#         result.append(temp_sum)
#         return
#     for i in (pick, pick+1):
#         dfs(count+1, i, temp_sum+board[count+1][i])

# n = int(input())

# board = []

# for _ in range(n):
#     board.append(list(map(int, input().split())))

# result = []
# dfs(0,0,board[0][0])
# print(max(result))


##dp
n = int(input())
d = []
for _ in range(n):
    d.append(list(map(int, input().split())))

for i in range(1,n):
    for j in range(len(d[i])):
        if j == 0:
            d[i][j] = d[i][j] + d[i-1][j]
        elif j == len(d[i])-1:
            d[i][j] = d[i][j] + d[i-1][j-1]
        else:
            d[i][j] = d[i][j] + max(d[i-1][j], d[i-1][j-1])

print(max(d[n-1]))