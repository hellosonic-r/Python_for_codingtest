n = int(input())

scorer = []
for _ in range(n):
    name, score = input().split()
    scorer.append((name,int(score)))

scorer = sorted(scorer, key = lambda student :student[1])

for student in scorer:
    print(student[0], end = " ")

