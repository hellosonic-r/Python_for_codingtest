def dfs(count,start,mo_cnt,ja_cnt,temp_list):
    if count == l:
        if mo_cnt>=1 and ja_cnt>=2 and ("".join(map(str, temp_list))) not in ans:
            temp_list.sort()
            ans.append("".join(map(str, temp_list)))
        return
    if count == c:
        return
    for i in range(start, len(total)):
        if total[i] in mo:
            dfs(count+1,i+1,mo_cnt+1,ja_cnt,temp_list+[total[i]])
        elif total[i] in ja:
            dfs(count+1,i+1,mo_cnt,ja_cnt+1,temp_list+[total[i]])


l,c = map(int, input().split())
total = list(map(str, input().split()))
mo = []
ja = []
for i in total:
    if i in ['a','e','i','o','u']:
        mo.append(i)
    else:
        ja.append(i)

v = [0] * c
ans = []

dfs(0,0,0,0,[])

ans.sort()
for i in ans:
    print(i)
