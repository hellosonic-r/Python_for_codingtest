# n, m = map(int,input().split())
# total = []
# for i in range(n):
#     total.append(list(map(int, input())))

# def dfs(x,y):
#     if x <= -1 or x >= n or y <= -1 or y >= m:
#         return False
#     if total[x][y] == 0:
#         total[x][y] = 1
#         dfs(x,y+1)
#         dfs(x+1,y)
#         dfs(x-1,y)
#         dfs(x,y-1)
#         return True
#     else:
#         return False
    
# result = 0
# for i in range(n):
#     for j in range(m):
#         if dfs(i,j) == True:
#             result +=1

# print(result)

#try1
# n, m = map(int, input().split())
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))

# def dfs(x,y):
#     if x<0 or x>=n or y<0 or y>=m:
#         return False
#     if graph[x][y] == 0:
#         graph[x][y] = 1
#         dfs(x,y+1)
#         dfs(x-1,y)
#         dfs(x,y-1)
#         dfs(x+1,y)
#         return True
#     else:
#         return False

# result = 0
# for i in range(n):
#     for j in range(m):
#         if dfs(i,j) == True:
#             result += 1

# print(result)

# #try2
# n, m = map(int, input().split())
# graph = []
# for _ in range(n):
#     graph.append(list(map(int, input())))

# def dfs(x,y):
#     if x<0 or x>=n or y<0 or y>=m:
#         return False
#     if graph[x][y] == 0:
#         graph[x][y] = 1
#         dfs(x,y-1)
#         dfs(x+1,y)
#         dfs(x,y+1)
#         dfs(x-1,y)
#         return True
#     else:
#         return False
# result = 0
# for i in range(n):
#     for j in range(m):
#         if dfs(i,j) == True:
#             result += 1 
# print(result)

#try3
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

def dfs(x,y):
    if x<0 or y<0 or x>=n or y>=m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    else:
        return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1

print(result)