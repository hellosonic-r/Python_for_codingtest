n = int(input())
for _ in range(n):
    a = list(map(int, input().split()))
    a.pop(0)
    a.sort(reverse= True)
    b = list(map(int, input().split()))
    b.pop(0)
    b.sort(reverse= True)
    if a > b:
        print("A")
    elif a < b:
        print("B")
    else:
        print("D")

