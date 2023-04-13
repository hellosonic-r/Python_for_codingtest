# def dfs(num):
#     if num == m:
#         print(" ".join(map(str, s)))
#         return
    
#     for i in range(1, n+1):
#         if i not in s:
#             s.append(i)
#             dfs(num+1)
#             s.pop()

# n, m = map(int, input().split())
# s = []

# dfs(0)

### 다른풀이 - 변수에 num

# def dfs(num):
#     if num == m:
#         print(" ".join(map(str, s)))
#         return
    
#     for i in range(1, n+1):
#         if visited[i] == 0:
#             visited[i] = 1
#             s.append(i)
#             dfs(num+1)
#             s.pop()
#             visited[i] = 0
#     return

    
# n, m = map(int, input().split())
# visited = [0] * (n+1)
# s = []

# dfs(0)


### 백트래킹 연습

# ans = []
# def dfs(index): #index자리
#     if len(ans) == m:
#         print(" ".join(map(str, ans)))
#         return
#     if index == n:
#         return 
    
#     for i in range(1, n+1):
#         if visited[i] == 0: #ans에 현재의 값이 들어있는지 확인
#             visited[i] = 1 #지금 들어가니까 방문처리
#             ans.append(i)
#             dfs(index+1) #다음 자리를 결정하는 함수 호출
#             visited[i] = 0
#             ans.pop() #갔다와서는 마지막 자리를 빼줌


# n, m = map(int, input().split())
# visited = [0] * (n+1) #중복되는 수열이 들어가면 안된다.

# dfs(0)

### 백트래킹 연습 2

def dfs(index, temp_list):
    if index == m:
        print(" ".join(map(str, temp_list)))
        return
    
    for i in range(1, n+1):
        if visited[i] == 0:
            visited[i] = 1
            temp_list += [i]
            dfs(index+1, temp_list)
            visited[i] = 0
            temp_list.pop()
    
n, m = map(int, input().split())

visited = [0] * (n+1)
dfs(0,[])