# ## 시도1 : ans에 안담김
# def dfs(count):
#     if count == m:
#         if temp_list not in ans:
#             ans.append(temp_list)
#             return
#     # if count == m:
#     #     ans.append(temp_list)
#     if count == n:
#         return
    
#     for i in range(n):
#         if visited[i] == 0:
#             visited[i] = 1
#             temp_list.append(num_list[i])
#             dfs(count+1)
#             visited[i] = 0
#             temp_list.pop()
            
# n, m = map(int, input().split())
# num_list = list(map(int, input().split()))
# num_list.sort()
# ans = []
# visited = [0] * n
# temp_list = []

# dfs(0)
# print(temp_list)
# print(ans)


# ## 시도2 : 시간초과
# def dfs(count, temp_list):
#     if count == m:
#         if temp_list not in ans:
#             ans.append(temp_list)
#         return
#     if count == n:
#         return

#     for i in range(n):
#         if visited[i] == 0:
#             visited[i] = 1
#             dfs(count+1, temp_list+[num_list[i]])
#             visited[i] = 0

# n, m = map(int ,input().split())
# num_list = list(map(int, input().split()))
# num_list.sort()
# visited = [0] * n
# ans = []

# dfs(0,[])

# for i in ans:
#     print(" ".join(map(str, i)))


## 시도3 : 시간초과 prev로 해결
def dfs(count, temp_list):
    if count == m:
        ans.append(temp_list)
        return
    if count == n:
        return
    
    prev = 0
    for i in range(n):
        if visited[i] == 0 and prev != num_list[i]:
            prev = num_list[i]
            visited[i] = 1
            dfs(count+1, temp_list + [num_list[i]])
            visited[i] = 0

n, m = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()
visited = [0] * n
ans = []

dfs(0, [])
for i in ans:
    print(" ".join(map(str, i)))
