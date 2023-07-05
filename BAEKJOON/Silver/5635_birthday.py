n = int(input())

d = {}
students = []
for _ in range(n):
    student = list(map(str, input().split(" ")))
    student[1] = int(student[1])
    student[2] = int(student[2])
    student[3] = int(student[3])
    students.append(student)

students.sort(key = lambda x:x[1])
students.sort(key = lambda x:x[2])
students.sort(key = lambda x:x[3])

print(students[-1][0])
print(students[0][0])

