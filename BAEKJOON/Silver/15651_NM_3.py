# ans = []

# def dfs(first):
#     if len(ans) == m:

#         print(" ".join(map(str, ans)))
#         return
#     if first == n:
#         return
#     for i in range(1, n+1):
#         ans.append(i)
#         dfs(first+1)
#         ans.pop()

# n, m = map(int, input().split())
# num_list = list(range(1,n+1))

# dfs(0)


### 백트래킹 연습

# 리스트를 고대로 넘겨준다. 
# def dfs(index, temp_list):
#     if index == m:
#         ans.append(temp_list)
#         return
#     for i in range(1, n+1):
#         dfs(index+1, temp_list+[i])

# n, m = map(int, input().split())
# ans = []

# dfs(0, [])
# for j in ans:
#     print(*j)

# 리스트를 넘겨주지 않고 ans에 그대로 append 한다

def dfs(index):
    if index == m:
        print(" ".join(map(str, ans)))
        return
    for i in range(1, n+1):
        ans.append(i)
        dfs(index+1)
        ans.pop()
n, m = map(int, input().split())
ans = []
dfs(0)
