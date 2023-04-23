###멀티 트리 시간초과
# def dfs(count,result):
#     global ans
#     if result == s:
#         ans+=1
#         return  
#     if count == n:
#         return  
   
#     for i in range(len(num_list)):
#         if visited[i] == 0:
#             visited[i] = 1
#             dfs(count+1, result+num_list[i])
#             visited[i] = 0

# n,s= map(int,input().split())
# num_list = list(map(int,input().split()))
# visited = [0] * n
# ans = 0
# dfs(0,0)

# print(ans)


###다른사람 풀이 참고
# def dfs(count,start):
#     global cnt
#     if sum(ans) == s and len(ans) >= 1:
#         cnt += 1  
        
   
#     for i in range(start,len(num_list)):
#         if visited[i] == 0:
#             visited[i] = 1
#             ans.append(num_list[i])
#             dfs(count+1,i+1)
#             visited[i] = 0
#             ans.pop()

# n,s= map(int,input().split())
# num_list = list(map(int,input().split()))
# visited = [0] * n
# ans = []
# cnt = 0
# dfs(0,0)

# print(cnt)

##다시풀어보기
# def dfs(count,start,temp_list):
#     global ans
#     if sum(temp_list) == s and len(temp_list) > 0:
#         ans +=1 
#     if count == len(num_list):
#         return
#     for i in range(start, len(num_list)):
#         dfs(count+1, i+1,temp_list+[num_list[i]])

# n,s = map(int, input().split())
# num_list = list(map(int, input().split()))
# ans = 0
# dfs(0,0,[])
# print(ans)

##다시 풀어보기

def dfs(count, start, temp_list):
    global ans
    if len(temp_list) != 0 and sum(temp_list) == s:
        ans += 1
    if count == n:
        return
    for i in range(start, n):
        dfs(count+1, i+1, temp_list+[num_list[i]])


n, s = map(int,input().split())
num_list = list(map(int, input().split()))
ans = 0

dfs(0,0,[])
print(ans)
