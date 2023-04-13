###TC 10/20 #백트래킹 실패
# def dfs(burger):
#     if burger == n or (sum(cal_sum) <= limit and sum(score_sum)>max(result)):
#         result.append(sum(score_sum))
#         return
    
#     for i in range(n):
#         if visited[i] == 0:
#             visited[i] = 1
#             score_sum.append(score_list[i])
#             cal_sum.append(cal_list[i])
#             if sum(cal_sum)>1000:
#                 visited[i] = 0
#                 score_sum.pop()
#                 cal_sum.pop()
#                 continue
#             else:
#                 dfs(burger+1)
#             score_sum.pop()
#             cal_sum.pop()
#             visited[i] = 0

# t = int(input())

# for test_case in range(1, t+1):
#     n, limit = map(int, input().split())
    
#     score_sum = []
#     cal_sum = []
#     result = [0]
    
#     score_list = []
#     cal_list = []
#     visited = [0]*n
    
#     for _ in range(n):
#         score, cal = map(int, input().split())
#         score_list.append(score)
#         cal_list.append(cal)
        
#     dfs(0)
#     print("#{} {}".format(test_case, max(result)))




###dfs
def dfs(index, score_sum, cal_sum):
    global max_score
    if cal_sum > limit:
        return
    if max_score < score_sum:
        max_score = score_sum
    if index == n:
        return

    dfs(index+1, score_sum+score_list[index], cal_sum+cal_list[index])
    dfs(index+1, score_sum, cal_sum)

t = int(input())

for test_case in range(1, t+1):
    n, limit = map(int,input().split())

    score_list = []
    cal_list = []
    for _ in range(n):
        score, cal = map(int, input().split())
        score_list.append(score)
        cal_list.append(cal)
    max_score = 0

    dfs(0,0,0)
    print(max_score)


    

    
        
    
        
    
        
        