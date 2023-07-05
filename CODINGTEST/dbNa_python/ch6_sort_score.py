n = int(input())

score = []

for _ in range(n):
    score.append(list(input().split()))

score.sort(key = lambda x:int(x[1]))

for i in range(n):
    print(score[i][0], end = " ")
print()