n = int(input())
fin = []
for _ in range(n):
    fin.append(int(input()))

fin.sort(reverse = True)

for i in fin:
    print(i, end = " ")
