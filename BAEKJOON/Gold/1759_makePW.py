def dfs(count, start, temp_list):
    if len(temp_list) == l:
        mo_cnt = 0
        za_cnt = 0
        for i in temp_list:
            if i in mo:
                mo_cnt += 1
            if i in za:
                za_cnt += 1
        if mo_cnt >= 1 and za_cnt >= 2:
            ans.append(temp_list)
    if count == c:
        return
    
    for i in range(start, len(pw_list)):
        dfs(count+1, i+1, temp_list+[pw_list[i]])

l, c = map(int, input().split())
pw_list = list(map(str, input().split()))
pw_list.sort()
mo = []
za = []
for i in pw_list:
    if i in ['a','e','i','o','u']:
        mo.append(i)
    else:
        za.append(i)
ans = []

dfs(0,0,[])
for i in ans:
    print("".join(map(str, i)))