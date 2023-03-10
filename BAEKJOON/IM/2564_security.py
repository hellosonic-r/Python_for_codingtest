result = 0
def find_distance(a,b, r, s):
    global n, m, result 
    if a == 1:
        if r == 2:
            result += min(b+m+s, (n-b)+m+(n-s))
        elif r == 3:
            result += b+s
        elif r == 4:
            result += n-b+s
        elif r == 1:
            result += abs(b-s)
    elif a == 2:
        if r == 1:
            result += min(b+m+s, (n-b)+m+(n-s))
        elif r == 3:
            result += b+m-s
        elif r == 4:
            result += n-b+m-s
        elif r == 2:
            result += abs(b-s)
    elif a == 3:
        if r == 1:
            result += b+s
        elif r == 2:
            result += m-b+s
        elif r == 4:
            result += min(b+n+s, (m-b)+n+(m-s))
        elif r == 3:
            result += abs(b-s)
    elif a == 4:
        if r == 1:
            result += b+n-s
        elif r == 2:
            result += m-b+n-s
        elif r == 3:
            result += min(b+n+s, (m-b)+n+(m-s))
        elif r == 4:
            result += abs(b-s)

n, m = map(int, input().split())
how_many_store = int(input())

direction_list = []
distance_list = []
for i in range(how_many_store):
    direction, distance = map(int, input().split())
    direction_list.append(direction)
    distance_list.append(distance)
dk_direction, dk_distance = map(int, input().split())


for i in range(how_many_store):
    find_distance(dk_direction,dk_distance,direction_list[i],distance_list[i])

print(result)