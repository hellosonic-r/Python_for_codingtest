def dfs(count, num, result):
    global a
    if count == r:
        a = result
        return
    result = result*num
    dfs(count+1, num-1, result)
    
def dfs2(num, result):
    global b
    if num == 0:
        b = result
        return
    result = result * num
    dfs2(num-1, result)

t = int(input())
for test_case in range(1, t+1):
    n,r = map(int, input().split())
    a = 0
    b = 0
    dfs(0,n,1)
    dfs2(r, 1)
    
    print("#{} {}".format(test_case, int(a//b) % 1234567891))
    