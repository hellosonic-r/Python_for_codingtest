def dfs(count,temp_sum):
    if count == n-1:
        result.append(temp_sum)
        return
    
    for i in range(4):
        if i == 0 and op[i] >= 1:
            op[i] -= 1
            dfs(count+1, temp_sum+num_list[count+1])
            op[i] += 1
        elif i == 1 and op[i] >= 1:
            op[i] -= 1
            dfs(count+1, temp_sum-num_list[count+1])
            op[i] += 1
        elif i == 2 and op[i] >= 1:
            op[i] -= 1
            dfs(count+1, temp_sum*num_list[count+1])
            op[i] += 1
        elif i == 3 and op[i] >= 1:
            op[i] -= 1
            if temp_sum < 0:
                dfs(count+1, -(abs(temp_sum)//num_list[count+1]))
            else:
                dfs(count+1, temp_sum//num_list[count+1])
            op[i] += 1 

n = int(input())
num_list = list(map(int, input().split()))
op = list(map(int ,input().split())) #+ - x / 개수
result = []
dfs(0, num_list[0])
print(max(result),min(result),sep="\n")
