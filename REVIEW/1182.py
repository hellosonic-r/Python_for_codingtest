def dfs(count, start, temp_sum):
    global ans
    if  sum(temp_sum) == s and len(temp_sum) != 0:
        ans += 1

    for i in range(start, n):
        dfs(count+1, i+1, temp_sum+[num_list[i]])


n, s = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()
temp_sum = []
ans = 0

dfs(0,0,[])

 
print(ans)