# n = int(input())
# candy = []
# for _ in range(n):
#     candy.append(list(input()))

# cnt = 0
# garo_result = 1
# garo_max_result = 0
# def garo_check(n, arr):
#     global garo_result, garo_max_result
#     garo_result = 1
#     for y in range(n):
#         for x in range(1,n):
#             if arr[y][x-1] == arr[y][x]:
#                 garo_result += 1
#             else:
#                 garo_result = 1
#         if garo_max_result < garo_result:
#             garo_max_result = garo_result
#     return garo_max_result

# sero_result = 1
# sero_max_result = 0
# def sero_check(n, arr):
#     global sero_result, sero_max_result
#     sero_result = 1
#     for x in range(n):
#         for y in range(1,n):
#             if arr[y-1][x] == arr[y][x]:
#                 sero_result += 1
#             else:
#                 sero_result = 1
#         if sero_max_result < sero_max_result:
#             sero_max_result = sero_result
#     return sero_max_result

# result = []

# def garo_switch(n, candy):
#     temp = candy
#     for y in range(n):
#         for x in range(1,n): #1,2
#             if candy[y][x-1] != candy[y][x]:
#                 temp[y].insert(x-1, temp[y].pop(x))
#                 result.append(max(sero_check(n,temp),garo_check(n,temp)))

# def sero_switch(n, candy):
#     temp = candy
#     for x in range(n):
#         for y in range(1,n):
#             if candy[y-1][x] != candy[y][x]: #[0][0]  != [1][0]
#                 out = temp[y-1].pop(x)
#                 temp[y-1].insert(x, temp[y].pop(x))
#                 temp[y].insert(x, out)
# #                 result.append(max(sero_check(n,temp),garo_check(n,temp)))

# # garo_switch(n,candy)
# # sero_switch(n,candy)

# # print(result)
    

# n = int(input())
# candy = []
# for _ in range(n):
#     candy.append(list(input()))

# cnt = 0
# garo_result = 1
# garo_max_result = 0
# def garo_check(n, arr):
#     global garo_result, garo_max_result
#     for y in range(n):
#         garo_result = 1
#         for x in range(1,n):
#             if arr[y][x-1] == arr[y][x]:
#                 garo_result += 1
#                 garo_max_result = garo_result
#             else:
#                 garo_result = 1
#         if garo_max_result < garo_result:
#             garo_max_result = garo_result
#     return garo_max_result

# sero_result = 1
# sero_max_result = 0
# def sero_check(n, arr):
#     global sero_result, sero_max_result
#     sero_result = 1
#     for x in range(n):
#         for y in range(1,n):
#             if arr[y-1][x] == arr[y][x]:
#                 sero_result += 1
#                 sero_max_result = sero_result
#             else:
#                 sero_result = 1
#         if sero_max_result < sero_max_result:
#             sero_max_result = sero_result
#     return sero_max_result

# result = []

# def garo_switch(n, candy):
#     temp = candy
#     for y in range(n):
#         for x in range(1,n): #1,2
#             if candy[y][x-1] != candy[y][x]:
#                 temp[y][x-1], temp[y][x] = temp[y][x], temp[y][x-1]
#                 result.append(max(sero_check(n,temp),garo_check(n,temp)))

# def sero_switch(n, candy):
#     temp = candy
#     for x in range(n):
#         for y in range(1,n):
#             if candy[y-1][x] != candy[y][x]: #[0][0]  != [1][0]
#                 out = temp[y-1].pop(x)
#                 temp[y-1].insert(x, temp[y].pop(x))
#                 temp[y].insert(x, out)
#                 result.append(max(sero_check(n,temp),garo_check(n,temp)))

# garo_switch(n,candy)
# sero_switch(n,candy)

# print(result)
    
n = int(input())
candy = []
for i in range(n):
    candy.append(list(input()))

garo_cnt = 1
max_garo_cnt = 0
sero_cnt = 1
max_sero_cnt = 0
def candy_check(n, arr):
    global garo_cnt, sero_cnt, max_garo_cnt, max_sero_cnt
    for y in range(n):
        garo_cnt = 1
        for x in range(1, n): #1,2
            if arr[y][x-1] == arr[y][x]:
                garo_cnt += 1 
                if max_garo_cnt < garo_cnt:
                    max_garo_cnt = garo_cnt
            else:
                garo_cnt = 1
    
    for x in range(n):
        sero_cnt = 1
        for y in range(1, n):
            if arr[y-1][x] == arr[y][x]:
                sero_cnt += 1
                if max_sero_cnt < sero_cnt:
                    max_sero_cnt = sero_cnt
            else:
                sero_cnt = 1
            
    return max(max_garo_cnt, max_sero_cnt)

result = []
ans = 0
#가로 스위치
for b in range(n):
    for a in range(1, n):
        if candy[b][a-1] != candy[b][a]:
            candy[b][a-1], candy[b][a] = candy[b][a], candy[b][a-1]
            result = candy_check(n, candy)
            candy[b][a], candy[b][a-1] = candy[b][a-1], candy[b][a]
            if ans < result:
                ans = result
    
#세로 스위치
for a in range(n):
    for b in range(1, n):
        if candy[b-1][a] != candy[b][a]:
            candy[b-1][a], candy[b][a] = candy[b][a], candy[b-1][a]
            result = candy_check(n, candy)
            candy[b][a], candy[b-1][a] = candy[b-1][a], candy[b][a]
            if ans < result:
                ans = result

print(ans)
