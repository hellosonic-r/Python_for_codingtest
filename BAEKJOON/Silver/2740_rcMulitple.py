n, m = map(int, input().split())
a_list = []
for _ in range(n):
    a_list.append(list(map(int, input().split())))

b_list = []
m,k = map(int, input().split())
for _ in range(m):
    b_list.append(list(map(int, input().split())))

result = [[0] * k for _ in range(n)]

for i in range(n): #3
    for j in range(k):
        for z in range(m): #2
            result[i][j] += a_list[i][z] * b_list[z][j] 

for i in result:
    for j in i:
        print(j, end = " ")
    print()



