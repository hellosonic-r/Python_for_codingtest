n = int(input())

pillar = []

for i in range(n):
    l, h = map(int, input().split())
    pillar.append((l,h))

#기둥 x좌표 순으로 오름차순 정렬
pillar.sort()
max_pillar_idx = 0

#오름차순 정렬한 기둥 리스트 중, 높이가 가장 큰 인덱스 찾기
for i in range(len(pillar)):
    if pillar[max_pillar_idx][1] < pillar[i][1]:
        max_pillar_idx = i

#높이가 가장 큰 인덱스의 기둥 면적
ans = 0

#높이가 가장 큰 인덱스 기준으로 좌측
h = pillar[0][1]
for i in range(0,max_pillar_idx): #0,3 #0,1,2/  max : 3
    #만약 다음 기둥이 현재 기둥 높이보다 크다면
    if pillar[i+1][1] > h:
        #면적에 다음 기둥까지 거리와 높이를 곱한 값을 더해주고
        ans += h*(pillar[i+1][0]-pillar[i][0])
        #높이를 다음 기둥으로 최신화
        h = pillar[i+1][1]
    #그렇지 않다면 높이는 현재 높이 그대로 하고 면적만 더해주기    
    else:
        ans += h*(pillar[i+1][0]-pillar[i][0])

#높이가 가장 큰 인덱스 기준으로 우측
h = pillar[-1][1]
for j in range(n-1,max_pillar_idx,-1): # (6,3) #6,5,4
    #만약 다음 기둥이 현재 기둥 높이보다 크다면
    if pillar[j-1][1] > h:
        #면적에 다음 기둥까지 거리와 높이를 곱한 값을 더해주고
        ans += h * (pillar[j][0]-pillar[j-1][0])
        #높이를 다음 기둥으로 최신화
        h = pillar[j-1][1]
    #그렇지 않다면 높이는 현재 높이 그대로 하고 면적만 더해주기
    else:
        ans += h*(pillar[j][0]-pillar[j-1][0])

print(ans + pillar[max_pillar_idx][1])


