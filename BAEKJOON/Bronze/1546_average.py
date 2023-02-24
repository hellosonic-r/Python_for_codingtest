###평균

n = int(input())
score = list(map(int, input().split()))

new_score = []
for i in range(n):
    new_score.append(score[i]/max(score)*100)

print(sum(new_score)/n)
