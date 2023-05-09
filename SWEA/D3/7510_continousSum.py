t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    ans = 0
    for i in range(1,n+1): #1부터 수열 생성 ~ 자기자신 수열까지
        start = i #초기 값 = i
        temp_sum = 0 #수열의 합을 저장받을 임시 변수 생성
        while temp_sum <= n: #합이 n이하일 때까지
            temp_sum = temp_sum + start 
            start += 1 #수열에 들어갈 숫자를 1씩 증가
            if temp_sum == n: #만약 합이 n과 같아진다면
                ans += 1 #경우의 수 1 증가
                break 
    print("#{} {}".format(test_case, ans))
