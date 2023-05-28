n = int(input())
a = list(map(int, input().split()))
a.sort()

m = int(input())
b = list(map(int, input().split()))

result = []

for x in b:
    start = 0
    end = n-1
    ans = False
    while start <= end:
        mid = (start + end) // 2
        if a[mid] > x:
            end = mid-1
        elif a[mid] < x:
            start = mid+1
        else:
            ans = True
            break
    if ans:
        result.append(1)
    else:
        result.append(0)

print(" ".join(map(str, result)))
