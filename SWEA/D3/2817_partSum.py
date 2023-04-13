###실패코드 - 돌아가지를 못한다
def dfs(index):
    global temp_sum
    if temp_sum == k:
        result.append(temp_sum)
        return
    if temp_sum > k:
        return
    if index == n:
        return
    temp_sum += a[index]
    dfs(index+1)
    

t = int(input())

for test_case in range(1, t+1):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    result=[]
    temp_sum = 0
    dfs(0)
    print(result)
    print("#{} {}".format(test_case, len(result)))
    
    