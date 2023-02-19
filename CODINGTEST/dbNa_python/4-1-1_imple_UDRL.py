###상하좌우
##나의풀이
n = int(input())
command_list = list(map(str, input().split()))

location = [1, 1]

for command in command_list:
    if command == "R":
        location[1] += 1
    elif command == "D":
        location[0] += 1
    elif command == "L":
        if location[1] == 1:
            continue
        else:
            location[1] -= 1
    elif command == "U":
        if location[0] == 1:
            continue
        else:
            location[0] -= 1

print(location[0],location[1])

