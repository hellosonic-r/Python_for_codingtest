# def dfs(c, v):
#     global ans
#     ans = max(ans, len(v))
#     for n in num_list[c]:
#         if n not in v:
#             dfs(n, v+[n])
            
# t = int(input())
# for test_case in range(1,t+1):
#     n,m = map(int, input().split())
#     num_list = [[] for _ in range(n+1)]
#     for _ in range(m):
#         x, y = map(int, input().split())
#         if y not in num_list[x]:
#             num_list[x].append(y)
#         if x not in num_list[y]:
#             num_list[y].append(x)
#     ans = 0
            
#     for s in range(1, n+1):
#         dfs(s, [s]) 
            
#     print("#{} {}".format(test_case, ans))


##다시 풀어보기
def dfs(s, temp_list):
    global ans
    ans = max(ans, len(temp_list))
    for i in graph[s]:
        if visited[i] == 0:
            visited[i] = 1
            dfs(i, temp_list+[i])

t = int(input())
for test_case in range(1, t+1):
    n,m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
    visited = [0] * (n+1)
    
    ans = 0
    for s in range(1, n+1):
        dfs(s, [s])
        
    print(ans)