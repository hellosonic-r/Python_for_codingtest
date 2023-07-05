# ##백트래킹 - 메모리 초과
# import sys
# sys.setrecursionlimit(10**6)
# def dfs(count, temp_list):
#     global ans
#     if sum(temp_list) >= k:
#         if sum(temp_list) == k:
#             ans += 1
#         return
    
#     for i in range(len(coin_list)):
#         #다음에 올 숫자 리스트 정렬해서 저장
#         next_temp_list = sorted(temp_list+[coin_list[i]])
#         #다음에 올 숫자 리스트가 방문 테이블에 없다면
#         if next_temp_list not in v:
#             #방문 테이블에 추가하고 
#             v.append(next_temp_list)
#             #다음 숫자 리스트에 대한 dfs호출
#             dfs(count+1, next_temp_list)

# n,k = map(int, input().split())
# coin_list = []
# for _ in range(n):
#     coin_list.append(int(input()))
# ans = 0
# v = []

# dfs(0,[])
# print(ans)


n, k = map(int, input().split())
coin_list = []
for _ in range(n):
    coin_list.append(int(input()))

dp = [0] * (k+1)

