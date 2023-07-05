##시간초과
def dfs(count, start, temp_list):
    global ans
    if count == k:
        if ans < sum(temp_list):
            ans = sum(temp_list)
        return
    if count == n:
        return

    for i in range(start, n):
        next_list = temp_list+[num_list[i]]
        if (count, sum(next_list)) not in r:
            r.append((count, sum(next_list)))
            dfs(count+1, i+1, temp_list+[num_list[i]])

t = int(input())

for test_case in range(1, t+1):
    n, k = map(int, input().split())
    num_list = list(map(int, input().split()))
    ans = 0
    r = []
    dfs(0,0,[])

    print("#{} {}".format(test_case, ans))



##정렬 활용
t = int(input())

for test_case in range(1, t+1):
    n, k = map(int, input().split())
    num_list = list(map(int, input().split()))

    num_list.sort(reverse=True)

    print("#{} {}".format(test_case, sum(num_list[:k])))