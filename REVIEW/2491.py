## 구현
# n = int(input())
# num_list = list(map(int, input().split()))

# ans = 1
# big_cnt = 1
# small_cnt = 1
# for i in range(1, len(num_list)):
#     #커지는 수 
#     if num_list[i] >= num_list[i-1]:
#         big_cnt+=1
#         if ans < big_cnt:
#             ans = big_cnt
#     else: 
#         big_cnt = 1
#     #작아지는 수
#     if num_list[i] <= num_list[i-1]:
#         small_cnt+=1
#         if ans < small_cnt:
#             ans = small_cnt
#     else:
#         small_cnt = 1

# print(ans)
          
               
## 다이나믹 프로그래밍

n = int(input())
num_list = list(map(int, input().split()))

dp1 = [1 for _ in range(n)] #가장 긴 증가하는 수열
dp2 = [1 for _ in range(n)] #가장 긴 감소하는 수열

for i in range(1, n):
    if num_list[i-1] <= num_list[i]:
        dp1[i] = dp1[i-1] + 1
    if num_list[i-1] >= num_list[i]:
        dp2[i] = dp2[i-1] + 1

print(max(max(dp1), max(dp2)))