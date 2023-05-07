##나의 코드
def dfs(a, count, result): #a:곱하려고 하는 숫자 count:곱하는 횟수 result:곱한 값
    global ans
    if count == m: #m번만큼 곱하면,
        ans = result #정답은 현재 저장된 곱한 값
        return #리턴
    result = result * a 
    dfs(a, count + 1, result) #다음 곱 수행
    
for test_case in range(1, 11):
    t = int(input())
    n, m = map(int, input().split())
    ans = 0
    dfs(n, 0, 1)
    print("#{} {}".format(test_case,ans))


##다른 코드
def dfs(n,m):
    if m == 0:
        return 1
    else:
        return n* dfs(n, m-1)
    
for test_case in range(1, 11):
    t = int(input())
    n, m = map(int, input().split())
    ans = dfs(n, m)
    print("#{} {}".format(test_case,ans))

