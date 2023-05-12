w,h = map(int,input().split()) #w:가로 h:세로
n = int(input()) #상점의 개수
store = []
for _ in range(n):
    store.append(list(map(int, input().split())))
direction, x = map(int, input().split())

distance = 0

for (d, p) in store:
    if direction == 1:
        if d == 1:
            distance += abs(x-p)
        elif d == 2:
            distance += min(x+h+p, (w-x)+h+(w-p))
        elif d == 3:
            distance += (x+p)
        else:
            distance += ((w-x)+p)
    elif direction == 2:
        if d == 1:
            distance += min(x+h+p, (w-x)+h+(w-p))
        elif d == 2:
            distance += abs(x-p)
        elif d == 3:
            distance += (x+(h-p))
        else: 
            distance += ((w-x)+(h-p))
    elif direction == 3:
        if d == 1:
            distance += (x+p)
        elif d == 2:
            distance += ((h-x)+p)
        elif d == 3:
            distance += abs(x-p)
        else:
            distance += min(x+w+p, (h-x)+w+(h-p))
    else:
        if d == 1:
            distance += ((w-p) + x)
        elif d == 2:
            distance += ((h-x)+(w-p))
        elif d == 3:
            distance += min(x+w+p, (h-x)+w+(h-p))
        else:
            distance += abs(x-p)
            
print(distance)
