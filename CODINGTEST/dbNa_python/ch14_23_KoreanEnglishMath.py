n = int(input())
students_score = []
for _ in range(n):
    students_score.append(list(input().split()))

students_score.sort(key = lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in range(n):
    print(students_score[i][0])