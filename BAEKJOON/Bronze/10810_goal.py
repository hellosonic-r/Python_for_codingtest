n, m = map(int,input().split())

arr = [0]*(n+1)
for _ in range(m):
    i,j,k = map(int,input().split())
    for z in range(i, j+1):
        arr[z] = k

arr.pop(0)

for num in arr:
    print(num, end=" ")

print()
