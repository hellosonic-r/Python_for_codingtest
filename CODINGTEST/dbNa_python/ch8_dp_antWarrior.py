n = int(input())

num_list = list(map(int, input().split()))

dp = [0] * 100

dp[0] = num_list[0]
dp[1] = max(num_list[0], num_list[1])

for i in range(2, n):
    dp[i] = max(dp[i-1], dp[i-2] + num_list[i])


print(dp[n-1])