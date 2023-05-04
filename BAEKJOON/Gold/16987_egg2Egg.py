##이렇게 풀다가 실패
def dfs(count, start_hp, start_weight, start):
    global ans
    if start_hp <= 0:
        ans = count
        return
    if count == n:
        ans = count
        return
    
    for i in range(start, n):
        first_hp = start_hp - weight_list[i]
        next_hp = hp_list[i] - start_weight 
        if next_hp <= 0:
            dfs(count+1, first_hp, start_weight, i)
           

n = int(input()) #계란의 수
hp_list = []
weight_list = []
for _ in range(n):
    hp, weight = map(int, input().split())
    hp_list.append(hp)
    weight_list.append(weight)
v = [0] * n
ans = 0
dfs(0, hp_list[0], weight_list[0], 1)
print(ans)





# def dfs(count, cnt ):
#     global ans
#     if count == n:
#         ans = max(ans, cnt)
#         return
#     if egg_list[count][0] <= 0:
#         dfs(count+1, cnt)
#     else:
#         flag = False
#         for i in range(n):
#             if count == i or egg_list[i][0] <= 0:
#                 continue
#             flag = True
#             egg_list[count][0] -= egg_list[i][1]
#             egg_list[i][0] -= egg_list[count][1]
#             dfs(count+1, cnt+int(egg_list[count][0]<=0)+int(egg_list[i][0]<=0))
#             egg_list[count][0] += egg_list[i][1]
#             egg_list[i][0] += egg_list[count][1]
#         if flag==False:
#             dfs(count+1, cnt)

# n = int(input())
# egg_list = []
# for _ in range(n):
#     egg_list.append(list(map(int, input().split())))
#     ans = 0
# dfs(0,0)
# print(ans)

