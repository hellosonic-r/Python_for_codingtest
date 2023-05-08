n = int(input())
cus = []
for _ in range(n):
    cus.append(input().split())

cus.sort(key = lambda x:int(x[0]))

for i in cus:
    print("{} {}".format(int(i[0]), i[1]))