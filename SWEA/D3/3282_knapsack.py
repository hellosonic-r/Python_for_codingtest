def dfs(count, volume_sum, cost_sum):
    global max_cost
    if volume_sum > k:
        return
    if volume_sum <= k:
        if cost_sum > max_cost:
            max_cost = cost_sum
            return
    if count == n:
        return
    
    for i in range(n):
        if 0<=i<=100 and v[i] == 0:
            v[i] = 1
            dfs(count+1, volume_sum + things[i][0], cost_sum + things[i][1])
            v[i] = 0

t = int(input())
for test_case in range(1,t+1):
    n, k = map(int, input().split()) #n:물건의개수 k:가방의부피
    things = []
    for _ in range(n):
        volume, cost = map(int, input().split()) #volume:부피 cost:가치  // cost(가치)의 합 최대화 // 선택한 물건의부피의 합이 k이하
        things.append((volume, cost))
    v = [0] * n
    r = []
    max_cost = 0
    dfs(0,0,0)
    print("#{} {}".format(test_case, max_cost))
        