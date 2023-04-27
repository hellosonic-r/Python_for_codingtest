##백트래킹
import sys
sys.setrecursionlimit(10**6)

def dfs(x,y,z, count):
    global ans
    if x == 16:
        x = 1
    if y == 29:
        y = 1
    if z == 20:
        z = 1 
    if x == e and y == s and m == z:
        ans = count
        return
    dfs(x+1, y+1, z+1, count+1)

e,s,m = map(int, input().split())
ans = 0
dfs(1,1,1,1)
print(ans)


##단순 반복문
e,s,m = map(int, input().split())

a,b,c = 1,1,1
ans = 1
while True:
    if a == e and b == s and c == m:
        break
    a += 1
    b += 1
    c += 1
    if a == 16:
        a = 1
    if b == 29:
        b = 1
    if c == 20:
        c = 1
    ans += 1

print(ans)