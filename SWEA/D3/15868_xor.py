t = int(input())
for test_case in range(1, t+1):
    n, m = map(int, input().split())
    if n != m:
        print("#{} {}".format(test_case, "yes"))
    else:
        graph = []    
        for i in range(n):
            graph.append(list(map(str, input())))
        ans = ""
        for i in range(n):
            for j in range(m):
                if graph[i][j] == graph[j][i]:
                    ans = "yes"
                else:
                    ans = "no"
                    break
        print("#{} {}".format(test_case, ans))

