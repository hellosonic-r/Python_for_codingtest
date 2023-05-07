def dfs(count, start, temp_list):
    if count == 3:
        result.append(sum(temp_list))
        return
    for i in range(start, 7):
        dfs(count+1, i+1, temp_list + [num_list[i]])

t = int(input())
for test_case in range(1,t+1):
    num_list = list(map(int, input().split()))
    result = []
    dfs(0,0,[])
    result.sort(reverse=True)
    ans_list = list(set(result))
    print("#{} {}".format(test_case, ans_list[4]))
                    