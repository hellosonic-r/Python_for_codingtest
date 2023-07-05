def dfs(count,x):
    if count == k:
        if v[x] == 1:
            result.append(x)
        return
    
    for i in lst[x]:
        if v[i] == 0:
            dfs(count+1, i)

n, m, k, x = map(int, input().split()) #n:도시의 개수 m:도로개수 k:거리정보 x:출발도시의 정보
lst = [[] for _ in range(n+1)]
for _ in range(m):
    start, end = map(int, input().split())
    lst[start].append(end)
v = [0] * (n+1)
result = []
v[x] = 1
dfs(0, x)
result.sort()
if result:
    for ans in result:
        print(ans)
else:
    print(-1)
