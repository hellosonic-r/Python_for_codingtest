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

###다른풀이 - 변수에 num



def dfs(num):
    if num == m:
        print(" ".join(map(str, s)))
        return
    
    for i in range(1, n+1):
        if visited[i] == 0:
            visited[i] = 1
            s.append(i)
            dfs(num+1)
            s.pop()
            visited[i] = 0
    return

    
n, m = map(int, input().split())
visited = [0] * (n+1)
s = []

dfs(0)
