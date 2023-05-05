def dfs(count,temp_list):
    if count == n:
        ans.append(temp_list)
        return
    for i in range(len(num_list)):
        if v[i] == 0:
            v[i] = 1
            dfs(count+1,temp_list+[num_list[i]])
            v[i] = 0


n = int(input())
num_list = list(range(1,(n+1)))
v = [0] * n
ans = []

dfs(0,[])
for i in ans:
    print(" ".join(map(str, i)))

