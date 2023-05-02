##이진트리
def dfs(count, score_sum, cal_sum):
    global max_score
    if cal_sum > l:
        return
    if score_sum > max_score:
        max_score = score_sum
    if count == n:
        return
    
    
    dfs(count+1, score_sum + scores[count], cal_sum + cals[count])
    dfs(count+1, score_sum, cal_sum)

t = int(input())
for test_case in range(1,t+1):
    n,l = map(int,input().split()) #n:재료수 / l:제한칼로리
    scores = []
    cals = []
    for _ in range(n):
        score,cal = map(int, input().split())
        scores.append(score)
        cals.append(cal)
    max_score = 0
    dfs(0,0,0)
    print(max_score)

##멀티트리
def dfs(count,start, score_sum,cal_sum):
    global max_score
    if cal_sum>l:
        return
    if score_sum > max_score:
        max_score = score_sum
    for i in range(start, len(scores)):
        dfs(count,i+1,score_sum+scores[i],cal_sum+cals[i])

t = int(input())
for test_case in range(1,t+1):
    n,l = map(int,input().split()) #n:재료수 / l:제한칼로리
    scores = []
    cals = []
    for _ in range(n):
        score,cal = map(int, input().split())
        scores.append(score)
        cals.append(cal)
    max_score = 0
    dfs(0,0,0,0)
    print(max_score)

