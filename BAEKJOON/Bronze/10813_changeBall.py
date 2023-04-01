n, m = map(int,input().split())
num_li = list(range(1,n+1))

for _ in range(m):
    i, j = map(int, input().split())
    num_li[i-1], num_li[j-1] = num_li[j-1], num_li[i-1]

for k in range(len(num_li)):
    print(num_li[k], end=" ")
    if k == len(num_li)-1:
        print()