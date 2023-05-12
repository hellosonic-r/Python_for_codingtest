w, h = map(int, input().split())
n = int(input())
garo = [0,w]
sero = [0,h]
for _ in range(n): #0:가로로 자르기 1:세로로 자르기
    direction, cut = map(int, input().split())
    if direction == 1:
        garo.append(cut)
    else:
        sero.append(cut)

garo.sort()
sero.sort()

ans = []
for i in range(1,len(garo)):
    for j in range(1,len(sero)):
        ans.append((garo[i]-garo[i-1])*(sero[j]-sero[j-1]))

print(max(ans))
