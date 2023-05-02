def dfs(count, start, temp_list):
    if count == 6:
        ans.append(temp_list)
        return
    for i in range(start, k):
        dfs(count+1, i+1, temp_list+[num_list[i]])

while True:
    num_list = list(map(int, input().split()))
    if num_list == [0]:
        break
    k = num_list.pop(0)
    ans = []
    dfs(0,0,[])
    ans.sort()
    for i in ans:
        print(" ".join(map(str, i)))
    
    print()
