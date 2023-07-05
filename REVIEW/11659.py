import sys

n, m = map(int, input().split())
num_list = list(map(int, input().split()))
dp = [0] * (n+1)
for i in range(1,n+1):
    dp[i] = dp[i-1] + num_list[i-1]

for _ in range(m):
    start, end = map(int,sys.stdin.readline().split())
    print(dp[end]-dp[start-1])
    