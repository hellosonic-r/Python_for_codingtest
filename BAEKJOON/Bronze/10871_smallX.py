n, x = map(int, input().split())

nums = list(map(int, input().split()))
fin = []
for num in nums:
    if num < x:
        fin.append(num)

for i in range(len(fin)):
    print(fin[i],end = " ")
    if i == len(fin) - 1:
        print()