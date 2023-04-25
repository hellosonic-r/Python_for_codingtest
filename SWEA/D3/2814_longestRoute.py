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
#TC 5/10
def dfs(s, temp_list): #거쳐간 정점들이 담긴 temp_list를 dfs를 호출할때마다 넘겨준다.
    global ans
    ans = max(ans, len(temp_list)) #최대 정점 개수 갱신
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

    print("#{} {}".format(test_case, ans))
    

##visited 말고 dfs함수의 변수에 정점이 포함되어있는지 확인해야함
def dfs(s, temp_list): #방문한 노드가 담긴 temp_list를 dfs를 호출할때마다 넘겨준다.
    global ans
    ans = max(ans, len(temp_list)) #최대 노드 개수 갱신
    for i in graph[s]:
        if i not in temp_list: #방문한 노드와 연결된 다른 노드가 방문 안했는지 확인(이미 있다면 방문처리 된 것) 
            dfs(i, temp_list+[i])

t = int(input())
for test_case in range(1, t+1):
    n,m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
    
    ans = 0
    for s in range(1, n+1): #모든 노드를 확인 (시작하는 위치를 준다)
        dfs(s, [s])

    print("#{} {}".format(test_case, ans))