def dfs(count, start, temp_list):
    if len(temp_list) == m:
        if temp_list not in ans:
            ans.append(temp_list)
    if count == n:
        return
    for i in range(start, len(num_list)):
        dfs(count+1, i, temp_list+[num_list[i]])
        
n,m = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort() # 1 ,7, 9, 9
ans = []
dfs(0,0,[])

for i in ans:
    print(" ".join(map(str, i)))