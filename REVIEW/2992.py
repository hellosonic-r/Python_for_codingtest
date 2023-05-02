def dfs(count, temp_list):
    global max_result
    if count == len(num_list):
        if x<int("".join(map(str, temp_list))):
            if max_result > int("".join(map(str, temp_list))):
                max_result = int("".join(map(str, temp_list)))
        return
    for i in range(len(num_list)):
        if v[i] == 0:
            v[i] = 1 
            dfs(count+1, temp_list+[num_list[i]])
            v[i] = 0

x = int(input())
num_list = list(map(int, str(x)))
max_result = 10**(len(num_list))
v = [0] * len(num_list)
dfs(0,[])
if len(list(map(int,str(max_result)))) > len(num_list):
    print(0)
else:
    print(max_result)