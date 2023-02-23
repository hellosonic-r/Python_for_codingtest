###색종이
n = int(input())
array = [[0] * 100 for _ in range(100)] #도화지 범위 초기화 (100*100)

for _ in range(n):
    x, y = map(int, input().split())

    for i in range(x, x+10):
        for j in range(y, y+10):
            array[i][j] = 1
fin = 0
for k in range(100):
    fin = fin + array[k].count(1)

print(fin)