ans = []
def dfs(index):
    if len(ans) == m:
        print(" ".join(map(str, ans)))
        return
    if index == n:
        return
    for i in range(1, n+1):
        if len(ans)!= 0:
            if ans[-1] > i:
                continue
        ans.append(i)
        dfs(index+1)
        ans.pop()


n, m = map(int, input().split())

dfs(0)


### 백트래킹 연습 
# 내 풀이
def dfs(index):
    if index == m:
        print(" ".join(map(str, ans)))
        return
    for i in range(1, n+1):
        if len(ans) != 0:
            if ans[-1] > i:
                continue
        ans.append(i)
        dfs(index+1)
        ans.pop()

n, m = map(int, input().split())
ans = []

dfs(0)

# 다른 풀이
def dfs(index, temp):
    if index == m:
        print(" ".join(map(str, ans)))
        return
    for i in range(temp, n+1):
        ans.append(i)
        dfs(index+1, i)
        ans.pop()

n, m = map(int, input().split())
ans = []

dfs(0,1)
