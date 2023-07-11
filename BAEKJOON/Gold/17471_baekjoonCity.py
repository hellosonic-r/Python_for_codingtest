from collections import deque
from itertools import combinations

def bfs(a, arr):
    queue = deque()
    queue.append(a)
    v[a] = 1
    while queue:
        x = queue.popleft()
        for nx in graph[x]:
            if v[nx] == 0 and nx in arr:
                v[nx] = 1
                queue.append(nx)

# def bfs(arr):
#     cnt = 0
#     for i in arr: #2,3,5,6
#         for j in arr:
#             if j in graph[i]:
#                 cnt += 1
#                 break
#     if cnt == len(arr):
#         return True
#     else:
#         return False

n = int(input())
pick_list = list(range(1,n+1))
people = [0] + list(map(int, input().split())) #1번구역부터 n번 구역까지
graph = [[] for _ in range(n+1)]

for i in range(1,n+1):
    connect_list = list(map(int, input().split()))
    x = connect_list.pop(0)
    for c in range(x):
        graph[i].append(connect_list[c])

min_ans = 1e9
ans = -1
for i in range(2, n): #1개부터 5개까지 뽑음
    a = list(combinations(pick_list, i))
    for a_list in a:
        a_ans = 0
        b_ans = 0 
        a_flag = True
        b_flag = True
        v = [0] * (n+1)
        b_list = list(set(pick_list)-set(a_list))
        bfs(a_list[0],a_list)
        if v.count(1) == len(a_list):
            for num in a_list:
                a_ans += people[num]
            v = [0] * (n+1)
            bfs(b_list[0],b_list)
            if v.count(1) == len(b_list):
                for nu in b_list:
                    b_ans += people[nu]
            else:
                b_flag = False
        else:
            a_flag = False

        if a_flag == True and b_flag == True:
            ans = 1
            if min_ans > abs(a_ans-b_ans):
                min_ans = abs(a_ans-b_ans)
                # print(graph)
                # print("people:",a_ans, b_ans, "a_list:",a_list,"b_list:",b_list)

if n > 2:
    if ans == 1:
        print(min_ans)
    else:
        print(-1)

elif n == 2: #2개 구역일 경우 최소값은 단순히 뺀 값
    print(abs(people[1] - people[2]))

