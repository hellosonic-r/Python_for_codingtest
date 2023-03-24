## 리스트 이용한 풀이
# n, k = map(int, input().split())

# num_li = list(range(1,n+1))
# ans = []
# num_plan_idx = k-1
# while num_li:
#     ans.append(num_li.pop(num_plan_idx)) 
#     if len(num_li) == 0:
#         break
#     else:
#         num_plan_idx = (num_plan_idx + (k-1)) % len(num_li)

# print("<",end="")
# for i in range(len(ans)):
#     if i == len(ans)-1:
#         print(ans[i],end="")
#     else:
#         print("{}{}".format(ans[i],", "),end="")
# print(">")


## 큐 이용한 풀이
from collections import deque
n, k = map(int, input().split())
queue =  deque(range(1, n + 1))
ans = []

while queue:
    for _ in range(k-1):
        #[1,2,3,4,5,6,7] 에서 k = 3일때, 
        #queue 에서 뺀 1,2 를 queue의 제일 마지막에 놓음으로써
        #빼야될 수를 가장 첫 번째 요소에 둔다.
        #[3,4,5,6,7,1,2] 
        queue.append(queue.popleft())
    ans.append(queue.popleft())

print(str(ans).replace('[','<').replace(']','>'))