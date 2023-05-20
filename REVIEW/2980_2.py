n, l = map(int, input().split())
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))

distance = 0
light = 0
t = 0
while True:
    if distance == l:
        break
    distance+=1
    t+=1
    if distance == lst[light][0]:
        if t % (lst[light][1] + lst[light][2]) <= lst[light][1]:
            t += lst[light][1] - (t%(lst[light][1] + lst[light][2]))
        light += 1
        if light >= len(lst):
            light = 0


print(t)
