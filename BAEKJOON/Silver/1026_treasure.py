n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort(reverse=True)

ans = 0

i = 0
while b:
    B=b.pop(b.index(min(b)))
    ans += a[i]*B
    i+=1

print(ans)