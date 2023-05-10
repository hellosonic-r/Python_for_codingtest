k = int(input())

height = []
width = []
total = []

for _ in range(6):
    dir, m = map(int, input().split())
    if dir == 1 or dir == 2:
        width.append(m)
        total.append(m)
    elif dir == 3 or dir == 4:
        height.append(m)
        total.append(m)

big = max(height) * max(width)

small_width = total[(total.index(max(height))+3)%6]
small_height = total[(total.index(max(width))+3)%6]

print(k * (big-small_height*small_width))
