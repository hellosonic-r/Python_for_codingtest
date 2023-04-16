# def dfs(count, index):
#     global temp
#     if count == n:
#         temp+=1 
#         return
#     for i in range(n):
#         if i != index-1 and i != index and i != index+1:

#             dfs(count + 1, i)

# n = int(input())
# ans = 0
# temp = 0
# dfs(0, 0)

# print(temp)


def dfs(y):
    global ans
    if y == n:
        ans += 1
        return
    for i in range(n):
        if v1[i] == 0 and v2[y+i] == 0 and v3[y-i] == 0:
            v1[i] = v2[y+i] = v3[y-i] = 1
            dfs(y+1)
            v1[i] = v2[y+i] = v3[y-i] = 0
    

n = int(input())
ans = 0
v1 = [0] * n 
v2 = [0] * (2*n)
v3 = [0] * (2*n)

dfs(0)
print(ans)