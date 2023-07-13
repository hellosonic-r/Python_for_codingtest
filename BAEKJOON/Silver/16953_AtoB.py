# def dfs(depth, temp):
#     global a,b
#     if temp >= b:
#         if temp == b:
#             result.append(depth)
#         return
#     dfs(depth+1, temp*2)
#     dfs(depth+1, int("".join(map(str, (list(map(int, str(temp)))+[1])))))

# a, b = map(int, input().split())

# result = []

# dfs(0,a)

# if result:
#     print(min(result)+1)
# else:
#     print(-1)



from collections import deque

def bfs(a,b):
    queue = deque()
    queue.append((a,1))
    
    while queue:
        next_num, depth = queue.popleft()
        if next_num > b:
            continue
        if next_num == b:
            result.append(depth)

        queue.append((int(str(next_num)+"1"),depth+1))
        queue.append((next_num*2, depth+1))

a,b = map(int, input().split())

result = []
bfs(a,b)

if result:
    print(min(result))
else:
    print(-1)