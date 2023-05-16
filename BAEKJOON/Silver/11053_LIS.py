n = int(input())
num_list = [0] + list(map(int, input().split()))

dp = [0] * (n+1)

for i in range(n+1): #dp 테이블 채우기
    mx = 0
    for j in range(i): #dp 처음 인덱스부터 현재 인덱스-1 까지 값 비교
        if num_list[i] > num_list[j]: #만약 작은 숫자라면,
            mx = max(mx, dp[j]) #최대값을 찾는다
            dp[i] = mx + 1 #찾은 최대값에서 +1 해준 것이 dp[i] 값

print(max(dp))
