from collections import deque

def bfs(sx):
    queue = deque()
    queue.append(sx)
    v[sx] = 1

    while queue:
        x = queue.popleft()
        if x == k:
            return v[x]-1
        for i in (x-1,x+1,2*x):
            if 0<=i<=100000 and v[i] == 0:
                v[i] = v[x]+1
                queue.append(i)

n, k = map(int,input().split())

v = [0] * 100001

print(bfs(n))