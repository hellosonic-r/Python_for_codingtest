n, l = map(int, input().split()) #n:신호등의 개수 l:도로의 길이
light = []
for _ in range(n):
    d,r,g = map(int, input().split()) #d:신호등위치 r:빨간색 지속시간 g:초록색 지속시간
    light.append((d,r,g))

t = 0
distance = 0
i = 0
while True:
    if distance == l:
        break
    t+=1
    distance += 1
    if i<=len(light)-1 and distance == light[i][0]:
        if (t % (light[i][1] + light[i][2])) >= light[i][1]:
            t += 0
        else:
            t += (light[i][1]-(t % (light[i][1] + light[i][2])))
        i+=1

print(t)
