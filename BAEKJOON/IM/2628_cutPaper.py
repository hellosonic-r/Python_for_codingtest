n, m = map(int, input().split())
cut = int(input())

x_points = [0]
y_points = [0]

x_points.append(n)
y_points.append(m)

for i in range(cut):
    direction, point = map(int, input().split())
    if direction == 0:
        y_points.append(point)
    elif direction == 1:
        x_points.append(point)

x_points.sort()
y_points.sort()

x_width = []
y_height = []

for i in range(len(x_points)-1):
    if i == len(x_points) - 1:
        continue
    x_width.append(x_points[i+1]-x_points[i])
for j in range(len(y_points)-1):
    if j == len(y_points) - 1:
        continue
    y_height.append(y_points[j+1]-y_points[j])

area = 0
fin = 0

for x in x_width:
    for y in y_height:
        area = x*y
        if area >= fin:
            fin = area
        else:
            continue

print(fin)