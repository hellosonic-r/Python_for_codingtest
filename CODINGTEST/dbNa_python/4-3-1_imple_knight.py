###왕실의 나이트
##나의 풀이(성공))

location = list(str(input()))
location_num = []
if location[0] == "a":
    location_num.append(1)
    location_num.append(int(location[1]))
elif location[0] == "b":
    location_num.append(2)
    location_num.append(int(location[1]))
elif location[0] == "c":
    location_num.append(3)
    location_num.append(int(location[1]))
elif location[0] == "d":
    location_num.append(4)
    location_num.append(int(location[1]))
elif location[0] == "e":
    location_num.append(5)
    location_num.append(int(location[1]))
elif location[0] == "f":
    location_num.append(6)
    location_num.append(int(location[1]))
elif location[0] == "g":
    location_num.append(7)
    location_num.append(int(location[1]))
elif location[0] == "h":
    location_num.append(8)
    location_num.append(int(location[1]))

move_type = ["A","B","C","D","E","F","G","H"]

dx = [2,2,1,-1,-2,-2,-1,1]
dy = [1,-1,-2,-2,-1,1,2,2]

count = 0
for j in range(len(move_type)):
    nx, ny = 0, 0
    nx = location_num[0]+dx[j]
    ny = location_num[1]+dy[j]
    if nx < 1 or ny < 1 or nx > 8 or ny > 8:
        continue
    else:
        count += 1

print(count)
