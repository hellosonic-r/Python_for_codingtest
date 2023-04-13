# s = []

# def check_sort(num_list):
#     for i in range(len(num_list)-1):
#         if num_list[i+1] - num_list[i] > 0:
#             continue
#         else:
#             return False
#     return True

# def dfs():
#     if len(s) == m:
#         if check_sort(s):
#             print(" ".join(map(str, s)))
#             return
#         else:
#             return 

#     for i in range(1, n+1):
#         if i not in s:
#             s.append(i)
#             dfs()
#             s.pop()

# n, m = map(int, input().split())

# dfs()

### 백트래킹 연습
# 1. 이진트리

# def dfs(selc_num, temp_list):
#     if selc_num > n:
#         if len(temp_list) == m:
#             ans.append(temp_list)
#         return
#     dfs(selc_num+1, temp_list+[selc_num]) #선택
#     dfs(selc_num+1, temp_list) #선택x 

# n, m = map(int, input().split())
# ans = []

# dfs(1, [])
# for i in ans:
#     print(*i)


# 2. 멀티트리

def dfs(index, s, temp_list):
    if index == m:
        ans.append(temp_list)
        return
    
    for i in range(s, n+1):
        dfs(index+1, i+1, temp_list+[i])
        
n, m = map(int, input().split())
ans = []

dfs(0, 1, [])
print(ans)