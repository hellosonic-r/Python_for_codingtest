def dfs(count, prize):
    global ans
    if count == k:
        ans = max(ans, int("".join(map(str,prize))))
        return
    for i in range(len(num_list)):
        for j in range(i+1, len(num_list)):
            num_list[i],num_list[j] = num_list[j],num_list[i]
            check = int("".join(map(str, num_list)))
            if (count,check) not in v:
                v.append((count,check))
                dfs(count+1, num_list)
            num_list[i],num_list[j] = num_list[j],num_list[i]

t = int(input())
for test_case in range(1,t+1):
    num, k = map(int, input().split())
    num_list = list(map(int, str(num)))
    v = []
    ans = 0
    dfs(0, [])
    print(ans)
    

    