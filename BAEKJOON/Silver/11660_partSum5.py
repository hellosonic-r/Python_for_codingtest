##이렇게 풀면 답 이상하게 나옴

# n, m = map(int, input().split())

# board = [list(map(int, input().split())) for _ in range(n)]

# dp = [[0] * (n+1) for _ in range(n)]

# temp = 0 # 1

# for i in range(n): #0,1,2,3
#     dp[i][0] = temp
#     for j in range(1,n+1): #1,2,3,4
#         dp[i][j] = dp[i][j-1] + board[i][j-1]
#     temp = dp[i][-1]

# for i in range(n):
#     print(" ".join(map(str, dp[i])))


# # for _ in range(n):
# #     x1,y1,x2,y2 = map(int, input().split())
# #     print(dp[x2-1][y2] - dp[x1-1][y1])



# ##입력값마다 dp테이블 따로 만들기 >> 시간초과
# import sys

# n, m = map(int, sys.stdin.readline().split())

# board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# for _ in range(m):
#     x1,y1,x2,y2 = map(int, sys.stdin.readline().split())
#     garo = y2-y1+1 #3
#     sero = x2-x1+1 #2
#     dp = [[0] * (garo+1) for _ in range(sero)] # 2줄짜리
#     temp = 0
#     for i in range(sero): #0,1
#         dp[i][0] = temp
#         for j in range(1,garo+1): #1,2,3
#             dp[i][j] = dp[i][j-1] + board[x1-1+i][y1-1+j-1] #board[0][0]
#         temp = dp[i][-1]
    
#     print(dp[-1][-1])
    


import sys

n, m = map(int, sys.stdin.readline().split())

board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dp = [[0]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + board[i-1][j-1]

answer = 0
for _ in range(m):
    x1,y1,x2,y2 = map(int, sys.stdin.readline().split())
    answer = dp[x2][y2]-(dp[x2][y1-1] + dp[x1-1][y2] - dp[x1-1][y1-1]) 
    print(answer)