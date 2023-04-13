n = int(input())

for _ in range(n):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.pop(0)
    a.sort(reverse=True)
    b.pop(0)
    b.sort(reverse=True)
    if a>b:
        print("A")
    elif a<b:
        print("B")
    else:
        print("D")

# a = [4,4,4]
# b = [4,3,2,1,1]

# print(a>b)

# a = [4,4,4]
# b = [4,3,4,4,4]

# print(a>b)

a = ['apple','banana','coconut']
b = ['apple','bbbbbb']

print(a<b)



