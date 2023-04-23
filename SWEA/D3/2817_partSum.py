# ###실패코드 - 돌아가지를 못한다
# # def dfs(index):
# #     global temp_sum
# #     if temp_sum == k:
# #         result.append(temp_sum)
# #         return
# #     if temp_sum > k:
# #         return
# #     if index == n:
# #         return
# #     temp_sum += a[index]
# #     dfs(index+1)
    

# # t = int(input())

# # for test_case in range(1, t+1):
# #     n, k = map(int, input().split())
# #     a = list(map(int, input().split()))
# #     result=[]
# #     temp_sum = 0
# #     dfs(0)
# #     print(result)
# #     print("#{} {}".format(test_case, len(result)))
    

# ### 멀티트리-pass
# def dfs(count, temp_sum, start):
#     global ans
#     if temp_sum >= k:
#         if temp_sum == k:
#             ans += 1
#         return
#     if count == n:
#         return
    
#     for i in range(start, n):
#         if v[i] == 0:
#             v[i] = 1
#             dfs(count + 1, temp_sum+num_list[i], i+1)
#             v[i] = 0
    
# t = int(input())
# for test_case in range(1, t+1):
#     n,k = map(int, input().split())
#     num_list = list(map(int, input().split()))
#     num_list.sort()
#     ans = 0
#     v = [0] * (n)
#     dfs(0,0,0)
#     print(ans)


# ###이진트리
# def dfs(index, temp_sum):
#     global ans
#     if temp_sum > k:
#         return
#     if temp_sum == k:
#         ans += 1
#         return
#     if index == n:
#         return
#     dfs(index+1, temp_sum)
#     dfs(index+1, temp_sum+num_list[index])


# t = int(input())
# for test_case in range(1, t+1):
#     n,k = map(int, input().split())
#     num_list = list(map(int, input().split()))
#     num_list.sort()
#     ans = 0
#     v = [0] * (n)
#     dfs(0, 0)
#     print("#{} {}".format(test_case, ans))

##다시 풀어보기
def dfs(count, start, temp_list):
    global ans
    if len(temp_list)>=1 and sum(temp_list) == k:
        ans += 1
    if count == n:
        return
    for i in range(start,n):
        if visited[i] == 0:
            visited[i] = 1
            dfs(count+1, i, temp_list + [num_list[i]])
            visited[i] = 0

t = int(input())
for test_case in range(1, t+1):
    n, k = map(int, input().split()) #최소 한 개 이상 선택하여 더하면 K
    num_list = list(map(int, input().split()))
    visited = [0]*n
    ans = 0
    dfs(0, 0, [])
    print("#{} {}".format(test_case, ans))


