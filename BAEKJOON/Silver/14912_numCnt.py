n, d = map(int, input().split())

ans = 0

for num in range(1, n+1):
    arr = list(map(int, str(num)))
    if d in arr:
        ans += arr.count(d)

print(ans)

