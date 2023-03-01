a = int(input())
b = int(input())
c = int(input())

num = list(map(int, str(a*b*c)))
check = [0]*10
for i in range(len(num)):
    check[num[i]] = num.count(num[i])

for j in check:
    print(j)
