n = int(input())
pillar = []
for i in range(n):
    location, height = map(int,input().split())
    pillar.append((location,height))
pillar.sort()
compare = 0
max_idx = 0

for i in range(len(pillar)):
    if compare <= pillar[i][1]:
        compare = pillar[i][1]
        max_idx = i

h = pillar[0][1]
result = pillar[max_idx][1]
#최대 높이 전까지 돌면서 다음 기둥이 현재보다 높으면
#result에 현재의 면적을 계산해서 더해주고 높이를 다음 기둥으로 갱신한다.
for i in range(max_idx):
    if h < pillar[i+1][1]:
        result += h * (pillar[i+1][0]-pillar[i][0])
        h = pillar[i+1][1]
    #아니면 그냥 현재 면적을 더해준다.
    else:
        result += h * (pillar[i+1][0]-pillar[i][0])
h = pillar[-1][1]
for i in range(n-1, max_idx, -1):
    if h < pillar[i-1][1]:
        result += h * (pillar[i][0] - pillar[i-1][0])
        h = pillar[i-1][1]
    else:
        result += h * (pillar[i][0] - pillar[i-1][0])

print(result)

