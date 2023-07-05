# def dfs(count, idx, temp_sum):
#     global answer #count 0 ->
#     if count == len(name_list):
#         if answer > temp_sum:
#             answer = temp_sum
#         return
    
#     if idx not in v:
#         v.append(idx)
#         dfs(count+1, idx-1, temp_sum+min((ord(name_list[idx])-ord("A")), (26- (ord("A")-ord(name_list[idx]))))+1)
#         dfs(count+1, idx+1, temp_sum+min((ord(name_list[idx])-ord("A")), (26- (ord("A")-ord(name_list[idx]))))+1)
#         dfs(count, idx+1, temp_sum+1)
#         dfs(count, idx-1, temp_sum+1)
#         v.pop()
        
# # a : 97 b : 98 1이 가깝냐 26-
# answer = 1e9
# name = input()
# name_list = list(map(str, name))
# v = []
# dfs(0,0,0)

# print(answer)

print([2]+[3])