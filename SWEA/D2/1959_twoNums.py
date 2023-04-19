def dfs(x,temp_list):
    if x == len(short_list):
        result.append((temp_list))
        return
    for i in range(len(long_list)):
        if visited[i] == 0:
            visited[i] = 1
            dfs(x+1,temp_list+[long_list[i]])
            visited[i] = 0

t = int(input())
for test_case in range(1,t+1):
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    if len(a_list) > len(b_list):
        long_list = a_list
        short_list = b_list
    else:
        long_list = b_list
        short_list = a_list
    visited = [0] * len(long_list)
    result = []
    dfs(0,[])
    
    max_ans = 0

    for check in result:
        ans = 0
        for i in range(len(short_list)):
            ans += check[i] * short_list[i]
        if max_ans < ans:
            max_ans = ans

    print(max_ans)
