n = int(input())

dp = [0] * (n+1)

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1 # 1로 더하는 경우 (dp[i-1] + 1) -> dp의 값에는 최소값이 저장되기 때문에 가
    if i % 2 == 0: #2로 나누어 떨어지는 경우
        dp[i] = min(dp[i], dp[i//2] + 1) #dp[i//2]에 저장된 값+1 과 dp[i](1로 더하는 경우) 비교
    if i % 3 == 0: #3으로 나누어 떨어지는 경우
        dp[i] = min(dp[i], dp[i//3] + 1) #dp[i//3]에 저장된 값+1 과 dp[i](1로 더하는 경우) 비교

print(dp[n])