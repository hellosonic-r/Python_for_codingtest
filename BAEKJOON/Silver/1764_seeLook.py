n, m = map(int, input().split())
d = {}
for _ in range(n):
    x = input()
    d[x] = 1
result = []
for _ in range(m):
    y = input()
    if y in d:
        result.append(y)

result.sort()

print(len(result))
for i in result:
    print(i)
    