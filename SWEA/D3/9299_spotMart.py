##백트래킹으로 풀이
def dfs(count, temp_list):
    if count == 2:
        if sum(temp_list) <= m:
            result.append(sum(temp_list))
        return
    if sum(temp_list) > m:
        return
    for i in range(n):
        if v[i] == 0:
            v[i] = 1
            dfs(count+1, temp_list + [num_list[i]])
            v[i] = 0
        
t = int(input())

for test_case in range(1, t+1):
    n, m = map(int, input().split()) #n: n개의 과자 m:제한무게
    num_list = list(map(int ,input().split()))
    result = []
    v = [0] * n

    dfs(0, [])
    if result:
        ans = max(result)
    else:
        ans = -1
    print("#{} {}".format(test_case, ans))



##단순 구현으로 풀기 - 2개뽑는거니까 2중for문 사용하면 됨
t = int(input())

for test_case in range(1, t+1):
    n, m = map(int ,input().split())
    num_list = list(map(int , input().split()))
    result = []
    for i in range(n-1):
        for j in range(i+1, n):
            if num_list[i] + num_list[j] <= m:
                result.append(num_list[i]+num_list[j])
    if result:
        ans = max(result)
    else:
        ans = - 1

    print("#{} {}".format(test_case, ans))
