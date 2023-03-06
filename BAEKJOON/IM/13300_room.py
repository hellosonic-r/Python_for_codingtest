n, k = map(int, input().split())
grade = [[0]*2 for _ in range(6)]
for _ in range(n):
    s, y = map(int, input().split())
    if s == 1:
        if y == 1:
            grade[0][0] += 1
        elif y == 2:
            grade[1][0] += 1
        elif y == 3:
            grade[2][0] += 1
        elif y == 4:
            grade[3][0] += 1
        elif y == 5:
            grade[4][0] += 1
        elif y == 6:

            grade[5][0] += 1
    if s == 0:
        if y == 1:
            grade[0][1] += 1
        elif y == 2:
            grade[1][1] += 1
        elif y == 3:
            grade[2][1] += 1
        elif y == 4:
            grade[3][1] += 1
        elif y == 5:
            grade[4][1] += 1
        elif y == 6:
            grade[5][1] += 1
count = 12

for i in range(6):
    for j in range(2):
        if grade[i][j] > k:
            count += grade[i][j] // k
        if grade[i][j] == 0:
            count -= 1
print(count)