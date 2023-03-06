# import sys
# n, k = map(int, sys.stdin.readline().split())
# temp = list(map(int,sys.stdin.readline().split()))
# sum = 0
# fin = 0
# for i in range(n-k+1):
#     for _ in range(k):
#         sum += temp[i]
#         i+=1
#     if sum >= fin:
#         fin = sum
#         sum = 0
#     else:
#         sum = 0 
    
# print(fin)

##시간초과
# import sys
# n, k = map(int, sys.stdin.readline().split())
# temp = list(map(int,sys.stdin.readline().split()))
# fin = 0
# for i in range(n-k+1):
#     if sum(temp[i:i+k]) > fin:
#         fin = sum(temp[i:i+k])
#     else:
#         continue
    
# print(fin)

import sys
n, k = map(int, sys.stdin.readline().split())
temp = list(map(int, sys.stdin.readline().split()))
sum_temp = sum(temp[:k])
max_temp = sum(temp[:k])
for i in range(k,n):
    sum_temp = sum_temp + temp[i] - temp[i-k]
    max_temp = max(sum_temp, max_temp)
print(max_temp)
