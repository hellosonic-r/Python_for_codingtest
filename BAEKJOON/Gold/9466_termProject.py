##시간초과

def dfs(sx,temp_list):
    v.append(sx)
    nx = num_list[sx]
    if nx == v[0]:
        temp_list = list(set(temp_list))
        team.append(temp_list)
        return True
    if nx != v[0] and nx in v:
        return False
    dfs(nx,temp_list + [nx] )

t = int(input())

for _ in range(t):
    n = int(input())
    num_list = [0] + list(map(int, input().split()))
    team = []
 
    for i in range(1, n+1):
        v = []
        dfs(i, [i])

    ans = []
    for i in team:
        for j in i:
            ans.append(j)

    ans = list(set(ans))
            
    print(n - len(ans))
