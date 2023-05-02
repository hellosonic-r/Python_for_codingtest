def dfs(count,last,temp_list): 
    global min_check,min_ans,max_check,max_ans
    if count == k:
        if min_check > int("".join(map(str, temp_list))):
            min_check = int("".join(map(str, temp_list)))
            min_ans = "".join(map(str, temp_list))
        if max_check < int("".join(map(str, temp_list))):
            max_check = int("".join(map(str, temp_list)))
            max_ans = "".join(map(str, temp_list))
        return

    for i in range(len(num_list)):
        if sign[count] == "<":
            if v[i] == 0 and num_list[i] > last:
                v[i] = 1
                dfs(count+1, num_list[i], temp_list+[num_list[i]])
                v[i] = 0
        if sign[count] == ">":
            if v[i] == 0 and num_list[i] < last:
                v[i] = 1
                dfs(count+1, num_list[i], temp_list+[num_list[i]])
                v[i] = 0
            
k = int(input())
sign = list(input().split())

num_list = list(range(0,10))

min_check = 9999999999
max_check = 0
min_ans = ""
max_ans = ""
for i in range(len(num_list)):
    v = [0] * 10
    v[i] = 1
    dfs(0,num_list[i],[i])

print(max_ans,min_ans,sep="\n")
