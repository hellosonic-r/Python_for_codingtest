#백트래킹 - 440ms
def dfs(count, temp_list):
    global max_score
    if count == 3:
        if sum(temp_list) <= m:
            if max_score < sum(temp_list):
                max_score = sum(temp_list)
        return
    for i in range(len(num_list)):
        if v[i] == 0:
            v[i] = 1
            dfs(count+1, temp_list+[num_list[i]])
            v[i] = 0

n,m = map(int, input().split())
num_list = list(map(int, input().split()))
v = [0]*n

max_score = 0

dfs(0,[])
print(max_score)

#반복문으로 구현 - 92ms
n,m = map(int, input().split())
num_list = list(map(int, input().split()))

max_score = 0

for i in range(len(num_list)-2):
    for j in range(i+1, len(num_list)-1):
        for k in range(j+1, len(num_list)):
            if num_list[i]+num_list[j]+num_list[k] <= m:
                if max_score < num_list[i]+num_list[j]+num_list[k]:
                    max_score = num_list[i]+num_list[j]+num_list[k]

print(max_score)


