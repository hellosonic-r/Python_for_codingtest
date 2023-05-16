n = int(input())
num_list = [0] + list(map(int, input().split()))
dp = [0] * (n+1) #dp테이블에 연속된 수들의 합 저장(만약 연속된 수들의 합이 음수라면 0 저장)

ans = 0

for i in range(1, n+1): #dp테이블 채우기
    dp[i] = dp[i-1] + num_list[i] #dp[i](현재 인덱스)는 이전까지 저장된 합(dp[i-1] + 현재숫자(num_list[i])
    if dp[i] < 0: #만약 연속된 수들의 합이 음수가 된다면
        dp[i] = 0 #음수말고 그냥 안더하는 걸 선택. 0으로 갱신

if max(num_list[1:]) < 0: #수열들이 음수로만 구성되어 있다면,
    ans = max(num_list[1:]) #그냥 안더해보고, 수열들 중 가장 큰 값이 정답
else:
    ans = max(dp)

print(ans)